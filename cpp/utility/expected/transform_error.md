---
title: std::expected::transform_error
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/transform_error
---


```cpp
dcla|num=1|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) &;
dcla|num=2|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) const&;
dcla|num=3|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) &&;
dcla|num=4|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) const&&;
dcla|num=5|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) &;
dcla|num=6|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) const&;
dcla|num=7|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) &&;
dcla|num=8|since=c++23|
template< class F >
constexpr auto transform_error( F&& f ) const&&;
```

If `*this` contains an unexpected value, invokes `f` with the unexpected value of `*this` as the argument and returns a `std::expected` object that contains an unexpected value, which is initialized with the result of `f`. Otherwise, returns a `std::expected` object that represents an expected value.
@1-4@ The expected value is initialized with the expected value  of `*this`.
Given type `G` as:
@1,2@ `std::remove_cv_t<std::invoke_result_t<F, decltype(error())>>`
@3,4@ `std::remove_cv_t<std::invoke_result_t<F, decltype(std::move(error()))>>`
@5,6@ `std::remove_cv_t<std::invoke_result_t<F, decltype(error())>>`
@7,8@ `std::remove_cv_t<std::invoke_result_t<F, decltype(std::move(error()))>>`
If any of the following conditions is satisfied, the program is ill-formed:
* `G` is not a valid template argument for `std::unexpected`.
* The following corresponding declaration is ill-formed:
:@1,2@ `G g(std::invoke(std::forward<F>(f), error()));`
:@3,4@ `G g(std::invoke(std::forward<F>(f), std::move(error()));`
:@5,6@ `G g(std::invoke(std::forward<F>(f), error()));`
:@7,8@ `G g(std::invoke(std::forward<F>(f), std::move(error()));`
@1,2@ .
@3,4@ .

## Parameters


### Parameters

- `f` - a suitable function or *Callable* object whose call signature returns a non-reference type

## Return value

Given expression `expr` as:
@1,2@ `std::invoke(std::forward<F>(f), error())`
@3,4@ `std::invoke(std::forward<F>(f), std::move(error()))`
@5,6@ `std::invoke(std::forward<F>(f), error())`
@7,8@ `std::invoke(std::forward<F>(f), std::move(error()))`
The return values are defined as follows:


| rowspan=2 | Overload |
| colspan=2 | Value of rlpf | operator bool | has_value |
| - |
| style="font-weight: normal;" | c | true |
| style="font-weight: normal;" | c | false |
| - |
| style="text-align: center;" | vl | 1,2 |
| box | c/core | std::expected<T, G>(std::in_place,tti | valc/core | ) |
| rowspan=4 | c multi | std::expected<T, G> | (std::unexpect, expr) |
| - |
| style="text-align: center;" | vl | 3,4 |
| box | c/core | std::expected<T, G>(std::in_place, std::move(tti | valc/core | )) |
| - |
| style="text-align: center;" | vl | 5,6 |
| rowspan=2 | c | std::expected<T, G>() |
| - |
| style="text-align: center;" | vl | 7,8 |


## Notes


## Example


## See also


| cpp/utility/expected/dsc or_else | (see dedicated page) |
| cpp/utility/expected/dsc transform | (see dedicated page) |

