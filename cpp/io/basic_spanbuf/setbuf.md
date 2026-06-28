---
title: std::basic_spanbuf::setbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/setbuf
---

ddcl|since=c++23|
protected:
std::basic_streambuf<CharT, Traits>* setbuf( CharT *s, std::streamsize n ) override;
Makes the `basic_spanbuf` perform I/O on the buffer [s, s + n). Equivalently calls `this->span(std::span<CharT>(s, n))` and then returns `this`.


| - |
| rowspan="2" | Set bits in open mode<br>(affecting pointers to get area) |
| colspan="3" | Return value after setting |
| - |
| lc | std::basic_streambuf::eback | eback() |
| lc | std::basic_streambuf::gptr | gptr() |
| lc | std::basic_streambuf::egptr | egptr() |
| - |
| c | std::ios_base::in |
| c | s |
| c | s |
| c | s + n |
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
| c | s |
| c | s |
| c | s + n |
| - |
| c | std::ios_base::out && std::ios_base::ate |
| c | s |
| c | s + n |
| c | s + n |

This function is protected virtual, it may only be called through `pubsetbuf()` or from member functions of a user-defined class derived from `std::basic_spanbuf`.

## Parameters


### Parameters

- `s` - pointer to the first `CharT` in the user-provided buffer
- `n` - the number of `CharT` elements in the user-provided buffer

## Return value

`this`

## Notes

The deprecated stream buffer `std::strstreambuf` or the boost.IOStreams device [https://www.boost.org/doc/libs/release/libs/iostreams/doc/classes/array.html#array `boost::basic_array`] can also implement I/O buffering over a user-provided `char` array.

## Example

