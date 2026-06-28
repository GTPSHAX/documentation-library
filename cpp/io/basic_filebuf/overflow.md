---
title: std::basic_filebuf::overflow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/overflow
---

ddcl|1=
protected:
virtual int_type overflow( int_type ch = Traits::eof() );
Writes some data from the put area to the associated character sequence (to the file).
Behaves like the base class version `std::basic_streambuf::overflow()`, except that the behavior of “consuming characters” is defined as follows:
1. First, uses `std::codecvt::out` of the imbued locale to convert the characters into external (possibly multibyte) representation, stored in a temporary buffer, as follows: (`XSIZE` is some unspecified buffer size)

```cpp
const std::codecvt<CharT, char, typename Traits::state_type>& a_codecvt =
    std::use_facet<std::codecvt<CharT, char, typename Traits::state_type>>(getloc());
typename Traits::state_type state;
CharT* end;
char xbuf[XSIZE];
char* xbuf_end;
std::codecvt_base::result r =
    a_codecvt.out(state, pbase(), pptr(), end, xbuf, xbuf + XSIZE, xbuf_end);
```

2. Then writes all fully-converted characters from the buffer into the file. Formally, performs the following steps based on the value of `r`:


| normal | c | r |
| Operation |
| - |
| c | std::codecvt_base::ok |
| Output characters in range | xbuf | xbuf_end to the file, and fail if output fails. At this point if c | 1=pbase() != pptr() and c | 1=pbase() == end are both c | true (which means c | xbuf is not large enough for even one external character), then increase c | XSIZE and repeat from the beginning. |
| - |
| c | std::codecvt_base::partial |
| Output the converted external characters in range | xbuf | xbuf_end to the file, and repeat using the remaining unconverted internal characters in range | end | pptr(). If output fails, fail (without repeating). |
| - |
| c | std::codecvt_base::noconv |
| Output characters in range | pbase() | pptr() to the file. |
| - |
| c | std::codecvt_base::error |
| Fail. |

@@ If the associated file is not open (`is_open()` returns `false`), output will always fail.
rrev|since=c++26|
3. Establishes an observable checkpoint.

## Parameters


### Parameters

- `ch` - the character to store in the put area

## Return value

`Traits::not_eof(ch)` to indicate success or `Traits::eof()` to indicate failure.

## Notes

If `a_codecvt.always_noconv()` returns `true`, the call to `a_codecvt.out()` may be skipped.

## Example

