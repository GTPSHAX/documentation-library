---
title: std::basic_istringstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istringstream
---

ddcl|header=sstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
> class basic_istringstream : public basic_istream<CharT, Traits>;
The class template `std::basic_istringstream` implements input operations on string based streams. It effectively stores an instance of `std::basic_string` and performs input operations on it.
At the low level, the class essentially wraps a raw string device implementation of `std::basic_stringbuf` into a higher-level interface of `std::basic_istream`. The complete interface to unique `std::basic_stringbuf` members is provided.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/io/dsc char_type | (see dedicated page) |
| cpp/io/dsc traits_type | (see dedicated page) |
| cpp/io/dsc int_type | (see dedicated page) |
| cpp/io/dsc pos_type | (see dedicated page) |
| cpp/io/dsc off_type | (see dedicated page) |
| cpp/io/dsc allocator_type | (see dedicated page) |


## Exposition-only members


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Member functions


| cpp/io/basic_stringstream/dsc constructor|basic_istringstream | (see dedicated page) |
| cpp/io/basic_stringstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_stringstream/dsc swap|basic_istringstream | (see dedicated page) |
| cpp/io/basic_stringstream/dsc rdbuf|basic_istringstream | (see dedicated page) |

#### String operations

| cpp/io/basic_stringstream/dsc str|basic_istringstream | (see dedicated page) |
| cpp/io/basic_stringstream/dsc view|basic_istringstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_stringstream/dsc swap2|basic_istringstream | (see dedicated page) |

