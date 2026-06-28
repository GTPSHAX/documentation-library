---
title: errno
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/errno
---


# errno

ddcl|header=cerrno|
#define errno /* implementation-defined */
`errno` is a preprocessor macro used for error indication. It expands to a <sup>(until C++11)</sup> static<sup>(since C++11)</sup> thread-local modifiable lvalue of type `int`.
Several standard library functions indicate errors by writing positive integers to `errno`. Typically, the value of `errno` is set to one of the error codes, listed in  as macro constants that begin with the letter `E`, followed by uppercase letters or digits.
The value of `errno` is `0` at program startup, and although library functions are allowed to write positive integers to `errno` whether or not an error occurred, library functions never store `0` in `errno`.

## Example


## See also


| cpp/error/dsc errno_macros | (see dedicated page) |
| cpp/io/c/dsc perror | (see dedicated page) |
| cpp/string/byte/dsc strerror | (see dedicated page) |

