---
title: std::ranges::less
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ranges/less
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++20|
struct less;
```

Function object for performing comparisons. Deduces the parameter types of the function call operator from the arguments (but not the return type).

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|1=operator()|2=
ddcl|
template< class T, class U >
constexpr bool operator()( T&& t, U&& u ) const;
Given the expression `std::forward<T>(t) < std::forward<U>(u)` as `expr`:
* If `expr` results in a call to built-in `operator<` comparing pointers, given the  of `t` and `u` as `P`:
:* If the converted `t` precedes the converted `u` (both are of type `P`) in the implementation-defined strict total order over pointers, returns `true`, otherwise returns `false`.
:* If the conversion sequence from `T` to `P` or the conversion sequence from `U` to `P` is not equality-preserving, the behavior is undefined.
* Otherwise:
:* Returns the result of `expr`.
:* If `std::totally_ordered_with<T, U>` is not modeled, the behavior is undefined.
.
If there exists an expression `expr1` of type `T` and an expression `expr2` of `U`, such that the comparison results of `expr1` and `expr2` violate [Total order#Strict and non-strict total orders|strict total ordering](https://en.wikipedia.org/wiki/Total order#Strict and non-strict total orders|strict total ordering) (rules are defined below), the behavior is undefined.
The comparison results of `expr1` and `expr2` follow strict total ordering only if '''exactly one''' of the following expressions is `true`:
* }
* }
* }

## Notes

Unlike `std::less`, `std::ranges::less` requires all six comparison operators `<`, `1=<=`, `>`, `1=>=`, `1===` and `1=!=` to be valid (via the  constraint).

## Example


## See also


| cpp/utility/functional/dsc less | (see dedicated page) |

