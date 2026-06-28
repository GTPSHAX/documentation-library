---
title: deduction guides for std::function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/deduction_guides
---


# deduction guides for tt|std::function


```cpp
**Header:** `<`functional`>`
dcl | num=1 | since=c++17 |
template< class R, class... ArgTypes >
function( R(*)(ArgTypes...) ) -> function<R(ArgTypes...)>;
dcl | num=2 | since=c++17 |
template< class F >
function( F ) -> function</*see below*/>;
dcl | num=3 | since=c++23 |
template< class F >
function( F ) -> function</*see below*/>;
dcl | num=4 | since=c++23 |
template< class F >
function( F ) -> function</*see below*/>;
```

1. This deduction guide is provided for `std::function` to allow deduction from functions.
2. . The deduced type is `std::function<R(A...)>`.
3. . The deduced type is `std::function<R(A...)>`.
4. . The deduced type is `std::function<R(A...)>`.

## Notes

These deduction guides do not allow deduction from a function with ellipsis parameter, and the `...` in the types is always treated as a pack expansion.
The type deduced by these deduction guides may change in a later standard revision (in particular, this might happen if `noexcept` support is added to `std::function` in a later standard).

## Example


## Defect reports

