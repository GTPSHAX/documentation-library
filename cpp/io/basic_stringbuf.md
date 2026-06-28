---
title: std::basic_stringbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf
---

ddcl|header=sstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
> class basic_stringbuf
: public std::basic_streambuf<CharT, Traits>
`std::basic_stringbuf` is a `std::basic_streambuf` whose associated character sequence is a memory-resident sequence of arbitrary characters, which can be initialized from or made available as an instance of `std::basic_string`.
Typical implementations of `std::basic_stringbuf` hold an object of type `std::basic_string` or equivalent resizable sequence container directly as a data member and use it as both the controlled character sequence (the array where the six pointers of `std::basic_streambuf` are pointing to) and as the associated character sequence (the source of characters for all input operations and the target for the output).
In addition, a typical implementation holds a data member of type `std::ios_base::openmode` to indicate the I/O mode of the associated stream (input-only, output-only, input/output, at-end, etc).
<sup>(since C++11)</sup> If over-allocation strategy is used by `overflow()`, an additional high-watermark pointer may be stored to track the last initialized character.

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


## Public member functions


| cpp/io/basic_stringbuf/dsc constructor | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc swap | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc destructor | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc str | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc get_allocator | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc view | (see dedicated page) |


## Protected member functions


| cpp/io/basic_stringbuf/dsc underflow | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc pbackfail | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekpos | (see dedicated page) |


## Non-member functions


| cpp/io/basic_stringbuf/dsc swap2 | (see dedicated page) |

