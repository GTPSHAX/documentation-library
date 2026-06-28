---
title: std::nested_exception
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/nested_exception
---

ddcl|header=exception|since=c++11|1=
class nested_exception;
`std::nested_exception` is a polymorphic mixin class which can capture and store the current exception, making it possible to nest exceptions of arbitrary types within each other.
<sup>(since C++26)</sup> All member functions of `std::nested_exception` are `constexpr`.

## Member functions


## Non-member functions


| cpp/error/dsc throw_with_nested | (see dedicated page) |
| cpp/error/dsc rethrow_if_nested | (see dedicated page) |


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Example


## See also


| cpp/error/dsc exception_ptr | (see dedicated page) |
| cpp/error/dsc throw_with_nested | (see dedicated page) |
| cpp/error/dsc rethrow_if_nested | (see dedicated page) |

