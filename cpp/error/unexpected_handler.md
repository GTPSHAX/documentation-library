---
title: std::unexpected_handler
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/unexpected_handler
---

ddcl|header=exception|deprecated=c++11|until=c++17|
typedef void ( *unexpected_handler )();
`std::unexpected_handler` is the function pointer type (pointer to function that takes no arguments and returns void), which is installed and queried by the functions `std::set_unexpected` and `std::get_unexpected` and called by `std::unexpected`.
The C++ implementation provides a default `std::unexpected_handler` function, which calls `std::terminate()`. If the null pointer value is installed (by means of `std::set_unexpected`), the implementation may restore the default handler instead.
A user-defined `std::unexpected_handler` is expected to either terminate the program or throw an exception. If it throws an exception, one of the following three situations may be encountered:
1) the exception thrown by `std::unexpected_handler` satisfies the dynamic exception specification that was violated earlier. The new exception is allowed to escape the function and stack unwinding continues.
2) the exception thrown by `std::unexpected_handler` still violates the exception specification:
2a) however, the exception specification allows `std::bad_exception`: the thrown exception object is destroyed, and `std::bad_exception` is constructed by the C++ runtime and thrown instead.
2b) the exception specification does not allow `std::bad_exception`: `std::terminate()` is called.

## See also


| cpp/error/dsc unexpected | (see dedicated page) |
| cpp/error/dsc set_unexpected | (see dedicated page) |
| cpp/error/dsc get_unexpected | (see dedicated page) |

