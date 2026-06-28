---
title: std::jmp_buf
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/jmp_buf
---

ddcl|header=csetjmp|
typedef /* unspecified */ jmp_buf;
The `std::jmp_buf` type is an array type suitable for storing information to restore a calling environment. The stored information is sufficient to restore execution at the correct block of the program and invocation of that block. The state of floating-point status flags, or open files, or any other data is not stored in an object of type `std::jmp_buf`.

## Example


## See also


| cpp/utility/program/dsc setjmp | (see dedicated page) |
| cpp/utility/program/dsc longjmp | (see dedicated page) |

