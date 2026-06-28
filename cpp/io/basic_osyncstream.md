---
title: std::basic_osyncstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream
---


```cpp
**Header:** `<`syncstream`>`
dcl|since=c++20|1=
template<
class CharT,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
> class basic_osyncstream : public std::basic_ostream<CharT, Traits>
```

The class template `std::basic_osyncstream` is a convenience wrapper for `cpp/io/basic_syncbuf|std::basic_syncbuf`. It provides a mechanism to synchronize threads writing to the same stream.
It can be used with a named variable:

```cpp
{
    std::osyncstream synced_out(std::cout); // synchronized wrapper for std::cout
    synced_out << "Hello, ";
    synced_out << "World!";
    synced_out << std::endl; // flush is noted, but not yet performed
    synced_out << "and more!\n";
} // characters are transferred and std::cout is flushed
```

as well as with a temporary:

```cpp
std::osyncstream(std::cout) << "Hello, " << "World!" << '\n';
```

It provides the guarantee that all output made to the same final destination buffer (`std::cout` in the examples above) will be free of data races and will not be interleaved or garbled in any way, as long as every write to that final destination buffer is made through (possibly different) instances of `std::basic_osyncstream`.
Typical implementation of `std::basic_osyncstream` holds only one member: the wrapped `std::basic_syncbuf`.

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


| cpp/io/basic_osyncstream/dsc constructor | (see dedicated page) |
| 1=cpp/io/basic_osyncstream/dsc operator= | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc destructor | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc rdbuf | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc get_wrapped | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc emit | (see dedicated page) |


## Notes

