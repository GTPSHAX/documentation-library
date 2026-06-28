---
title: std::expected::transform
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/transform
---


```cpp
dcl|num=1|since=c++23|
template< class F >
constexpr auto transform( F&& f ) &;
dcl|num=2|since=c++23|
template< class F >
constexpr auto transform( F&& f ) const&;
dcl|num=3|since=c++23|
template< class F >
constexpr auto transform( F&& f ) &&;
dcl|num=4|since=c++23|
template< class F >
constexpr auto transform( F&& f ) const&&;
```

If `*this` contains an expected value, invokes `f` and returns a `std::expected` object that contains its result; otherwise, returns a `std::expected` object that contains a copy of `error()`.
If `T` is not (possibly cv-qualified) `void`, the contained value (`operator*()`) is passed as an argument to `f`; otherwise `f` takes no argument.
Let `U` be:
* if `T` is not (possibly cv-qualified) `void`:
** for overloads , `std::remove_cv_t<std::invoke_result_t<F, decltype(operator*())>>`;
** for overloads , `std::remove_cv_t<std::invoke_result_t<F, decltype(std::move(operator*()))>>`;
* otherwise (`T` is possibly cv-qualified `void`), `std::remove_cv_t<std::invoke_result_t<F>>`.
`U` must be a valid value type for `std::expected`. A variable of type `U` must be constructible from the result of invocation (but does not need to be move-constructible). The return type is `std::expected<U, E>`.
@1-2@ .
@3-4@ .
Formally, these functions perform the following steps:
* If `*this` contains an expected value `val`:
:# Invoke `f` as if by
:#* `std::invoke(std::forward<F>(f), val)` for overloads  if `std::is_void_v<T>` is `false`;
:#* `std::invoke(std::forward<F>(f), std::move(val))` for overloads  if `std::is_void_v<T>` is `false`;
:#* `std::invoke(std::forward<F>(f))` if `std::is_void_v<T>` is `true`.
:# Then:
:#* if `std::is_void_v<U>` is `false`, returns a `std::expected` object that contains an expected value, direct-initialized from the result of invocation;
:#* otherwise, returns `std::expected<U, E>()`.
* Otherwise (`*this` contains an error value), returns `std::expected<U, E>(std::unexpect, error())`.

## Parameters


### Parameters


## Return value

A `std::expected` object containing either the result of `f` or an error value, as described above.

## Notes


## Example


## Defect reports


## See also


| cpp/utility/expected/dsc transform_error | (see dedicated page) |

