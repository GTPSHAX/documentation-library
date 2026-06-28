---
title: std::basic_streambuf::sputc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sputc
---

ddcl | 1=
int_type sputc( char_type ch );
Writes one character to the output sequence.
If the output sequence write position is not available (the buffer is full), then calls `overflow(ch)`.

## Parameters


### Parameters


## Return value

The written character, converted to `int_type` with `Traits::to_int_type(ch)` on success.
`Traits::eof()` (as returned by `overflow()`) on failure.

## Example


## See also

de:cpp/io/basic streambuf/sputc
es:cpp/io/basic streambuf/sputc
fr:cpp/io/basic streambuf/sputc
it:cpp/io/basic streambuf/sputc
ja:cpp/io/basic streambuf/sputc
pt:cpp/io/basic streambuf/sputc
ru:cpp/io/basic streambuf/sputc
zh:cpp/io/basic streambuf/sputc
