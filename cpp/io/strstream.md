---
title: std::strstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstream
---

ddcl|header=strstream|deprecated=c++98|removed=c++26|1=
class strstream : public std::iostream
The class `strstream` implements input and output operations on array-backed streams. It essentially wraps a raw array I/O device implementation (`std::strstreambuf`) into the higher-level interface of `std::basic_iostream`.
The typical implementation of `strstream` holds only one non-derived data member: an object of type `std::strstreambuf`.

## Notes

After any call to `str()`, a call to `freeze()|freeze(false)` is required to allow the destructor to deallocate the buffer as necessary.
Before any call to `str()` that uses the result as a C-string, the buffer must be null-terminated, typically with `std::ends`.
`strstream` has been deprecated since C++98 and removed since C++26. `std::stringstream`<sup>(since C++23)</sup> , `cpp/io/basic_spanstream|std::spanstream`, and [https://www.boost.org/doc/libs/release/libs/iostreams/doc/classes/array.html#array `boost::iostreams::array`] are the recommended replacements.

## Member functions


| cpp/io/strstream/dsc constructor|strstream | (see dedicated page) |
| cpp/io/strstream/dsc destructor|strstream | (see dedicated page) |
| cpp/io/strstream/dsc rdbuf|strstream | (see dedicated page) |
| cpp/io/strstream/dsc str|strstream | (see dedicated page) |
| cpp/io/strstream/dsc freeze|strstream | (see dedicated page) |
| cpp/io/strstream/dsc pcount|strstream | (see dedicated page) |

