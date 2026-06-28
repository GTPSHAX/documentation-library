---
title: std::convertible_to
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/convertible_to
---

ddcl|header=concepts|since=c++20|1=
template< class From, class To >
concept convertible_to =
std::is_convertible_v<From, To> &&
requires {
static_cast<To>(std::declval<From>());
};
The concept `convertible_to<From, To>` specifies that an expression of the same type and value category as those of `std::declval<From>()` can be implicitly and explicitly converted to the type `To`, and the two forms of conversion produce equal results.

## Semantic requirements

`convertible_to<From, To>` is modeled only if, given a function `fun` of type `std::add_rvalue_reference_t<From>()` such that the expression `fun()` is equality-preserving,
* Either
** `To` is neither an object type nor a reference-to-object type, or
** `static_cast<To>(fun())` is equal to }, and
* One of the following is true:
** `std::add_rvalue_reference_t<From>` is not a reference-to-object type, or
** `std::add_rvalue_reference_t<From>` is an rvalue reference to a non-const-qualified type, and the resulting state of the object referenced by `fun()` is valid but unspecified after either expression above; or
** the object referred to by `fun()` is not modified by either expression above.

## References


## See also


| cpp/types/dsc is_convertible | (see dedicated page) |

