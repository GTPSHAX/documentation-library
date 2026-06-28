---
title: std::basic_spanbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf
---

ddcl|header=spanstream|since=c++23|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_spanbuf
: public std::basic_streambuf<CharT, Traits>
`std::basic_spanbuf` is a `std::basic_streambuf` whose associated character sequence is a memory-resident sequence of arbitrary characters, which can be initialized from or made available as an instance of `std::span<CharT>`.
`std::basic_spanbuf` performs I/O on a fixed buffer, and therefore it does not attempt to obtain a new buffer when the underlying buffer is exhausted.

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member functions


#### Public member functions

| cpp/io/basic_spanbuf/dsc constructor | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc swap | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc span | (see dedicated page) |

#### Protected member functions

| cpp/io/basic_spanbuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc seekpos | (see dedicated page) |


## Non-member functions


| cpp/io/basic_spanbuf/dsc swap2 | (see dedicated page) |


## Notes

`std::basic_spanbuf` does not own the underlying buffer.
It is the responsibility of programmers to ensure the underlying buffer is in its lifetime when used by a `std::basic_spanbuf` object. Additional synchronization may be needed if more than one thread operates the same underlying buffer through different `std::basic_spanbuf` objects.

## See also


| cpp/io/dsc basic_stringbuf | (see dedicated page) |
| cpp/io/dsc strstreambuf | (see dedicated page) |

