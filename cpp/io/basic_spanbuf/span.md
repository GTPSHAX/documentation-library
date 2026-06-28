---
title: std::basic_spanbuf::span
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/span
---


```cpp
dcl | num=1 | since=c++23 |
std::span<CharT> span() const noexcept;
dcl | num=2 | since=c++23 |
void span( std::span<CharT> s ) noexcept;
```

1. Gets a `span` referencing the written area if `std::ios_base::out` is set in the open mode, or a `span` referencing the underlying buffer otherwise.
2. Makes the `basic_spanbuf` perform I/O on the buffer referenced by `s`. Sets pointers to get area, put area, or both.


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


## Parameters


### Parameters


## Return value

1. `std::span<CharT>(pbase(), pptr())` if `std::ios_base::out` is set in the open mode, or a `std::span<CharT>` that references the whole underlying buffer otherwise.
2. (none)

## Example

