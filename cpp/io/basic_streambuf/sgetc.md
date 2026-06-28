---
title: std::basic_streambuf::sgetc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sgetc
---

ddcl | 1=
int_type sgetc();
Reads one character from the input sequence.
If the input sequence read position is not available, returns `underflow()`. Otherwise returns `Traits::to_int_type(*gptr())`.

## Parameters

(none)

## Return value

The value of the character pointed to by the ''get pointer''.

## Example


## See also

de:cpp/io/basic streambuf/sgetc
es:cpp/io/basic streambuf/sgetc
fr:cpp/io/basic streambuf/sgetc
it:cpp/io/basic streambuf/sgetc
ja:cpp/io/basic streambuf/sgetc
pt:cpp/io/basic streambuf/sgetc
ru:cpp/io/basic streambuf/sgetc
zh:cpp/io/basic streambuf/sgetc
