---
title: static members
type: Language
source: https://en.cppreference.com/w/cpp/language/static
---


# tt|static

Inside a class definition, the keyword `cpp/keywords/static` declares members that are not bound to class instances.
Outside a class definition, it has a different meaning: see `storage duration`.

## Syntax

A declaration for a static member is a `member declaration` whose declaration specifiers contain the keyword `static`. The keyword `static` usually appears before other specifiers (which is why the syntax is often informally described as `static` *member-declaration*), but may appear anywhere in the specifier sequence.
The name of any static data member and static member function must be different from the name of the containing class.

## Explanation

Static members of a class are not associated with the objects of the class: they are independent variables with static<sup>(since C++11)</sup>  or thread `storage duration` or regular functions.
The `static` keyword is only used with the declaration of a static member, inside the class definition, but not with the definition of that static member:

```cpp
class X { static int n; }; // declaration (uses 'static')
int X::n = 1;              // definition (does not use 'static')
```

The declaration inside the class body is not a definition and may declare the member to be of `incomplete type` (other than `void`), including the type in which the member is declared:

```cpp
struct Foo;

struct S
{
    static int a[]; // declaration, incomplete type
    static Foo x;   // declaration, incomplete type
    static S s;     // declaration, incomplete type (inside its own definition)
};

int S::a[10]; // definition, complete type
struct Foo {};
Foo S::x;     // definition, complete type
S S::s;       // definition, complete type
```

rrev|since=c++11|
However, if the declaration uses `cpp/language/constexpr`<sup>(since C++17)</sup>  or `cpp/language/inline` specifier, the member must be declared to have complete type.
To refer to a static member `m` of class `T`, two forms may be used: qualified name `T::m` or member access expression `E.m` or `E->m`, where `E` is an expression that evaluates to `T` or `T*` respectively. When in the same class scope, the qualification is unnecessary:

```cpp
struct X
{
    static void f(); // declaration
    static int n;    // declaration
};

X g() { return X(); } // some function returning X

void f()
{
    X::f();  // X::f is a qualified name of static member function
    g().f(); // g().f is member access expression referring to a static member function
}

int X::n = 7; // definition

void X::f() // definition
{
    n = 1; // X::n is accessible as just n in this scope
}
```

Static members obey the `class member access rules (private, protected, public)`.

### Static member functions

Static member functions are not associated with any object. When called, they have no `this` pointer.
Static member functions cannot be `virtual`, `const`, `volatile`, or `ref-qualified`.
The address of a static member function may be stored in a regular `pointer to function`, but not in a `pointer to member function`.

### Static data members

Static data members are not associated with any object. They exist even if no objects of the class have been defined. There is only one instance of the static data member in the entire program with static `storage duration`<sup>(since C++11)</sup> , unless the keyword `cpp/keyword/thread_local` is used, in which case there is one such object per thread with thread storage duration.
Static data members cannot be `mutable`.
Static data members of a class in namespace scope have `external linkage` if the class itself has external linkage (is not a member of `unnamed namespace`). Local classes (classes defined inside functions) and unnamed classes, including member classes of unnamed classes, cannot have static data members.
rrev|since=c++17|
A static data member may be declared `cpp/language/inline`. An inline static data member can be defined in the class definition and may specify an initializer. It does not need an out-of-class definition:

```cpp
struct X
{
    inline static int fully_usable = 1; // No out-of-class definition required,
                                        // ODR-usable
    inline static const std::string class_name{"X"}; // Likewise

    static const int non_addressable = 1; // C.f. non-inline constants, usable
                                          // for its value, but not ODR-usable
    // static const std::string class_name{"X"}; // Non-integral declaration of this
                                                 // form is disallowed entirely
};
```


### Constant static members

If a static data member of integral or enumeration type is declared `const` (and not `volatile`), it can be initialized with an `initializer` in which every expression is a `constant expression`, right inside the class definition:

```cpp
struct X
{
    const static int n = 1;
    const static int m{2}; // since C++11
    const static int k;
};
const int X::k = 3;
```

rrev|since=c++11|
If a static data member of *LiteralType* is declared `constexpr`, it must be initialized with an initializer in which every expression is a constant expression, right inside the class definition:

```cpp
struct X
{
    constexpr static int arr[] = { 1, 2, 3 };        // OK
    constexpr static std::complex<double> n = {1,2}; // OK
    constexpr static int k; // Error: constexpr static requires an initializer
};
```

If a const <sup>(since C++17)</sup> non-inline static data member <sup>(since C++11)</sup> until=c++17|or a constexpr static data member is , a definition at namespace scope is still required, but it cannot have an initializer.
rrev|since=c++17|
A `constexpr` static data member is implicitly `inline` and does not need to be redeclared at namespace scope. This redeclaration without an initializer (formerly required) is still permitted, but is deprecated.

```cpp
struct X
{
    static const int n = 1;
    static constexpr int m = 4;
};

const int *p = &X::n, *q = &X::m; // X::n and X::m are ODR-used
const int X::n;             // … so a definition is necessary
constexpr int X::m;         // … (except for X::m in C++17)
```


## Keywords

`cpp/keyword/static`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-194 | C++98 | (static) member function names can be the same as the class name | naming restriction added (including<br>rlp |


## References


## See also

* ``static` storage specifier`
