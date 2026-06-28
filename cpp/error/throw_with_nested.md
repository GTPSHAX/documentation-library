---
title: std::throw_with_nested
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/throw_with_nested
---

ddcla|header=exception|since=c++11|constexpr=c++26|
template< class T >
noreturn void throw_with_nested( T&& t );
If `std::decay<T>::type` is a non-final non-union class type that is neither `std::nested_exception` nor derived from `std::nested_exception`, throws an exception of an unspecified type that is publicly derived from both `std::nested_exception` and from `std::decay<T>::type`, and constructed from `std::forward<T>(t)`. The default constructor of the `nested_exception` base class calls `std::current_exception`, capturing the currently handled exception object, if any, in a `std::exception_ptr`.
Otherwise, throws `std::forward<T>(t)`.
Requires that `std::decay<T>::type` is *CopyConstructible*.

## Parameters


### Parameters

- `t` - the exception object to throw

## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Example


## See also


| cpp/error/dsc nested_exception | (see dedicated page) |
| cpp/error/dsc rethrow_if_nested | (see dedicated page) |

