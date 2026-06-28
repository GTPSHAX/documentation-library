---
title: std::basic_spanstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanstream
---

ddcl|header=spanstream|since=c++23|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_spanstream
: public basic_iostream<CharT, Traits>
The class template `std::basic_spanstream` implements input and output operations on streams based on fixed buffers.
At the low level, the class essentially wraps a raw device implementation of `std::basic_spanbuf` into a higher-level interface of `std::basic_iostream`. The complete interface to unique `std::basic_spanbuf` members is provided.

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member functions


| cpp/io/basic_spanstream/dsc constructor|basic_spanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_spanstream/dsc swap|basic_spanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc rdbuf|basic_spanstream | (see dedicated page) |

#### Underlying buffer operations

| cpp/io/basic_spanstream/dsc span|basic_spanstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_spanstream/dsc swap2|basic_spanstream | (see dedicated page) |


## Notes

