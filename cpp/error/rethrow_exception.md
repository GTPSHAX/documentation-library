---
title: std::rethrow_exception
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/rethrow_exception
---

ddcla|header=exception|since=c++11|constexpr=c++26|
noreturn void rethrow_exception( std::exception_ptr p );
Throws the previously captured exception object referred-to by the exception pointer `p`, or a copy of that object.
It is unspecified whether a copy is made. If a copy is made, the storage for it is allocated in an unspecified way.
The behavior is undefined if `p` is null.

## Parameters


### Parameters

- `p` - non-null `std::exception_ptr`

## Exceptions

The exception object referred-to by `p` if no copy is made.
Otherwise, a copy of such exception object if the implementation successfully copied the exception object.
Otherwise, `std::bad_alloc` or the exception thrown when copying the exception object, if allocation or copying fails, respectively.

## Notes

Before `P1675R2`, `rethrow_exception` was not allowed to copy the exception object, which is unimplementable on some platforms where exception objects are allocated on the stack.

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Example


## See also


| cpp/error/dsc exception_ptr | (see dedicated page) |
| cpp/error/dsc current_exception | (see dedicated page) |

