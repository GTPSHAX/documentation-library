---
title: Using-declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/using_declaration
---


# Using-declaration

Introduces a name that is defined elsewhere into the declarative region where this using-declaration appears. See <sup>(since C++20)</sup> ``using enum` and ```using namespace`` for other related declarations.

**Syntax:**

- `**`typename`** *nested-name-specifier* *unqualified-id* **`;`**|notes=<sup>(until C++17)</sup>`
- `*declarator-list* **`;`**|notes=<sup>(C++17)</sup>`

### Parameters

- `{{ttb` - typename|the keyword `typename` may be used as necessary to resolve `dependent name`s, when the using-declaration introduces a member type from a base class into a class template 
- `{{spar` - nested-name-specifier|a sequence of names and scope resolution operators `::`, ending with a scope resolution operator. A single `::` refers to the global namespace.
- `{{spar` - unqualified-id|an `id-expression` 
- `{{spar` - declarator-list|comma-separated list of one or more declarators of the **`typename`** *nested-name-specifier* *unqualified-id*. Some or all of the declarators may be followed by an ellipsis `...` to indicate `pack expansion`

## Explanation

Using-declarations can be used to introduce namespace members into other namespaces and block scopes, or to introduce base class members into derived class definitions<sup>(since C++20)</sup> , or to introduce `enumerators into namespaces, block, and class scopes`.
rrev|since=c++17|
A using-declaration with more than one using-declarator is equivalent to a corresponding sequence of using-declarations with one using-declarator.

### In namespace and block scope

`Using-declarations` introduce a member of another namespace into the current namespace or block scope.

```cpp
#include <iostream>
#include <string>

using std::string;

int main()
{
    string str = "Example";
    using std::cout;
    cout << str;
}
```

See `namespace` for details.

### In class definition

Using-declaration introduces a member of a base class into the derived class definition, such as to expose a protected member of base as public member of derived. In this case, *nested-name-specifier* must name a base class of the one being defined. If the name is the name of an overloaded member function of the base class, all base class member functions with that name are introduced. If the derived class already has a member with the same name, parameter list, and qualifications, the derived class member hides or overrides (doesn't conflict with) the member that is introduced from the base class.

### Example


**Output:**
```
D::f
D::f
----------
D::g
B::g
----------
B::h
D::h
```

rrev|since=c++11|1=

### Inheriting constructors

If the ''using-declaration'' refers to a constructor of a direct base of the class being defined (e.g. `using Base::Base;`), all constructors of that base (ignoring member access) are made visible to overload resolution when initializing the derived class.
If overload resolution selects an inherited constructor, it is accessible if it would be accessible when used to construct an object of the corresponding base class: the accessibility of the using-declaration that introduced it is ignored.
If overload resolution selects one of the inherited constructors when initializing an object of such derived class, then the `Base` subobject from which the constructor was inherited is initialized using the inherited constructor, and all other bases and members of `Derived` are initialized as if by the defaulted default constructor (default member initializers are used if provided, otherwise default initialization takes place). The entire initialization is treated as a single function call: initialization of the parameters of the inherited constructor is `sequenced before` initialization of any base or member of the derived object.

```cpp
struct B1 { B1(int, ...) {} };
struct B2 { B2(double)   {} };

int get();

struct D1 : B1
{
    using B1::B1; // inherits B1(int, ...)
    int x;
    int y = get();
};

void test()
{
    D1 d(2, 3, 4); // OK: B1 is initialized by calling B1(2, 3, 4),
                   // then d.x is default-initialized (no initialization is performed),
                   // then d.y is initialized by calling get()

    D1 e;          // Error: D1 has no default constructor
}

struct D2 : B2
{
    using B2::B2; // inherits B2(double)
    B1 b;
};

D2 f(1.0); // error: B1 has no default constructor
```


```cpp
struct W { W(int); };

struct X : virtual W
{
    using W::W; // inherits W(int)
    X() = delete;
};

struct Y : X
{
    using X::X;
};

struct Z : Y, virtual W
{
    using Y::Y;
};

Z z(0); // OK: initialization of Y does not invoke default constructor of X
```

If the `Base` base class subobject is not to be initialized as part of the `Derived` object (i.e., `Base` is a `virtual base class` of `Derived`, and the `Derived` object is not the `most derived object`), the invocation of the inherited constructor, including the evaluation of any arguments, is omitted:

```cpp
struct V
{
    V() = default;
    V(int);
};

struct Q { Q(); };

struct A : virtual V, Q
{
    using V::V;
    A() = delete;
};

int bar() { return 42; }

struct B : A
{
    B() : A(bar()) {} // OK
};

struct C : B {};

void foo()
{
    C c; // “bar” is not invoked, because the V subobject
         // is not initialized as part of B
         // (the V subobject is initialized as part of C,
         //  because “c” is the most derived object)
}
```

If the constructor was inherited from multiple base class subobjects of type `Base`, the program is ill-formed, similar to multiply-inherited non-static member functions:

```cpp
struct A { A(int); };
struct B : A { using A::A; };
struct C1 : B { using B::B; };
struct C2 : B { using B::B; };

struct D1 : C1, C2
{
    using C1::C1;
    using C2::C2;
};
D1 d1(0); // ill-formed: constructor inherited from different B base subobjects

struct V1 : virtual B { using B::B; };
struct V2 : virtual B { using B::B; };

struct D2 : V1, V2
{
    using V1::V1;
    using V2::V2;
};
D2 d2(0); // OK: there is only one B subobject.
          // This initializes the virtual B base class,
          //   which initializes the A base class
          // then initializes the V1 and V2 base classes
          //   as if by a defaulted default constructor
```

As with using-declarations for any other non-static member functions, if an inherited constructor matches the signature of one of the constructors of `Derived`, it is hidden from lookup by the version found in `Derived`. If one of the inherited constructors of `Base` happens to have the signature that matches a copy/move constructor of the `Derived`, it does not prevent implicit generation of `Derived` copy/move constructor (which then hides the inherited version, similar to `1=using operator=`).

```cpp
struct B1 { B1(int); };
struct B2 { B2(int); };

struct D2 : B1, B2
{
    using B1::B1;
    using B2::B2;

    D2(int); // OK: D2::D2(int) hides both B1::B1(int) and B2::B2(int)
};
D2 d2(0);    // calls D2::D2(int)
```

Within a `templated class`, if a using-declaration refers to a `dependent name`, it is considered to name a constructor if the *nested-name-specifier* has a terminal name that is the same as the *unqualified-id*.

```cpp
template<class T>
struct A : T
{
    using T::T; // OK, inherits constructors of T
};

template<class T, class U>
struct B : T, A<U>
{
    using A<U>::A; // OK, inherits constructors of A<U>
    using T::A;    // does not inherit constructor of T
                   // even though T may be a specialization of A<>
};
```

rrev|since=c++20|

### Introducing scoped enumerators

In addition to members of another namespace and members of base classes, using-declaration can also introduce enumerators of `enumerations` into namespace, block, and class scopes.
A using-declaration can also be used with unscoped enumerators.

```cpp
enum class button { up, down };

struct S
{
    using button::up;
    button b = up; // OK
};

using button::down;
constexpr button non_up = down; // OK

constexpr auto get_button(bool is_up)
{
    using button::up, button::down;
    return is_up ? up : down; // OK
}

enum unscoped { val };
using unscoped::val; // OK, though needless
```


## Notes

Only the name explicitly mentioned in the using-declaration is transferred into the declarative scope: in particular, enumerators are not transferred when the enumeration type name is using-declared.
A using-declaration cannot refer to a namespace<sup>(until C++20)</sup> , to a scoped enumerator, to a destructor of a base class or to a specialization of a member template for a user-defined conversion function.
A using-declaration cannot name a member template specialization (`template-id` is not permitted by the grammar):

```cpp
struct B
{
    template<class T>
    void f();
};

struct D : B
{
    using B::f;      // OK: names a template
//  using B::f<int>; // Error: names a template specialization

    void g() { f<int>(); }
};
```

A using-declaration also can't be used to introduce the name of a dependent member template as a ''template-name'' (the `template` disambiguator for `dependent name`s is not permitted).

```cpp
template<class X>
struct B
{
    template<class T>
    void f(T);
};

template<class Y>
struct D : B<Y>
{
//  using B<Y>::template f; // Error: disambiguator not allowed
    using B<Y>::f;          // compiles, but f is not a template-name

    void g()
    {
//      f<int>(0);          // Error: f is not known to be a template name,
                            // so < does not start a template argument list
        f(0);               // OK
    }   
};
```

If a using-declaration brings the base class assignment operator into derived class, whose signature happens to match the derived class's copy-assignment or move-assignment operator, that operator is hidden by the implicitly-declared copy/move assignment operator of the derived class. <sup>(since C++11)</sup> Same applies to a using-declaration that inherits a base class constructor that happens to match the derived class copy/move constructor.
rrev|since=c++11|1=
The semantics of inheriting constructors were retroactively changed by a defect report against C++11. Previously, an inheriting constructor declaration caused a set of synthesized constructor declarations to be injected into the derived class, which caused redundant argument copies/moves, had problematic interactions with some forms of SFINAE, and in some cases can be unimplementable on major ABIs. Older compilers may still implement the previous semantics.
If the ''using-declaration'' refers to a constructor of a direct base of the class being defined (e.g. `using Base::Base;`), constructors of that base class are inherited, according to the following rules:
1. A set of ''candidate inheriting constructors'' is composed of
:@a@ All non-template constructors of the base class <sup>(since C++14)</sup> (after omitting ellipsis parameters, if any)
:@b@ For each constructor with default arguments or the ellipsis parameter, all constructor signatures that are formed by dropping the ellipsis and omitting default arguments from the ends of argument lists one by one
:@c@ All constructor templates of the base class <sup>(since C++14)</sup> (after omitting ellipsis parameters, if any)
:@d@ For each constructor template with default arguments or the ellipsis, all constructor signatures that are formed by dropping the ellipsis and omitting default arguments from the ends of argument lists one by one
2. All candidate inherited constructors that aren't the default constructor or the copy/move constructor and whose signatures do not match user-defined constructors in the derived class, are implicitly declared in the derived class. The default parameters are not inherited:

```cpp
struct B1
{
    B1(int);
};

struct D1 : B1
{
    using B1::B1;

    // The set of candidate inherited constructors is 
    // 1. B1(const B1&)
    // 2. B1(B1&&)
    // 3. B1(int)

    // D1 has the following constructors:
    // 1. D1() = delete
    // 2. D1(const D1&) 
    // 3. D1(D1&&)
    // 4. D1(int) <- inherited
};

struct B2
{
    B2(int = 13, int = 42);
};

struct D2 : B2
{
    using B2::B2;

    // The set of candidate inherited constructors is
    // 1. B2(const B2&)
    // 2. B2(B2&&)
    // 3. B2(int = 13, int = 42)
    // 4. B2(int = 13)
    // 5. B2()

    // D2 has the following constructors:
    // 1. D2()
    // 2. D2(const D2&)
    // 3. D2(D2&&)
    // 4. D2(int, int) <- inherited
    // 5. D2(int) <- inherited
};
```

The inherited constructors are equivalent to user-defined constructors with an empty body and with a `member initializer list` consisting of a single *nested-name-specifier*, which forwards all of its arguments to the base class constructor.
It has the same `access` as the corresponding base constructor. It is `constexpr` if the user-defined constructor would have satisfied `constexpr` constructor requirements. It is deleted if the corresponding base constructor is deleted or if a defaulted default constructor would be deleted (except that the construction of the base whose constructor is being inherited doesn't count). An inheriting constructor cannot be explicitly instantiated or explicitly specialized.
If two using-declarations inherit the constructor with the same signature (from two direct base classes), the program is ill-formed.
An inheriting constructor template should not be `explicitly instantiated` or `explicitly specialized`.
rrev|since=c++17|
`Pack expansions` in using-declarations make it possible to form a class that exposes overloaded members of variadic bases without recursion:

```cpp
template<typename... Ts>
struct Overloader : Ts...
{
    using Ts::operator()...; // exposes operator() from every base
};

template<typename... T>
Overloader(T...) -> Overloader<T...>; // C++17 deduction guide, not needed in C++20

int main()
{
    auto o = Overloader{ [] (auto const& a) {std::cout << a;},
                         [] (float f) {std::cout << std::setprecision(3) << f;} };
}
```


## Keywords

`cpp/keyword/using`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-258 | C++98 | a non-const member function of a derived class can<br>override and/or hide a const member function of its base | overriding and hiding also require<br>cv-qualifications to be the same |
| cwg-1738 | C++11 | it was not clear whether it is permitted to<br>explicitly instantiate or explicitly specialize<br>specializations of inheriting constructor templates | prohibited |
| cwg-2504 | C++11 | the behavior of inheriting constructors<br>from virtual base classes was unclear | made clear |


## References

