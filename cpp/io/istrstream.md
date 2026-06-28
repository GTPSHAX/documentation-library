---
title: std::istrstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/istrstream
---

ddcl|header=strstream|deprecated=c++98|removed=c++26|1=
class istrstream : public std::istream
The class `istrstream` implements input operations on array-backed streams. It essentially wraps a raw array I/O device implementation (`std::strstreambuf`) into the higher-level interface of `std::basic_istream`.
The typical implementation of `istrstream` holds only one non-derived data member: an object of type `std::strstreambuf`.

## Notes

`istrstream` has been deprecated since C++98 and removed since C++26. `std::istringstream`<sup>(since C++23)</sup> , `cpp/io/basic_ispanstream|std::ispanstream`, and [https://www.boost.org/doc/libs/release/libs/iostreams/doc/classes/array.html#array_source `boost::iostreams::array_source`] are the recommended replacements.

## Member functions


| cpp/io/strstream/dsc constructor|istrstream | (see dedicated page) |
| cpp/io/strstream/dsc destructor|istrstream | (see dedicated page) |
| cpp/io/strstream/dsc rdbuf|istrstream | (see dedicated page) |
| cpp/io/strstream/dsc str|istrstream | (see dedicated page) |

