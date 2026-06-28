---
title: std::basic_ispanstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ispanstream
---

ddcl|header=spanstream|since=c++23|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_ispanstream
: public basic_istream<CharT, Traits>
The class template `std::basic_ispanstream` implements input operations on streams based on fixed buffers.
At the low level, the class essentially wraps a raw device implementation of `std::basic_spanbuf` into a higher-level interface of `std::basic_istream`. The complete interface to unique `std::basic_spanbuf` members is provided.

## Data members


| Item | Description |
|------|-------------|
| **Member object** | Definition |


## Member functions


| cpp/io/basic_spanstream/dsc constructor|basic_ispanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_spanstream/dsc swap|basic_ispanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc rdbuf|basic_ispanstream | (see dedicated page) |

#### Underlying buffer operations

| cpp/io/basic_spanstream/dsc span|basic_ispanstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_spanstream/dsc swap2|basic_ispanstream | (see dedicated page) |


## Notes

