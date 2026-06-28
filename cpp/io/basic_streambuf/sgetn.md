---
title: std::basic_streambuf::xsgetn
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sgetn
---


```cpp
dcl | num=1 | 1=
std::streamsize sgetn( char_type* s, std::streamsize count );
dcl | num=2 | 1=
protected:
virtual std::streamsize xsgetn( char_type* s, std::streamsize count );
```

1. Calls `xsgetn(s, count)` of the most derived class.
2. Reads `count` characters from the input sequence and stores them into a character array pointed to by `s`. The characters are read as if by repeated calls to `sbumpc()`. That is, if less than `count` characters are immediately available, the function calls `uflow()` to provide more until `Traits::eof()` is returned.
@@Classes derived from `std::basic_streambuf` are permitted to provide more efficient implementations of this function.

## Parameters


### Parameters


## Return value

The number of characters successfully read. If it is less than `count` the input sequence has reached the end.

## Notes

The rule about "more efficient implementations" permits bulk I/O without intermediate buffering: that's how `std::ifstream::read` simply passes the pointer to the POSIX `read()` system call in some implementations of iostreams

## Example


## See also

de:cpp/io/basic streambuf/sgetn
es:cpp/io/basic streambuf/sgetn
fr:cpp/io/basic streambuf/sgetn
it:cpp/io/basic streambuf/sgetn
ja:cpp/io/basic streambuf/sgetn
pt:cpp/io/basic streambuf/sgetn
ru:cpp/io/basic streambuf/sgetn
zh:cpp/io/basic streambuf/sgetn
