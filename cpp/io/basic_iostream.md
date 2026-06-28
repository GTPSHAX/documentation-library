---
title: std::basic_iostream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_iostream
---

ddcl|header=istream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_iostream :
public basic_istream<CharT, Traits>,
public basic_ostream<CharT, Traits>
The class template `basic_iostream` provides support for high level input/output operations on streams. The supported operations include sequential reading or writing and formatting. This functionality is implemented over the interface provided by the `std::basic_streambuf` class. It is accessed through `std::basic_ios` class.

## Member functions


| cpp/io/basic_iostream/dsc constructor | (see dedicated page) |
| cpp/io/basic_iostream/dsc destructor | (see dedicated page) |


## Protected member functions


| cpp/io/basic_iostream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_iostream/dsc swap | (see dedicated page) |


## Defect reports


## See also

* `Input/output manipulators`
