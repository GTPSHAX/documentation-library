---
title: Move constructors
type: Language
source: https://en.cppreference.com/w/cpp/language/move_constructor
---


# Move constructors

A move constructor is a `constructor` which can be called with an argument of the same class type and copies the content of the argument, possibly mutating the argument.

## Syntax


**Syntax:**

- `**`(`**parameter-list**`);`**`
- `**`(`**parameter-list**`)`** *function-body*`
- `**`(`**single-parameter-list**`) = default;`**`
- `**`(`**parameter-list**`) = delete;`**`
- `**`::`**class-name**`(`**parameter-list**`)`** *function-body*`
- `**`::`**class-name**`(`**single-parameter-list**`) = default;`**`

### Parameters

- `{{spar` - class-name|the class whose move constructor is being declared
- `{{spar` - parameter-list|a non-empty  satisfying all following conditions:
- `{{spar` - single-parameter-list|a  of only one parameter, which is of type `T&&`, `const T&&`, `volatile T&&` or `const volatile T&&` and does not have a default argument
- `{{spar` - function-body|the `function body` of the move constructor

## Explanation

1. Declaration of a move constructor inside of class definition.
@2-4@ Definition of a move constructor inside of class definition.
:@3@ The move constructor is explicitly-defaulted.
:@4@ The move constructor is deleted.
@5,6@ Definition of a move constructor outside of class definition (the class must contain a declaration ).
:@6@ The move constructor is explicitly-defaulted.

```cpp
struct X
{
    X(X&& other); // move constructor
//  X(X other);   // Error: incorrect parameter type
};

union Y
{
    Y(Y&& other, int num = 1); // move constructor with multiple parameters
//  Y(Y&& other, int num);     // Error: `num` has no default argument
};
```

The move constructor is typically called when an object is `initialized` (by `direct-initialization` or `copy-initialization`) from <sup>(until C++17)</sup> <sup>(since C++17)</sup> xvalue of the same type, including
* initialization: `1=T a = std::move(b);` or `1=T a(std::move(b));`, where `b` is of type `T`;
* function argument passing: `f(std::move(a));`, where `a` is of type `T` and `f` is `void f(T t)`;
* function return: `return a;` inside a function such as `T f()`, where `a` is of type `T` which has a move constructor.
When the initializer is a prvalue, the move constructor call is <sup>(until C++17)</sup> often optimized out<sup>(since C++17)</sup> never made, see `copy elision`.
Move constructors typically transfer the resources held by the argument (e.g. pointers to dynamically-allocated objects, file descriptors, TCP sockets, thread handles, etc.) rather than make copies of them, and leave the argument in some valid but otherwise indeterminate state. Since move constructor doesn’t change the lifetime of the argument, the destructor will typically be called on the argument at a later point. For example, moving from a `std::string` or from a `std::vector` may result in the argument being left empty. For some types, such as `std::unique_ptr`, the moved-from state is fully specified.

## Implicitly-declared move constructor

If no user-defined move constructors are provided for a class type, and all of the following is true:
* there are no user-declared `copy constructor`s;
* there are no user-declared `copy assignment operator`s;
* there are no user-declared `move assignment operator`s;
* there is no user-declared `destructor`.
Then the compiler will declare a move constructor as a non-`explicit` `inline public` member of its class with the signature `T::T(T&&)`.
A class can have multiple move constructors, e.g. both `T::T(const T&&)` and `T::T(T&&)`. If some user-defined move constructors are present, the user may still force the generation of the implicitly declared move constructor with the keyword `default`.
The implicitly-declared (or defaulted on its first declaration) move constructor has an exception specification as described in <sup>(until C++17)</sup> `dynamic exception specification`<sup>(since C++17)</sup> `noexcept specification`.

## Implicitly-defined move constructor

If the implicitly-declared move constructor is neither deleted nor trivial, it is defined (that is, a function body is generated and compiled) by the compiler if  or `needed for constant evaluation`. For union types, the implicitly-defined move constructor copies the object representation (as by `std::memmove`). For non-union class types, the move constructor performs full member-wise move of the object's direct base subobjects and member subobjects, in their initialization order, using direct initialization with an  argument. For each non-static data member of a reference type, the move constructor binds the reference to the same object or function to which the source reference is bound.
If this satisfies the requirements of a <sup>(until C++23)</sup> ``constexpr` constructor`<sup>(since C++23)</sup> ``constexpr` function`, the generated move constructor is `constexpr`.

## Deleted move constructor

The implicitly-declared or explicitly-defaulted move constructor for class `T` is defined as deleted if `T` has a  of class type `M` (or possibly multi-dimensional array thereof) such that
* `M` has a destructor that is deleted or inaccessible from the copy constructor, or
* the overload resolution as applied to find `M`'s move constructor
:* does not result in a usable candidate, or
:* in the case of the subobject being a `variant member`, selects a non-trivial function.
Such a constructor is ignored by `overload resolution` (otherwise it would prevent copy-initialization from rvalue).

## Trivial move constructor

The move constructor for class `T` is trivial if all of the following is true:
* it is not user-provided (meaning, it is implicitly-defined or defaulted);
* `T` has no virtual member functions;
* `T` has no virtual base classes;
* the move constructor selected for every direct base of `T` is trivial;
* the move constructor selected for every non-static class type (or array of class type) member of `T` is trivial.
A trivial move constructor is a constructor that performs the same action as the trivial copy constructor, that is, makes a copy of the object representation as if by `std::memmove`. All data types compatible with the C language are trivially movable.

## Eligible move constructor

Triviality of eligible move constructors determines whether the class is an implicit-lifetime type, and whether the class is a trivially copyable type.

## Notes

To make the `strong exception guarantee` possible, user-defined move constructors should not throw exceptions. For example, `std::vector` relies on `std::move_if_noexcept` to choose between move and copy when the elements need to be relocated.
If both copy and move constructors are provided and no other constructors are viable, overload resolution selects the move constructor if the argument is an  of the same type (an  such as the result of `std::move`<sup>(until C++17)</sup>  or a ), and selects the copy constructor if the argument is an  (named object or a function/operator returning lvalue reference). If only the copy constructor is provided, all argument categories select it (as long as it takes a reference to const, since rvalues can bind to const references), which makes copying the fallback for moving, when moving is unavailable.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>

struct A
{
    std::string s;
    int k;

    A() : s("test"), k(-1) {}
    A(const A& o) : s(o.s), k(o.k) { std::cout << "move failed!\n"; }
    A(A&& o) noexcept :
        s(std::move(o.s)),       // explicit move of a member of class type
        k(std::exchange(o.k, 0)) // explicit move of a member of non-class type
    {}
};

A f(A a)
{
    return a;
}

struct B : A
{
    std::string s2;
    int n;
    // implicit move constructor B::(B&&)
    // calls A's move constructor
    // calls s2's move constructor
    // and makes a bitwise copy of n
};

struct C : B
{
    ~C() {} // destructor prevents implicit move constructor C::(C&&)
};

struct D : B
{
    D() {}
    ~D() {}           // destructor would prevent implicit move constructor D::(D&&)
    D(D&&) = default; // forces a move constructor anyway
};

int main()
{
    std::cout << "Trying to move A\n";
    A a1 = f(A()); // return by value move-constructs the target
                   // from the function parameter

    std::cout << "Before move, a1.s = " << std::quoted(a1.s)
        << " a1.k = " << a1.k << '\n';

    A a2 = std::move(a1); // move-constructs from xvalue
    std::cout << "After move, a1.s = " << std::quoted(a1.s)
        << " a1.k = " << a1.k << '\n';


    std::cout << "\nTrying to move B\n";
    B b1;

    std::cout << "Before move, b1.s = " << std::quoted(b1.s) << "\n";

    B b2 = std::move(b1); // calls implicit move constructor
    std::cout << "After move, b1.s = " << std::quoted(b1.s) << "\n";


    std::cout << "\nTrying to move C\n";
    C c1;
    C c2 = std::move(c1); // calls copy constructor

    std::cout << "\nTrying to move D\n";
    D d1;
    D d2 = std::move(d1);
}
```


**Output:**
```
Trying to move A
Before move, a1.s = "test" a1.k = -1
After move, a1.s = "" a1.k = 0

Trying to move B
Before move, b1.s = "test"
After move, b1.s = ""

Trying to move C
move failed!

Trying to move D
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1353 | C++11 | the conditions where defaulted move constructors are<br>defined as deleted did not consider multi-dimensional array types | consider these types |
| cwg-1402 | C++11 | a defaulted move constructor that would call<br>a non-trivial copy constructor was defined as<br>deleted; a defaulted move constructor that is<br>deleted still participated in overload resolution | allows call to such copy<br>constructor; made ignored<br>in overload resolution |
| cwg-1491 | C++11 | a defaulted move constructor of a class with a non-static data<br>member of rvalue reference type was defined as deleted | not deleted in this case |
| cwg-2595 | C++20 | a move constructor was not eligible if there is<br>another move constructor which is more constrained<br>but does not satisfy its associated constraints | it can be eligible in this case |


## See also

* `converting constructor`
* `copy assignment`
* `copy constructor`
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
* `new`
