---
title: std::basic_ios
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios
---

ddcl|header=ios|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_ios
: public std::ios_base
The class `std::basic_ios` provides facilities for interfacing with objects that have `std::basic_streambuf` interface. Several `std::basic_ios` objects can refer to one actual `std::basic_streambuf` object.

## Public member functions


| cpp/io/basic_ios/dsc constructor | (see dedicated page) |
| cpp/io/basic_ios/dsc destructor | (see dedicated page) |

#### State functions

| cpp/io/basic_ios/dsc good | (see dedicated page) |
| cpp/io/basic_ios/dsc eof | (see dedicated page) |
| cpp/io/basic_ios/dsc fail | (see dedicated page) |
| cpp/io/basic_ios/dsc bad | (see dedicated page) |
| cpp/io/basic_ios/dsc operator! | (see dedicated page) |
| cpp/io/basic_ios/dsc operator bool | (see dedicated page) |
| cpp/io/basic_ios/dsc rdstate | (see dedicated page) |
| cpp/io/basic_ios/dsc setstate | (see dedicated page) |
| cpp/io/basic_ios/dsc clear | (see dedicated page) |

#### Formatting

| cpp/io/basic_ios/dsc copyfmt | (see dedicated page) |
| cpp/io/basic_ios/dsc fill | (see dedicated page) |

#### Miscellaneous

| cpp/io/basic_ios/dsc exceptions | (see dedicated page) |
| cpp/io/basic_ios/dsc imbue | (see dedicated page) |
| cpp/io/basic_ios/dsc rdbuf | (see dedicated page) |
| cpp/io/basic_ios/dsc tie | (see dedicated page) |
| cpp/io/basic_ios/dsc narrow | (see dedicated page) |
| cpp/io/basic_ios/dsc widen | (see dedicated page) |


## Protected member functions


| cpp/io/basic_ios/dsc init | (see dedicated page) |
| cpp/io/basic_ios/dsc move | (see dedicated page) |
| cpp/io/basic_ios/dsc swap | (see dedicated page) |
| cpp/io/basic_ios/dsc set_rdbuf | (see dedicated page) |


## Notes

Straightforward implementation of `std::basic_ios` stores only the following members (which all depend on the template parameters and thus cannot be part of `std::ios_base`):
* the fill character (see )
* the tied stream pointer (see )
* the associated stream buffer pointer (see ).
Actual implementations vary:
Microsoft Visual Studio stores just those three members.
LLVM libc++ stores 1 less member: it maintains the `rdbuf` pointer as a `void*` member of `ios_base`.
GNU libstdc++ stores 4 additional members: three cached facets and a flag to indicate that fill was initialized.
