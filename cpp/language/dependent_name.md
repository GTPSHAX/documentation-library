---
title: Dependent names
type: Language
source: https://en.cppreference.com/w/cpp/language/dependent_name
---


# Dependent names

Inside the definition of a `template` (both `class template` and `function template`), the meaning of some constructs may differ from one instantiation to another. In particular, types and expressions may depend on types of type template parameters and values of non-type template parameters.

```cpp
template<typename T>
struct X : B<T> // “B<T>” is dependent on T
{
    typename T::A* pa; // “T::A” is dependent on T
                       // (see below for the meaning of this use of “typename”)

    void f(B<T>* pb)
    {
        static int i = B<T>::i; // “B<T>::i” is dependent on T
        pb->j++; // “pb->j” is dependent on T
    }
};
```

Name `lookup` and binding are different for dependent names and non-dependent names.

## Binding rules

Non-dependent names are looked up and bound at the point of template definition. This binding holds even if at the point of template instantiation there is a better match:

### Example

```cpp
#include <iostream>

void g(double) { std::cout << "g(double)\n"; }

template<class T>
struct S
{
    void f() const
    {
        g(1); // “g” is a non-dependent name, bound now
    }
};

void g(int) { std::cout << "g(int)\n"; }

int main()
{
    g(1);  // calls g(int)

    S<int> s;
    s.f(); // calls g(double)
}
```

If the meaning of a non-dependent name changes between the definition context and the point of instantiation of a specialization of the template, the program is ill-formed, no diagnostic required. This is possible in the following situations:
* a type used in a non-dependent name is `incomplete` at the point of definition but complete at the point of instantiation
rrev|since=c++17|
* lookup for a name in the template definition found a `using-declaration`, but the lookup in the corresponding scope in the instantiation does not find any declarations because the using-declaration was a pack expansion and the corresponding pack is empty
* an instantiation uses a default argument or default template argument that had not been defined at the point of definition
* a `constant expression` at the point of instantiation uses the value of a const object of integral or unscoped enum type<sup>(since C++11)</sup> , the value of a constexpr object, the value of a reference, or the definition of a constexpr function, and that object<sup>(since C++11)</sup> /reference/function was not defined at the point of definition
* the template uses a non-dependent class template specialization <sup>(since C++14)</sup> or variable template specialization at the point of instantiation, and this template it uses is either instantiated from a partial specialization that was not defined at the point of definition or names an explicit specialization that was not declared at the point of definition
Binding of dependent names is postponed until lookup takes place.

## Lookup rules

The `lookup` of a dependent name used in a template is postponed until the template arguments are known, at which time
* non-ADL lookup examines function declarations with external linkage that are visible from the template definition context
* `ADL` examines function declarations with external linkage that are visible from either the template definition context or the template instantiation context
(in other words, adding a new function declaration after template definition does not make it visible, except via ADL).
The purpose of this rule is to help guard against violations of the `ODR` for template instantiations:

```cpp
// an external library
namespace E
{
    template<typename T>
    void writeObject(const T& t)
    {
        std::cout << "Value = " << t << '\n';
    }
}

// translation unit 1:
// Programmer 1 wants to allow E::writeObject to work with vector<int>
namespace P1
{
    std::ostream& operator<<(std::ostream& os, const std::vector<int>& v)
    {
        for (int n : v)
            os << n << ' ';
        return os;
    }

    void doSomething()
    {
        std::vector<int> v;
        E::writeObject(v); // Error: will not find P1::operator<<
    }
}

// translation unit 2:
// Programmer 2 wants to allow E::writeObject to work with vector<int>
namespace P2
{
    std::ostream& operator<<(std::ostream& os, const std::vector<int>& v)
    {
        for (int n : v)
            os << n << ':';
        return os << "[]";
    }

    void doSomethingElse()
    {
        std::vector<int> v;
        E::writeObject(v); // Error: will not find P2::operator<<
    }
}
```

In the above example, if non-ADL lookup for `operator<<` were allowed from the instantiation context, the instantiation of `E::writeObject<vector<int>>` would have two different definitions: one using `P1::operator<<` and one using `P2::operator<<`. Such ODR violation may not be detected by the linker, leading to one or the other being used in both instances.
To make ADL examine a user-defined namespace, either `std::vector` should be replaced by a user-defined class or its element type should be a user-defined class:

```cpp
namespace P1
{
    // if C is a class defined in the P1 namespace
    std::ostream& operator<<(std::ostream& os, const std::vector<C>& v)
    {
        for (C n : v)
            os << n;
        return os;
    }

    void doSomething()
    {
        std::vector<C> v;
        E::writeObject(v); // OK: instantiates writeObject(std::vector<P1::C>)
                           //     which finds P1::operator<< via ADL
    }
}
```

Note: this rule makes it impractical to overload operators for standard library types:

### Example

```cpp
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

// Bad idea: operator in global namespace, but its arguments are in std::
std::ostream& operator<<(std::ostream& os, std::pair<int, double> p)
{
    return os << p.first << ',' << p.second;
}

int main()
{
    typedef std::pair<int, double> elem_t;
    std::vector<elem_t> v(10);
    std::cout << v[0] << '\n'; // OK, ordinary lookup finds ::operator<<
    std::copy(v.begin(), v.end(),
              std::ostream_iterator<elem_t>(std::cout, " "));
    // Error: both ordinary lookup from the point of definition of
    // std::ostream_iterator and ADL will only consider the std namespace,
    // and will find many overloads of std::operator<<, so the lookup will be done.
    // Overload resolution will then fail to find operator<< for elem_t
    // in the set found by the lookup.
}
```

Note: limited lookup (but not binding) of dependent names also takes place at template definition time, as needed to distinguish them from non-dependent names and also to determine whether they are members of the current instantiation or members of unknown specialization. The information obtained by this lookup can be used to detect errors, see below.

## Dependent types

The following types are ''dependent types'':
* template parameter
* a member of an unknown specialization (see below)
* a nested class/enum that is a dependent member of unknown specialization (see below)
* a cv-qualified version of a dependent type
* a compound type constructed from a dependent type
* an array type whose element type is dependent or whose bound (if any) is value-dependent
rrev|since=c++11|
* a function type whose parameters include one or more function `parameter pack`s
* a function type whose exception specification is value-dependent
* a `template identifier` where either
:* the template name is a template parameter, or
:* any of template arguments is type-dependent, or value-dependent<sup>(since C++11)</sup> , or is a pack expansion (even if the template identifier is used without its argument list, as `injected-class-name`)
rev|since=c++11|
* the result of `decltype` applied to a type-dependent expression
: The result of `decltype` applied to a type-dependent expression is a unique dependent type. Two such results refer to the same type only if their expressions are `equivalent`.
rev|since=c++26|
* the  applied to a type-dependent constant expression
: The pack indexing specifier applied to a type-dependent constant expression is a unique dependent type. Two such pack indexing specifiers refer to the same type only if their constant expressions are equivalent. Otherwise, two such pack indexing specifiers refer to the same type only if their indices have the same value.
* the result of `splice type specifier` applied to a dependent constant expression
Note: a typedef member of a current instantiation is only dependent when the type it refers to is.

## Type-dependent expressions

The following expressions are ''type-dependent'':
* an expression whose any subexpression is a type-dependent expression
* `this`, if the class is a dependent type.
* an `identifier expression` that<sup>(since C++20)</sup>  is not a `concept-id and` satisfies any of the following conditions:
:* contains an identifier for which name lookup finds at least one dependent declaration
:* contains a dependent `template identifier`
:* contains the name of `conversion function` to a dependent type
:* contains a nested name specifier or `qualified identifier` that is a member of unknown specialization
:* names a dependent member of the current instantiation which is a static data member of type “array of unknown bound”
rev|since=c++11|
:* contains the special identifier `__func__` (if some enclosing function is a template, a non-template member of a class template<sup>(since C++14)</sup> , or a generic lambda)
rev|since=c++14|
:* contains an identifier for which name lookup finds one or more declarations of member functions of the current instantiation declared with
rev|since=c++17|
:* contains an identifier for which name lookup finds a `structured binding declaration` whose initializer is type-dependent
:* contains an identifier for which name lookup finds a non-type template parameter whose type contains the placeholder `auto`
:* contains an identifier for which by name lookup finds a variable declared with a type that contains a `placeholder type` (e.g., `auto` static data member), where the initializer is type-dependent
rev|since=c++26|
:* contains an identifier for which name lookup finds a `pack`
:* contains a name introduced by the *item-declaration* of an `expansion statement` `S`, where the type specified for that name contains a `placeholder type` and either
::* `S` is not an , or
::* the *expansion-initializer* of `S` is type-dependent
* any cast expression to a dependent type
* ``new` expression` that creates an object of a dependent type
* member access expression that refers to a member of the current instantiation whose type is dependent
* member access expression that refers to a member of unknown specialization
rrev|since=c++17|
* `fold expression`
rrev|since=c++26|
* `pack indexing expression` if its identifier expression is a type-dependent expression
The following expressions are never type-dependent because the types of these expressions cannot be:
*
* pseudo-destructor calls
* `sizeof`
rrev|since=c++11|
* `sizeof...`
* `alignof`
* `noexcept`
* `throw`
* `typeid`
* `delete`
rev|since=c++20|
* `requires`
rev|since=c++26|
* `reflection operator` `^^`

## Value-dependent expressions

The following expressions are ''value-dependent'':
* an expression used in context where `constant expression` is required, and whose any subexpression is value-dependent
* an `identifier expression` that satisfies any of the following conditions:
:* It is type-dependent.
:* It is a name of a non-type template parameter.
:* It names a static data member that is a dependent member of the current instantiation and is not initialized.
:* It names a static member function that is a dependent member of the current instantiation.
:* It is a constant with a <sup>(until C++11)</sup> integer or enumeration<sup>(since C++11)</sup> literal type, initialized from a value-dependent expression.
rev|since=c++20|
:* It is a `concept-id` and any of its arguments are dependent.
rev|since=c++26|
:* It is a name introduced by the *item-declaration* of an `expansion statement`.
* the following expressions where the operand is a type-dependent expression:
:* `sizeof`
:* `typeid`
rrev|since=c++11|
:* `alignof`
* the following expressions where the operand is a dependent type-id:
:* `sizeof`
:* `typeid`
* the following expressions where the target type is dependent or the operand is a type-dependent expression:
:* `C-style cast`
:* `static_cast`
:* `const_cast`
:* `reinterpret_cast`
:* `dynamic_cast`
* `function-style cast` expression where the target type is dependent or a value-dependent expression is enclosed by parentheses<sup>(since C++11)</sup>  or braces
rev|since=c++11|
* `sizeof...` expression<sup>(since C++26)</sup>  where the operand is not a `structured binding pack`
rev|since=c++17|
* `fold expression`
* address-of expression where the argument is a `qualified identifier` that names a dependent member of the current instantiation
* address-of expression where the argument is any expression which, evaluated as a core `constant expression`, refers to a  that is an object with static <sup>(since C++11)</sup> or thread storage duration or a member function.
rrev|since=c++26|

## Dependent namespaces

`Namespace` names are dependent if they are introduced by `namespace alias` definitions that contain dependent `splice specifiers`.

```cpp
template <std::meta::info R> int fn() {
    namespace Alias = [:R:];  // [:R:] is dependent
    return typename Alias::T{};  // Alias is dependent
}

namespace NS {
    using T = int;
}

int a = fn<^^NS>();
```


## Dependent names

> **TODO:** reword to maybe make it more clear (or at least less intimidating), and while at it, apply

## Current instantiation

Within a class template definition (including its member functions and nested classes) some names may be deduced to refer to the ''current instantiation''. This allows certain errors to be detected at the point of definition, rather than instantiation, and removes the requirement on the `typename` and `template` disambiguators for dependent names, see below.
Only the following names can refer to the current instantiation:
* in the definition of a class template, a nested class of a class template, a member of a class template, or a member of a nested class of a class template:
** the injected-class-name of the class template or nested class
* in the definition of a primary class template or a member of a primary class template:
** the name of the class template followed by template argument list (or an equivalent alias template specialization) for the primary template where each argument is equivalent (defined below) to its corresponding parameter.
* in the definition of a nested class of a class template:
** the name of the nested class used as a member of the current instantiation
* in the definition of a class template partial specialization or a member of a class template partial specialization:
** the name of the class template followed by template argument list for the partial specialization, where each argument is equivalent to its corresponding parameter
* in the definition of a `templated function`:
** the name of a `local class`
A template argument is equivalent to a template parameter if
* for a `type parameter`, the template argument denotes the same type as the template parameter.
* for a `non-type parameter`, the template argument is an `identifier` that names a variable that is equivalent to the template parameter. A variable is equivalent to a template parameter if
:* it has the same type as the template parameter (ignoring cv-qualification) and
:* its initializer consists of a single identifier that names the template parameter or, recursively, such a variable.

```cpp
template<class T>
class A
{
    A* p1;      // A is the current instantiation
    A<T>* p2;   // A<T> is the current instantiation
    ::A<T>* p4; // ::A<T> is the current instantiation
    A<T*> p3;   // A<T*> is not the current instantiation

    class B
    {
        B* p1;                 // B is the current instantiation
        A<T>::B* p2;           // A<T>::B is the current instantiation
        typename A<T*>::B* p3; // A<T*>::B is not the current instantiation
    };
};

template<class T>
class A<T*>
{
    A<T*>* p1; // A<T*> is the current instantiation
    A<T>* p2;  // A<T> is not the current instantiation
};

template<int I>
struct B
{
    static const int my_I = I;
    static const int my_I2 = I + 0;
    static const int my_I3 = my_I;
    static const long my_I4 = I;
    static const int my_I5 = (I);

    B<my_I>* b1;  // B<my_I> is the current instantiation:
                  //   my_I has the same type as I,
                  //   and it is initialized with only I
    B<my_I2>* b2; // B<my_I2> is not the current instantiation:
                  //   I + 0 is not a single identifier
    B<my_I3>* b3; // B<my_I3> is the current instantiation:
                  //   my_I3 has the same type as I,
                  //   and it is initialized with only my_I (which is equivalent to I)
    B<my_I4>* b4; // B<my_I4> is not the current instantiation:
                  //   the type of my_I4 (long) is not the same as the type of I (int)
    B<my_I5>* b5; // B<my_I5> is not the current instantiation:
                  //   (I) is not a single identifier
};
```

Note that a base class can be the current instantiation if a nested class derives from its enclosing class template. Base classes that are dependent types but are not the current instantiation are ''dependent base classes'':

```cpp
template<class T>
struct A
{
    typedef int M;

    struct B
    {
        typedef void M;

        struct C;
    };
};

template<class T>
struct A<T>::B::C : A<T>
{
    M m; // OK, A<T>::M
};
```

A name is classified as a member of the current instantiation if it is
* an unqualified name that is found by `unqualified lookup` in the current instantiation or in its non-dependent base.
* `qualified name`, if the qualifier (the name to the left of **`::`**) names the current instantiation and lookup finds the name in the current instantiation or in its non-dependent base
* a name used in a class member access expression (`y` in `x.y` or `xp->y`), where the object expression (`x` or `*xp`) is the current instantiation and lookup finds the name in the current instantiation or in its non-dependent base

```cpp
template<class T>
class A
{
    static const int i = 5;

    int n1[i];       // i refers to a member of the current instantiation
    int n2[A::i];    // A::i refers to a member of the current instantiation
    int n3[A<T>::i]; // A<T>::i refers to a member of the current instantiation

    int f();
};

template<class T>
int A<T>::f()
{
    return i; // i refers to a member of the current instantiation
}
```

Members of the current instantiation may be both dependent and non-dependent.
If the lookup of a member of current instantiation gives a different result between the point of instantiation and the point of definition, the lookup is ambiguous. Note however that when a member name is used, it is not automatically converted to a class member access expression, only explicit member access expressions indicate members of current instantiation:

```cpp
struct A { int m; };
struct B { int m; };

template<typename T>
struct C : A, T
{
    int f() { return this->m; } // finds A::m in the template definition context
    int g() { return m; }       // finds A::m in the template definition context
};

template int C<B>::f(); // error: finds both A::m and B::m

template int C<B>::g(); // OK: transformation to class member access syntax
                        // does not occur in the template definition context
```


## Unknown specializations

Within a template definition, certain names are deduced to belong to an ''unknown specialization'', in particular,
* a `qualified name`, if any name that appears to the left of **`::`** is a dependent type that is not a member of the current instantiation
* a `qualified name`, whose qualifier is the current instantiation, and the name is not found in the current instantiation or any of its non-dependent base classes, and there is a dependent base class
* a name of a member in a class member access expression (the `y` in `x.y` or `xp->y`), if the type of the object expression (`x` or `*xp`) is a dependent type and is not the current instantiation
* a name of a member in a class member access expression (the `y` in `x.y` or `xp->y`), if the type of the object expression (`x` or `*xp`) is the current instantiation, and the name is not found in the current instantiation or any of its non-dependent base classes, and there is a dependent base class

```cpp
template<typename T>
struct Base {};

template<typename T>
struct Derived : Base<T>
{
    void f()
    {
        // Derived<T> refers to current instantiation
        // there is no “unknown_type” in the current instantiation
        // but there is a dependent base (Base<T>)
        // Therefore, “unknown_type” is a member of unknown specialization
        typename Derived<T>::unknown_type z;
    }
};

template<>
struct Base<int> // this specialization provides it
{
    typedef int unknown_type;
};
```

This classification allows the following errors to be detected at the point of template definition (rather than instantiation):
* If any template definition has a `qualified name` in which the qualifier refers to the current instantiation and the name is neither a member of current instantiation nor a member of unknown specialization, the program is ill-formed (no diagnostic required) even if the template is never instantiated.

```cpp
template<class T>
class A
{
    typedef int type;

    void f()
    {
        A<T>::type i; // OK: “type” is a member of the current instantiation
        typename A<T>::other j; // Error:

        // “other” is not a member of the current instantiation
        // and it is not a member of an unknown specialization
        // because A<T> (which names the current instantiation),
        // has no dependent bases for “other” to hide in.
    }
};
```

* If any template definition has a member access expression where the object expression is the current instantiation, but the name is neither a member of current instantiation nor a member of unknown specialization, the program is ill-formed even if the template is never instantiated.
Members of unknown specialization are always dependent, and are looked up and bound at the point of instantiation as all dependent names (see above)

## The `typename` disambiguator for dependent names

In a declaration or a definition of a template, including alias template, a name that is not a member of the current instantiation and is dependent on a template parameter is not considered to be a type unless the keyword `typename` is used or unless it was already established as a type name, e.g. with a typedef declaration or by being used to name a base class.

### Example

```cpp
#include <iostream>
#include <vector>

int p = 1;

template<typename T>
void foo(const std::vector<T> &v)
{
    // std::vector<T>::const_iterator is a dependent name,
    typename std::vector<T>::const_iterator it = v.begin();

    // without “typename”, the following is parsed as multiplication
    // of the type-dependent data member “const_iterator”
    // and some variable “p”. Since there is a global “p” visible
    // at this point, this template definition compiles.
    std::vector<T>::const_iterator* p;

    typedef typename std::vector<T>::const_iterator iter_t;
    iter_t * p2; // “iter_t” is a dependent name, but it is known to be a type name
}

template<typename T>
struct S
{
    typedef int value_t; // member of current instantiation

    void f()
    {
        S<T>::value_t n{}; // S<T> is dependent, but “typename” not needed
        std::cout << n << '\n';
    }
};

int main()
{
    std::vector<int> v;
    foo(v); // template instantiation fails: there is no member variable
            // called “const_iterator” in the type std::vector<int>
    S<int>().f();
}
```

The keyword `typename` may only be used in this way before qualified names (e.g. `T::x`), but the names need not be dependent.
Usual `qualified name lookup` is used for the identifier prefixed by `typename`. Unlike the case with `elaborated type specifier`, the lookup rules do not change despite the qualifier:

```cpp
struct A // A has a nested variable X and a nested type struct X
{
    struct X {};
    int X;
};

struct B
{
    struct X {}; // B has a nested type struct X
};

template<class T>
void f(T t)
{
    typename T::X x;
}

void foo()
{
    A a;
    B b;
    f(b); // OK: instantiates f<B>, T::X refers to B::X
    f(a); // error: cannot instantiate f<A>:
          // because qualified name lookup for A::X finds the data member
}
```

The keyword `typename` can be used even outside of templates.

```cpp
#include <vector>

int main()
{
    // Both OK (after resolving CWG 382)
    typedef typename std::vector<int>::const_iterator iter_t;
    typename std::vector<int> v;
}
```

rrev|since=c++26|
The `typename` keyword can also be used in a `splice specifier` to indicate that it designates a type.
rrev|since=c++20|
In some contexts, only type names can validly appear. In these contexts, a dependent qualified name <sup>(since C++26)</sup> or a splice specifier is assumed to name a type and no `typename` is required:
* A qualified name that is used as a `declaration specifier` in the (top-level) *decl-specifier-seq* of:
:* a  or  at namespace scope;
:* a `class member declaration`;
:* a `parameter declaration` in a `class member declaration` (including friend function declarations), outside of default arguments;
:* a `parameter declaration` of a `declarator for a function or function template` whose name is qualified, outside of default arguments;
:* a `parameter declaration` of a `lambda expression` outside of default arguments;
:* a parameter declaration of a ``requires` expression`;
:* the type in the declaration of a ;
* A qualified name that appears in `type-id`, where the smallest enclosing type-id is:
:* the *type* in a `new expression` that does not parenthesize its type;
:* the *type-id* in an `alias declaration`;
:* a `trailing return type`,
:* a `default argument of a type template parameter`, or
:* the *type-id* of a `static_cast`, `dynamic_cast`, `const_cast`, or `reinterpret_cast`.

## The `template` disambiguator for dependent names

Similarly, in a template definition, a dependent name that is not a member of the current instantiation is not considered to be a template name unless the disambiguation keyword `template` is used or unless it was already established as a template name:
The keyword `template` may only be used in this way after operators `::` (scope resolution), `->` (member access through pointer), and `.` (member access), the following are all valid examples:
* `T::template foo<X>();`
* `s.template foo<X>();`
* `this->template foo<X>();`
* `typename T::template iterator<int>::value_type v;`
As is the case with `typename`, the `template` prefix is allowed even if the name is not dependent or the use does not appear in the scope of a template.
Even if the name to the left of **`::`** refers to a namespace, the template disambiguator is allowed:

```cpp
template<typename>
struct S {};

::template S<void> q; // allowed, but unnecessary
```

rrev|until=c++23|
Due to the special rules for `unqualified name lookup` for template names in member access expressions, when a non-dependent template name appears in a member access expression (after `->` or after `.`), the disambiguator is unnecessary if there is a <sup>(since C++11)</sup> class or alias template with the same name found by ordinary lookup in the context of the expression. <sup>(until C++11)</sup> However, if the template found by lookup in the context of the expression differs from the one found in the context of the class, the program is ill-formed

```cpp
template<int>
struct A { int value; };

template<class T>
void f(T t)
{
    t.A<0>::value; // Ordinary lookup of A finds a class template.
                   // A<0>::value names member of class A<0>
    // t.A < 0;    // Error: “<” is treated as the start of template argument list
}
```

rrev|since=c++26|
The `template` keyword can also be used in a `splice specifier` to indicate that it designates a template.

## Keywords

`cpp/keyword/template`,
`cpp/keyword/typename`

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-206 | C++98 | it was unspecified at what point semantic constraints are<br>applied when a type used in a non-dependent name is<br>incomplete at the point at which a template is defined but is<br>complete at the point at which an instantiation is performed | the program is ill-formed<br>and no diagnostic is<br>required in this case |
| cwg-224 | C++98 | the definition of dependent types was based<br>on the form of the name rather than lookup | definition revamped |
| cwg-502 | C++98 | it was unspecified whether nested enumerations are dependent | dependent as nested classes |
| cwg-1160 | C++98 | it was unspecified whether a name refers to the current instantiation<br>when a template identifier matching a primary template or partial<br>specialization appears in the definition of a member of the template | specified |
| cwg-1413 | C++98 | uninitialized static data member, static member function, and address<br>of member of a class template were not listed as value-dependent | listed |
| cwg-1471 | C++98 | a nested type of a non-dependent base of<br>the current instantiation was dependent | it is not dependent |
| cwg-1850 | C++98 | the list of cases that meaning may change between the<br>definition context and the point of instantiation was incomplete | made complete |
| cwg-2100 | C++98 | address of a static data member of class<br>template was not listed as value-dependent | listed |
| cwg-2109 | C++98 | type-dependent identifier expressions might not be value-dependent | they are always<br>value-dependent |
| cwg-2276 | C++98 | a function type whose exception specification<br>is value-dependent was not a dependent type | it is |
| cwg-2307 | C++98 | a parenthesized non-type template parameter used as a<br>template argument was equivalent to that template parameter | not equivalent anymore |
| cwg-2457 | C++11 | a function type with function parameter<br>pack was not a dependent type | it is |
| cwg-2936 | C++98 | the names of local classes of templated<br>functions were not part of the current instantiation | they are |

