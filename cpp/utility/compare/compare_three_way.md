---
title: std::compare_three_way
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/compare_three_way
---


```cpp
**Header:** `<`compare`>`
**Header:** `<`functional`>`
dcl|since=c++20|
struct compare_three_way;
```

Function object for performing comparisons. Deduces the parameter types and the return type of the function call operator.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|1=operator()|2=
ddcl|
template< class T, class U >
constexpr auto operator()( T&& t, U&& u ) const;
Given the expression `1=std::forward<T>(t) <=> std::forward<U>(u)` as `expr`:
* If `expr` results in a call to built-in `1=operator<=>` comparing pointers, given the  of `t` and `u` as `P`:
:* Compares the two converted pointers (of type `P`) in the implementation-defined strict total order over pointers:
::* If `t` precedes `u`, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::less`.
::* If `u` precedes `t`, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::greater`.
::* Otherwise, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::equal`.
:* If the conversion sequence from `T` to `P` or the conversion sequence from `U` to `P` is not equality-preserving, the behavior is undefined.
* Otherwise:
:* Returns the result of `expr`.
:* If `std::three_way_comparable_with<T, U>` is not modeled, the behavior is undefined.
.

## Example


### Example


**Output:**
```
greater
greater
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3530 | C++20 | syntactic checks were relaxed while comparing pointers | only semantic requirements are relaxed |


## See also


| cpp/utility/functional/ranges/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less_equal | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater_equal | (see dedicated page) |

