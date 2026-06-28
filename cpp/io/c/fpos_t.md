---
title: std::fpos_t
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fpos_t
---

ddcl|header=cstdio|
typedef /* implementation-defined */ fpos_t;
`std::fpos_t` is a non-array complete object type, can be used to store (by `std::fgetpos`) and restore (by `std::fsetpos`) the position and multibyte parser state (if any) for a C stream.
The multibyte parser state of a wide-oriented C stream is represented by a `std::mbstate_t` object, whose value is stored as part of the value of a `std::fpos_t` object by `std::fgetpos`.

## See also

