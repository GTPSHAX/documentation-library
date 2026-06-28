---
title: std::exception_ptr
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/exception_ptr
---

ddcl|header=exception|since=c++11|1=
using exception_ptr = /*unspecified*/
`std::exception_ptr` is a nullable pointer-like type that manages an exception object which has been thrown and captured with `std::current_exception`. An instance of `std::exception_ptr` may be passed to another function, possibly on another thread, where the exception may be rethrown and handled with a `catch` clause.
A default-constructed `std::exception_ptr` is a null pointer; it does not point to an exception object.
Two instances of `std::exception_ptr` compare equal only if they are both null or both point at the same exception object.
`std::exception_ptr` is not implicitly convertible to any arithmetic, enumeration, or pointer type. It is contextually convertible to `bool`, and will evaluate to `false` if it is null, `true` otherwise.
The exception object referenced by an `std::exception_ptr` remains valid as long as there remains at least one `std::exception_ptr` that is referencing it: `std::exception_ptr` is a shared-ownership smart pointer (note: this is in addition to the usual exception object lifetime rules).
`std::exception_ptr` meets the requirements of *NullablePointer*.

## Example


## See also


| cpp/error/dsc make_exception_ptr | (see dedicated page) |
| cpp/error/dsc current_exception | (see dedicated page) |
| cpp/error/dsc rethrow_exception | (see dedicated page) |

