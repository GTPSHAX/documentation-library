---
title: SFINAE
type: Language
source: https://en.cppreference.com/w/cpp/language/sfinae
---


# SFINAE

"Substitution Failure Is Not An Error"
This rule applies during overload resolution of function templates: When `substituting` the explicitly specified or `deduced type` for the template parameter fails, the specialization is discarded from the `overload set` instead of causing a compile error.
This feature is used in template metaprogramming.

## Explanation

Function template parameters are substituted (replaced by template arguments) twice:
* explicitly specified template arguments are substituted before template argument deduction
* deduced arguments and the arguments obtained from the defaults are substituted after template argument deduction
Substitution occurs in
* all types used in the function type (which includes return type and the types of all parameters)
* all types used in the template parameter declarations
* all types used in the template argument list of a partial specialization
rrev|since=c++11|
* all expressions used in the function type
* all expressions used in a template parameter declaration
* all expressions used in the template argument list of a partial specialization
rrev|since=c++20|
* all expressions used in the explicit specifier
A ''substitution failure'' is any situation when the type or expression above would be ill-formed (with a required diagnostic), if written using the substituted arguments.
Only the failures in the types and expressions in the ''immediate context'' of the function type or its template parameter types <sup>(since C++20)</sup> or its explicit specifier are SFINAE errors. If the evaluation of a substituted type/expression causes a side-effect such as instantiation of some template specialization, generation of an implicitly-defined member function, etc, errors in those side-effects are treated as hard errors. <sup>(since C++20)</sup> A `lambda expression is not considered part of the immediate context.`
Substitution proceeds in lexical order and stops when a failure is encountered.
rrev|since=c++11|
If there are multiple declarations with different lexical orders (e.g. a function template declared with trailing return type, to be substituted after a parameter, and redeclared with ordinary return type that would be substituted before the parameter), and that would cause template instantiations to occur in a different order or not at all, then the program is ill-formed; no diagnostic required.

```cpp
template<typename A>
struct B { using type = typename A::type; };

template<
    class T,
    class U = typename T::type,    // SFINAE failure if T has no member type
    class V = typename B<T>::type> // hard error if B has no member type
                                   // (guaranteed to not occur via CWG 1227 because
                                   // substitution into the default template argument
                                   // of U would fail first)
void foo (int);

template<class T>
typename T::type h(typename B<T>::type);

template<class T>
auto h(typename B<T>::type) -> typename T::type; // redeclaration

template<class T>
void h(...) {}

using R = decltype(h<int>(0));     // ill-formed, no diagnostic required
```


### Type SFINAE

The following type errors are SFINAE errors:
rrev|since=c++11|
* attempting to instantiate a pack expansion containing multiple packs of different lengths
* attempting to create an array of void, array of reference, array of function, array of negative size, array of non-integral size, or array of size zero:

```cpp
template<int I>
void div(char(*)[I % 2 == 0] = nullptr)
{
    // this overload is selected when I is even
}

template<int I>
void div(char(*)[I % 2 == 1] = nullptr)
{
    // this overload is selected when I is odd
}
```

* attempting to use a type on the left of a scope resolution operator **`::`** and it is not a class or enumeration:

```cpp
template<class T>
int f(typename T::B*);

template<class T>
int f(T);

int i = f<int>(0); // uses second overload
```

* attempting to use a member of a type, where
:* the type does not contain the specified member
:* the specified member is not a type where a type is required
:* the specified member is not a template where a template is required
:* the specified member is not a non-type where a non-type is required

```cpp
template<int I>
struct X {};

template<template<class T> class>
struct Z {};

template<class T>
void f(typename T::Y*) {}

template<class T>
void g(X<T::N>*) {}

template<class T>
void h(Z<T::template TT>*) {}

struct A {};
struct B { int Y; };
struct C { typedef int N; };
struct D { typedef int TT; };
struct B1 { typedef int Y; };
struct C1 { static const int N = 0; };
struct D1
{ 
    template<typename T>
    struct TT {}; 
};

int main()
{
    // Deduction fails in each of these cases:
    f<A>(0); // A does not contain a member Y
    f<B>(0); // The Y member of B is not a type
    g<C>(0); // The N member of C is not a non-type
    h<D>(0); // The TT member of D is not a template

    // Deduction succeeds in each of these cases:
    f<B1>(0); 
    g<C1>(0); 
    h<D1>(0);
}
// todo: needs to demonstrate overload resolution, not just failure
```

* attempting to create a pointer to reference
* attempting to create a reference to void
* attempting to create pointer to member of T, where T is not a class type:

```cpp
template<typename T>
class is_class
{
    typedef char yes[1];
    typedef char no[2];

    template<typename C>
    static yes& test(int C::*); // selected if C is a class type

    template<typename C>
    static no& test(...);       // selected otherwise
public:
    static bool const value = sizeof(test<T>(nullptr)) == sizeof(yes);
};
```

* attempting to give an invalid type to a non-type template parameter:

```cpp
template<class T, T>
struct S {};

template<class T>
int f(S<T, T()>*);

struct X {};
int i0 = f<X>(0);
// todo: needs to demonstrate overload resolution, not just failure
```

* attempting to perform an invalid conversion in
:* in a template argument expression
:* in an expression used in function declaration:

```cpp
template<class T, T*> int f(int);
int i2 = f<int, 1>(0); // can’t conv 1 to int*
// todo: needs to demonstrate overload resolution, not just failure
```

* attempting to create a function type with a parameter of type void
* attempting to create a function type which returns an array type or a function type
<!-- removed by p0929r2 adopted as a DR in Jax-2018 rrev |since=c++11|
* attempting to create a function type with a parameter or return type that is an `abstract class`
-->

### Expression SFINAE

rev|until=c++11|
Only constant expressions that are used in types (such as array bounds) were required to be treated as SFINAE (and not hard errors) before C++11.
rev|since=c++11|
The following expression errors are SFINAE errors
* Ill-formed expression used in a template parameter type
* Ill-formed expression used in the function type:

```cpp
struct X {};
struct Y { Y(X){} }; // X is convertible to Y

template<class T>
auto f(T t1, T t2) -> decltype(t1 + t2); // overload #1

X f(Y, Y);                               // overload #2

X x1, x2;
X x3 = f(x1, x2); // deduction fails on #1 (expression x1 + x2 is ill-formed)
                  // only #2 is in the overload set, and is called
```


### SFINAE in partial specializations

Deduction and substitution also occur while determining whether a specialization of a class <sup>(since C++14)</sup> or variable template is generated by some `partial specialization` or the primary template. A substitution failure is not treated as a hard-error during such determination, but makes the corresponding partial specialization declaration ignored instead, as if in the overload resolution involving function templates.

```cpp
// primary template handles non-referenceable types:
template<class T, class = void>
struct reference_traits
{
    using add_lref = T;
    using add_rref = T;
};

// specialization recognizes referenceable types:
template<class T>
struct reference_traits<T, std::void_t<T&>>
{
    using add_lref = T&;
    using add_rref = T&&;
};

template<class T>
using add_lvalue_reference_t = typename reference_traits<T>::add_lref;

template<class T>
using add_rvalue_reference_t = typename reference_traits<T>::add_rref;
```


## Library support

rrev|since=c++11|
The standard library component `std::enable_if` allows for creating a substitution failure in order to enable or disable particular overloads based on a condition evaluated at compile time.
In addition, many  must be implemented with SFINAE if appropriate compiler extensions are unavailable.
rrev|since=c++17|
The standard library component `std::void_t` is another utility metafunction that simplifies partial specialization SFINAE applications.

## Alternatives

Where applicable, tag dispatch<sup>(since C++17)</sup> , `if constexpr`<sup>(since C++20)</sup> , and `concepts ` are usually preferred over use of SFINAE.
<sup>(since C++11)</sup> `static_assert is usually preferred over SFINAE if only a conditional compile time error is wanted.`

## Examples


### Example

```cpp
#include <iostream>

// This overload is added to the set of overloads if C is
// a class or reference-to-class type and F is a pointer to member function of C
template<class C, class F>
auto test(C c, F f) -> decltype((void)(c.*f)(), void())
{
    std::cout << "(1) Class/class reference overload called\n";
}

// This overload is added to the set of overloads if C is a
// pointer-to-class type and F is a pointer to member function of C
template<class C, class F>
auto test(C c, F f) -> decltype((void)((c->*f)()), void())
{
    std::cout << "(2) Pointer overload called\n";
}

// This overload is always in the set of overloads: ellipsis
// parameter has the lowest ranking for overload resolution
void test(...)
{
    std::cout << "(3) Catch-all overload called\n";
}

int main()
{
    struct X { void f() {} };
    X x;
    X& rx = x;
    test(x, &X::f);  // (1)
    test(rx, &X::f); // (1), creates a copy of x
    test(&x, &X::f); // (2)
    test(42, 1337);  // (3)
}
```


**Output:**
```
(1) Class/class reference overload called
(1) Class/class reference overload called
(2) Pointer overload called
(3) Catch-all overload called
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-295 | c++98 | creating cv-qualified function type<br>could result in substitution failure | made not failure,<br>discarding cv-qualification |
| cwg-1227 | c++98 | the order of substitution was unspecified | same as the lexical order |
| cwg-2054 | c++98 | substitution in partial specializations was not correctly specified | specified |
| cwg-2322 | c++11 | declarations in different lexical orders would cause template<br>instantiations to occur in a different order or not at all | such case is ill-formed,<br>no diagnostic required |

