---
title: std::expected::or_else
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/or_else
---


```cpp
dcla|num=1|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) &;
dcla|num=2|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) const&;
dcla|num=3|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) &&;
dcla|num=4|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) const&&;
dcla|num=5|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) &;
dcla|num=6|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) const&;
dcla|num=7|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) &&;
dcla|num=8|since=c++23|
template< class F >
constexpr auto or_else( F&& f ) const&&;
```

If `*this` contains an unexpected value, invokes `f` with the unexpected value of `*this` as the argument and returns its result. Otherwise, returns a `std::expected` object that represents an expected value.
@1-4@ The expected value is initialized with the expected value  of `*this`.
Given type `G` as:
@1,2@ `std::remove_cvref_t<std::invoke_result_t<F, decltype(error())>>`
@3,4@ `std::remove_cvref_t<std::invoke_result_t<F, decltype(std::move(error()))>>`
@5,6@ `std::remove_cvref_t<std::invoke_result_t<F, decltype(error())>>`
@7,8@ `std::remove_cvref_t<std::invoke_result_t<F, decltype(std::move(error()))>>`
If `G` is not a specialization of `std::expected`, or `std::is_same_v<G::value_type, T>` is `false`, the program is ill-formed.
@1,2@ .
@3,4@ .

## Parameters


### Parameters

- `f` - a suitable function or *Callable* object that returns a `std::expected`

## Return value


| rowspan=2 | Overload |
| colspan=2 | Value of rlpf | operator bool | has_value |
| - |
| style="font-weight: normal;" | c | true |
| style="font-weight: normal;" | c | false |
| - |
| style="text-align: center;" | vl | 1,2 |
| box | c/core | G(std::in_place,tti | valc/core | ) |
| c | std::invoke(std::forward<F>(f), error()) |
| - |
| style="text-align: center;" | vl | 3,4 |
| box | c/core | G(std::in_place, std::move(tti | valc/core | )) |
| c | std::invoke(std::forward<F>(f), std::move(error())) |
| - |
| style="text-align: center;" | vl | 5,6 |
| rowspan=2 | c | G() |
| c | std::invoke(std::forward<F>(f), error()) |
| - |
| style="text-align: center;" | vl | 7,8 |
| c | std::invoke(std::forward<F>(f), std::move(error())) |


## Notes


## Example


## See also


| cpp/utility/expected/dsc transform_error | (see dedicated page) |

