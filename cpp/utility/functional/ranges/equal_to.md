---
title: std::ranges::equal_to
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ranges/equal_to
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++20|
struct equal_to;
```

Function object for performing comparisons. The parameter types of the function call operator (but not the return type) are deduced from the arguments.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|1=operator()|2=
ddcl|
template< class T, class U >
constexpr bool operator()( T&& t, U&& u ) const;
Given the expression `1=std::forward<T>(t) == std::forward<U>(u)` as `expr`:
* If `expr` results in a call to built-in `1=operator==` comparing pointers, given the  of `t` and `u` as `P`:
:* For the two converted pointers (of type `P`), if one pointer precedes the other in the implementation-defined strict total order over pointers, returns `false`, otherwise returns `true`.
:* If the conversion sequence from `T` to `P` or the conversion sequence from `U` to `P` is not equality-preserving, the behavior is undefined.
* Otherwise:
:* Returns the result of `expr`.
:* If `std::equality_comparable_with<T, U>` is not modeled, the behavior is undefined.
.

## Notes

Compared to `std::equal_to`, `std::ranges::equal_to` additionally requires `1=!=` to be valid, and that both argument types are required to be (homogeneously) comparable with themselves (via the  constraint).

## Example


## See also


| cpp/utility/functional/dsc equal_to | (see dedicated page) |

