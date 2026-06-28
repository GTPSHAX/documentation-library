---
title: std::basic_ostream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream
---

ddcl|header=ostream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_ostream : virtual public std::basic_ios<CharT, Traits>
The class template `basic_ostream` provides support for high level output operations on character streams. The supported operations include formatted output (e.g. integer values) and unformatted output (e.g. raw characters and character arrays). This functionality is implemented in terms of the interface provided by the `basic_streambuf` class, accessed through the `basic_ios` base class. In typical implementations, `basic_ostream` has no non-inherited data members.

## Global objects

Six global `basic_ostream` objects are provided by the standard library:


| iostream | |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/dsc cerr | (see dedicated page) |
| cpp/io/dsc clog | (see dedicated page) |


## Member functions


| cpp/io/basic_ostream/dsc constructor | (see dedicated page) |
| cpp/io/basic_ostream/dsc destructor | (see dedicated page) |
| cpp/io/basic_ostream/dsc operator{{= | (see dedicated page) |

#### Formatted output

| cpp/io/basic_ostream/dsc operator_ltlt | (see dedicated page) |

#### Unformatted output

| cpp/io/basic_ostream/dsc put | (see dedicated page) |
| cpp/io/basic_ostream/dsc write | (see dedicated page) |

#### Positioning

| cpp/io/basic_ostream/dsc tellp | (see dedicated page) |
| cpp/io/basic_ostream/dsc seekp | (see dedicated page) |

#### Miscellaneous

| cpp/io/basic_ostream/dsc flush | (see dedicated page) |
| cpp/io/basic_ostream/dsc swap | (see dedicated page) |


## Member classes


| cpp/io/basic_ostream/dsc sentry | (see dedicated page) |


## Non-member functions


| cpp/io/basic_ostream/dsc operator_ltlt2 | (see dedicated page) |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/io/basic_ostream/dsc println | (see dedicated page) |
| cpp/io/basic_ostream/dsc vprint_unicode | (see dedicated page) |
| cpp/io/basic_ostream/dsc vprint_nonunicode | (see dedicated page) |

