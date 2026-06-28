---
title: Copy constructors
type: Language
source: https://en.cppreference.com/w/cpp/language/copy_constructor
---


# Copy constructors

A copy constructor is a `constructor` which can be called with an argument of the same class type and copies the content of the argument without mutating the argument.

## Syntax


**Syntax:**

- `**`(`**parameter-list**`);`**`
- `**`(`**parameter-list**`)`** *function-body*`
- `**`(`**single-parameter-list**`) = default;`**|notes=<sup>(C++11)</sup>`
- `**`(`**parameter-list**`) = delete;`**|notes=<sup>(C++11)</sup>`
- `**`::`**class-name**`(`**parameter-list**`)`** *function-body*`
- `**`::`**class-name**`(`**single-parameter-list**`) = default;`**|notes=<sup>(C++11)</sup>`

### Parameters

- `{{spar` - class-name|the class whose copy constructor is being declared
- `{{spar` - parameter-list|a non-empty `parameter list` satisfying all following conditions:
- `{{spar` - single-parameter-list|a `parameter list` of only one parameter, which is of type `T&`, `const T&`, `volatile T&` or `const volatile T&` and does not have a default argument
- `{{spar` - function-body|the `function body` of the copy constructor

## Explanation

1. Declaration of a copy constructor inside of class definition.
@2-4@ Definition of a copy constructor inside of class definition.
:@3@ The copy constructor is explicitly-defaulted.
:@4@ The copy constructor is deleted.
@5,6@ Definition of a copy constructor outside of class definition (the class must contain a declaration ).
:@6@ The copy constructor is explicitly-defaulted.

```cpp
struct X
{
    X(X& other); // copy constructor
//  X(X other);  // Error: incorrect parameter type
};

union Y
{
    Y(Y& other, int num = 1); // copy constructor with multiple parameters
//  Y(Y& other, int num);     // Error: `num` has no default argument
};
```

The copy constructor is called whenever an object is `initialized` (by `direct-initialization` or `copy-initialization`) from another object of the same type (unless `overload resolution` selects a better match or the call is `elided`), which includes
* initialization: `1=T a = b;` or `1=T a(b);`, where `b` is of type `T`;
* function argument passing: `f(a);`, where `a` is of type `T` and `f` is `void f(T t)`;
* function return: `return a;` inside a function such as `T f()`, where `a` is of type `T`, which has no `move constructor`.

## Implicitly-declared copy constructor

If no user-defined copy constructors are provided for a class type, the compiler will always declare a copy constructor as a non-`explicit` `inline public` member of its class. This implicitly-declared copy constructor has the form `T::T(const T&)` if all of the following are true:
* each direct and virtual base `B` of `T` has a copy constructor whose parameters are of type `const B&` or `const volatile B&`;
* each non-static data member `M` of `T` of class type or array of class type has a copy constructor whose parameters are of type `const M&` or `const volatile M&`.
Otherwise, the implicitly-declared copy constructor is `T::T(T&)`.
Due to these rules, the implicitly-declared copy constructor cannot bind to a `volatile` lvalue argument.
A class can have multiple copy constructors, e.g. both `T::T(const T&)` and `T::T(T&)`.
rrev|since=c++11|
Even if some user-defined copy constructors are present, the user may still force the implicit copy constructor declaration with the keyword `default`.
The implicitly-declared (or defaulted on its first declaration) copy constructor has an exception specification as described in <sup>(until C++17)</sup> `dynamic exception specification`<sup>(since C++17)</sup> `noexcept specification`.

## Implicitly-defined copy constructor

If the implicitly-declared copy constructor is not deleted, it is defined (that is, a function body is generated and compiled) by the compiler if `odr-used`<sup>(since C++11)</sup>  or `needed for constant evaluation`. For union types, the implicitly-defined copy constructor copies the object representation (as by `std::memmove`). For non-union class types, the constructor performs full member-wise copy of the object's direct base subobjects and member subobjects, in their initialization order, using direct initialization. For each non-static data member of a reference type, the copy constructor binds the reference to the same object or function to which the source reference is bound.
rrev|since=c++11|
If this satisfies the requirements of a <sup>(until C++23)</sup> `constexpr constructor`<sup>(since C++23)</sup> `constexpr function`, the generated copy constructor is `constexpr`.
The generation of the implicitly-defined copy constructor is deprecated if `T` has a user-defined destructor or user-defined copy assignment operator.

## Deleted copy constructor

The implicitly-declared<sup>(since C++11)</sup>  or explicitly-defaulted copy constructor for class `T` is <sup>(until C++11)</sup> undefined<sup>(since C++11)</sup> defined as deleted if any of the following conditions is satisfied:
rrev|since=c++11|
* `T` has a non-static data member of rvalue reference type.
* `T` has a `potentially constructed subobject` of class type `M` (or possibly multi-dimensional array thereof) such that
:* `M` has a destructor that is<sup>(since C++11)</sup>  deleted or inaccessible from the copy constructor, or
:* the overload resolution as applied to find `M`'s copy constructor
::* does not result in a usable candidate, or
::* in the case of the subobject being a `variant member`, selects a non-trivial function.
rrev|since=c++11|
The implicitly-declared copy constructor for class `T` is defined as deleted if `T` declares a `move constructor` or `move assignment operator`.

## Trivial copy constructor

The copy constructor for class `T` is trivial if all of the following are true:
* it is not user-provided (that is, it is implicitly-defined or defaulted);
* `T` has no virtual member functions;
* `T` has no virtual base classes;
* the copy constructor selected for every direct base of `T` is trivial;
* the copy constructor selected for every non-static class type (or array of class type) member of `T` is trivial;
A trivial copy constructor for a non-union class effectively copies every scalar subobject (including, recursively, subobject of subobjects and so forth) of the argument and performs no other action. However, padding bytes need not be copied, and even the object representations of the copied subobjects need not be the same as long as their values are identical.
*TriviallyCopyable* objects can be copied by copying their object representations manually, e.g. with `std::memmove`. All data types compatible with the C language (POD types) are trivially copyable.

## Eligible copy constructor

Triviality of eligible copy constructors determines whether the class is an implicit-lifetime type, and whether the class is a trivially copyable type.

## Notes

In many situations, copy constructors are optimized out even if they would produce observable side-effects, see `copy elision`.

## Example


```cpp
code=
struct A
{
    int n;
    A(int n = 1) : n(n) {}
    A(const A& a) : n(a.n) {} // user-defined copy constructor
};

struct B : A
{
    // implicit default constructor B::B()
    // implicit copy constructor B::B(const B&)
};

struct C : B
{
    C() : B() {}
private:
    C(const C&); // non-copyable, C++98 style
};

int main()
{
    A a1(7);
    A a2(a1); // calls the copy constructor

    B b;
    B b2 = b;
    A a3 = b; // conversion to A& and copy constructor

    volatile A va(10);
    // A a4 = va; // compile error

    C c;
    // C c2 = c; // compile error
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1353 | C++98 | the conditions where implicitly-declared copy constructors<br>are undefined did not consider multi-dimensional array types | consider these types |
| cwg-2595 | C++20 | a copy constructor was not eligible if there is<br>another copy constructor which is more constrained<br>but does not satisfy its associated constraints | it can be eligible in this case |


## See also

* `converting constructor`
* `copy assignment`
* `copy elision`
* `default constructor`
* `destructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy initialization`
** `default initialization`
** `direct initialization`
** `initializer list`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move assignment`
* `move constructor`
* `new`
