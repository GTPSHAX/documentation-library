---
title: std::basic_istream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream
---

ddcl|header=istream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_istream : virtual public std::basic_ios<CharT, Traits>
The class template `basic_istream` provides support for high level input operations on character streams. The supported operations include formatted input (e.g. integer values or whitespace-separated characters and characters strings) and unformatted input (e.g. raw characters and character arrays). This functionality is implemented in terms of the interface provided by the underlying `basic_streambuf` class, accessed through the `basic_ios` base class. The only non-inherited data member of `basic_istream`, in most implementations, is the value returned by .

## Global objects

Two global basic_istream objects are provided by the standard library.


| iostream | |
| cpp/io/dsc cin | (see dedicated page) |


## Member functions


| cpp/io/basic_istream/dsc constructor | (see dedicated page) |
| cpp/io/basic_istream/dsc destructor | (see dedicated page) |
| cpp/io/basic_istream/dsc operator{{= | (see dedicated page) |

#### Formatted input

| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |

#### Unformatted input

| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc peek | (see dedicated page) |
| cpp/io/basic_istream/dsc unget | (see dedicated page) |
| cpp/io/basic_istream/dsc putback | (see dedicated page) |
| cpp/io/basic_istream/dsc getline | (see dedicated page) |
| cpp/io/basic_istream/dsc ignore | (see dedicated page) |
| cpp/io/basic_istream/dsc read | (see dedicated page) |
| cpp/io/basic_istream/dsc readsome | (see dedicated page) |
| cpp/io/basic_istream/dsc gcount | (see dedicated page) |

#### Positioning

| cpp/io/basic_istream/dsc tellg | (see dedicated page) |
| cpp/io/basic_istream/dsc seekg | (see dedicated page) |

#### Miscellaneous

| cpp/io/basic_istream/dsc sync | (see dedicated page) |
| cpp/io/basic_istream/dsc swap | (see dedicated page) |


## Member classes


| cpp/io/basic_istream/dsc sentry | (see dedicated page) |


## Non-member functions


| cpp/io/basic_istream/dsc operator_gtgt2 | (see dedicated page) |

