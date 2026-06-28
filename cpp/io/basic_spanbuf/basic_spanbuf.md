---
title: std::basic_spanbuf::basic_spanbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/basic_spanbuf
---


```cpp
dcl|num=1|since=c++23|
basic_spanbuf() : basic_spanbuf(std::ios_base::in | std::ios_base::out) {}
dcl|num=2|since=c++23|
explicit basic_spanbuf( std::ios_base::openmode which )
: basic_spanbuf(std::span<CharT>{}, which) {}
dcl|num=3|since=c++23|1=
explicit basic_spanbuf( std::span<CharT> buf, std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
dcl|num=4|since=c++23|1=
basic_spanbuf( const basic_spanbuf& ) = delete;
dcl|num=5|since=c++23|1=
basic_spanbuf( basic_spanbuf&& rhs );
```

1. Default constructor. Creates a `basic_spanbuf` that has no underlying buffer and is opened for both input and output. The pointers to get and put area are set to the null pointer value.
2. Same as , except that the `basic_spanbuf` is opened in mode specified by `which`.
3. Creates a `basic_spanbuf` that manages the underlying buffer referenced by `buf` (or has no underlying buffer if `buf` is empty) and is opened in mode specified by `which`. The pointers to get and put area are set as following, or to the null pointer value if not mentioned in the table:


| - |
| rowspan="2" | Set bits in open mode<br>(affecting pointers to get area) |
| colspan="3" | Return value after setting |
| - |
| lc | std::basic_streambuf::eback | eback() |
| lc | std::basic_streambuf::gptr | gptr() |
| lc | std::basic_streambuf::egptr | egptr() |
| - |
| c | std::ios_base::in |
| c | s.data() |
| c | s.data() |
| c | s.data() + s.size() |
| - |
| colspan="4" | <nowiki/> |
| - |
| rowspan="2" | Set bits in open mode<br>(affecting pointers to put area) |
| colspan="3" | Return value after setting |
| - |
| lc | std::basic_streambuf::pbase | pbase() |
| lc | std::basic_streambuf::pptr | pptr() |
| lc | std::basic_streambuf::epptr | epptr() |
| - |
| c | std::ios_base::out && !std::ios_base::ate |
| c | s.data() |
| c | s.data() |
| c | s.data() + s.size() |
| - |
| c | std::ios_base::out && std::ios_base::ate |
| c | s.data() |
| c | s.data() + s.size() |
| c | s.data() + s.size() |

4. Copy constructor is deleted. `basic_spanbuf` is not copyable.
5. Move constructor. Move-constructs the `std::basic_streambuf` base subobject from that of `rhs`. The pointers to get and put area, the open mode, and the underlying buffer (if any) are identical to those in `rhs` before construction.<br>It is implementation-defined whether `rhs` still holds the underlying buffer after the move-construction.

## Parameters


### Parameters

- `buf` - a `cpp/container/span|std::span` referencing the underlying buffer
- `rhs` - another `basic_spanbuf`
- `which` - specifies stream open mode. It is bitmask type, the following constants are defined:

## Notes

These constructors are typically called by the constructors of `std::basic_ispanstream`, `std::basic_ospanstream`, and `std::basic_spanstream`.

## Example

