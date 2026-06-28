---
title: std::basic_syncbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf
---

ddcl|header=syncstream|since=c++20|1=
template<
class CharT,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
> class basic_syncbuf : public std::basic_streambuf<CharT, Traits>
`std::basic_syncbuf` is a wrapper for a `std::basic_streambuf` (provided at construction time as a pointer). It accumulates output in its own internal buffer, and atomically transmits its entire contents to the wrapped buffer on destruction and when explicitly requested, so that they appear as a contiguous sequence of characters. It guarantees that there are no data races and no interleaving of characters sent to the wrapped buffer as long as all other outputs made to the same buffer are made through, possibly different, instances of `std::basic_syncbuf`.
Typical implementation of `std::basic_syncbuf` holds a pointer to the wrapped `std::basic_streambuf`, a boolean flag indicating whether the buffer will transmit its contents to the wrapped buffer on sync (flush), a boolean flag indicating a pending flush when the policy is to not emit on sync, an internal buffer that uses `Allocator` (such as `std::string`), and a pointer to a mutex used to synchronize emit between multiple threads accessing the same wrapped stream buffer (these mutexes may be in a hash map with pointers to `std::basic_streambuf` objects used as keys).
Like other streambuf classes, `std::basic_syncbuf` is normally only accessed through the corresponding stream, `cpp/io/basic_osyncstream|std::osyncstream`, not directly.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/io/dsc char_type | (see dedicated page) |
| cpp/io/dsc traits_type | (see dedicated page) |
| cpp/io/dsc int_type | (see dedicated page) |
| cpp/io/dsc pos_type | (see dedicated page) |
| cpp/io/dsc off_type | (see dedicated page) |


## Member functions


| cpp/io/basic_syncbuf/dsc constructor | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc swap | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc destructor | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc emit | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc get_wrapped | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc get_allocator | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc set_emit_on_sync | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc sync | (see dedicated page) |


## Non-member functions


| cpp/io/basic_syncbuf/dsc swap2 | (see dedicated page) |


## Notes

