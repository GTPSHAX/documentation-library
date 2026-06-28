---
title: Constant initialization
type: Language
source: https://en.cppreference.com/w/cpp/language/constant_initialization
---


# Constant initialization

Sets the initial values of the `static` variables to a compile-time constant.

## Explanation

''Constant initialization'' is performed in the following cases:
rev|until=c++11|
* Initializing a reference with  with a `constant expression`.
* Initializing an object of  with static storage duration with a constant expression.
rev|since=c++11|until=c++17|
* Initializing a reference with `static` or `thread` storage duration, where all following conditions are satisfied:
:* Each `full-expression` (including implicit conversions) that appears in the initializer is a `constant expression`.
:* The reference is bound to one of the following entities:
::* an lvalue designating an object with static storage duration
::* a temporary object
::* a `subobject` of a temporary object
::* a function
* Initializing an object with static or thread storage duration, and one of the following conditions is satisfied:
:* If the object is initialized by a constructor call, where the initialization full-expression is a constant expression, except that it may also invoke ``constexpr` constructors` for the object and its subobjects (even if those objects are of non-`literal` class types).
:* Otherwise, either the object is `value-initialized` or every full-expression that appears in its initializer is a constant expression.
rev|since=c++17|until=c++20|
* Initializing a variable or temporary object with `static` or `thread` storage duration by  an initializer whose `full-expression` is a `constant expression`, except that if the entity being intialized is an object, such an initializer may also invoke ``constexpr` constructors` for the object and its  (even if those objects are of non-`literal` class types).
rev|since=c++20|
* A variable<sup>(until C++26)</sup>  or temporary object with `static` or `thread` storage duration is `constant-initialized`.
The effects of constant initialization are the same as the effects of the corresponding initialization, except that it is guaranteed that it is complete before any other initialization of a static<sup>(since C++11)</sup>  or thread-local object begins.

## Notes

The compiler is permitted to initialize other static<sup>(since C++11)</sup>  and thread-local objects using constant initialization, if it can guarantee that the value would be the same as if the standard order of initialization was followed.
Constant initialization usually happens when the program loads into memory, as part of initializing the program's runtime environment.

## Example


### Example

```cpp
#include <iostream>
#include <array>

struct S
{
    static const int c;
};

const int d = 10 * S::c; // not a constant expression: S::c has no preceding
                         // initializer, this initialization happens after const
const int S::c = 5;      // constant initialization, guaranteed to happen first

int main()
{
    std::cout << "d = " << d << '\n';
    std::array<int, S::c> a1; // OK: S::c is a constant expression
//  std::array<int, d> a2;    // error: d is not a constant expression
}
```


**Output:**
```
d = 50
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-441 | C++98 | references could not be constant initialized | made constant initializable |
| cwg-1489 | C++11 | it was unclear whether value-initializing<br>an object can be a constant initialization | it can |
| cwg-1747 | C++11 | binding a reference to a function could not be constant initialization | it can |
| cwg-1834 | C++11 | binding a reference to an xvalue could not be constant initialization | it can |


## See also

* `constinit`
* `constexpr`
* `constructor`
* `converting constructor`
* `copy constructor`
* `default constructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `copy initialization`
** `default initialization`
** `direct initialization`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move constructor`
