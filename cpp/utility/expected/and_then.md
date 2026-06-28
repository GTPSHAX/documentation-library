---
title: std::expected::and_then
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/and_then
---


```cpp
dcla|num=1|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) &;
dcl|num=2|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) const&;
dcla|num=3|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) &&;
dcl|num=4|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) const&&;
dcla|num=5|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) &;
dcl|num=6|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) const&;
dcla|num=7|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) &&;
dcl|num=8|since=c++23|
template< class F >
constexpr auto and_then( F&& f ) const&&;
```

If `*this` represents an expected value, invokes `f` and returns its result. Otherwise, returns a `std::expected` object that contains an unexpected value, which is initialized with the unexpected value of `*this`.
@1-4@ `f` is invoked with the expected value  as the argument.
@5-8@ `f` is invoked without any argument.
Given type `U` as:
@1,2@ `std::remove_cvref_t<std::invoke_result_t<F, decltype((``))>>`
@3,4@ `std::remove_cvref_t<std::invoke_result_t<F, decltype(std::move(``))>>`
@5-8@ `std::remove_cvref_t<std::invoke_result_t<F>>`
If `U` is not a specialization of `std::expected`, or `std::is_same_v<U::error_type, E>` is `false`, the program is ill-formed.
@1,2@ .
@3,4@ .
@5,6@ .
@7,8@ .

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
| box | c/core | std::invoke(std::forward<F>(f),tti | valc/core | ) |
| c | U(std::unexpect, error()) |
| - |
| style="text-align: center;" | vl | 3,4 |
| box | c/core | std::invoke(std::forward<F>(f),std::move(tti | valc/core | )) |
| c | U(std::unexpect, std::move(error())) |
| - |
| style="text-align: center;" | vl | 5,6 |
| rowspan=2 | c | std::invoke(std::forward<F>(f)) |
| c | U(std::unexpect, error()) |
| - |
| style="text-align: center;" | vl | 7,8 |
| c | U(std::unexpect, std::move(error())) |


## Notes


## Example


## See also


| cpp/utility/expected/dsc unexpect_t | (see dedicated page) |
| cpp/utility/expected/dsc transform | (see dedicated page) |

