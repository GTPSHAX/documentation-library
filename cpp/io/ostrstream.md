---
title: std::ostrstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ostrstream
---

ddcl|header=strstream|deprecated=c++98|removed=c++26|1=
class ostrstream : public std::ostream
The class `ostrstream` implements output operations on array-backed streams. It essentially wraps a raw array I/O device implementation (`std::strstreambuf`) into the higher-level interface of `std::basic_ostream`.
The typical implementation of `ostrstream` holds only one non-derived data member: an object of type `std::strstreambuf`.

## Notes

After any call to `str()`, a call to `freeze()|freeze(false)` is required to allow the destructor to deallocate the buffer as necessary.
Before any call to `str()` that uses the result as a C-string, the buffer must be null-terminated, typically with `std::ends`.
`ostrstream` has been deprecated since C++98 and removed since C++26. `std::ostringstream`<sup>(since C++23)</sup> , `cpp/io/basic_ospanstream|std::ospanstream`,  and [https://www.boost.org/doc/libs/release/libs/iostreams/doc/classes/array.html#array_sink `boost::iostreams::array_sink`] are the recommended replacements.

## Member functions


| cpp/io/strstream/dsc constructor|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc destructor|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc rdbuf|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc str|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc freeze|ostrstream | (see dedicated page) |
| cpp/io/strstream/dsc pcount|ostrstream | (see dedicated page) |

