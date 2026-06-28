---
title: std::basic_streambuf::snextc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/snextc
---

ddcl | 1=
int_type snextc();
Advances the input sequence by one character and reads one character.
The function calls `sbumpc()` to advance the input sequence. If that function returns `Traits::eof()` meaning that input sequence has been exhausted and `uflow()` could not retrieve more data, `Traits::eof()` is returned. Otherwise `sgetc()` is called in order to read the character.

## Parameters

(none)

## Return value

The value of the next character. If the input sequence has been exhausted, `Traits::eof()` is returned.

## Example


## See also

de:cpp/io/basic streambuf/snextc
es:cpp/io/basic streambuf/snextc
fr:cpp/io/basic streambuf/snextc
it:cpp/io/basic streambuf/snextc
ja:cpp/io/basic streambuf/snextc
pt:cpp/io/basic streambuf/snextc
ru:cpp/io/basic streambuf/snextc
zh:cpp/io/basic streambuf/snextc
