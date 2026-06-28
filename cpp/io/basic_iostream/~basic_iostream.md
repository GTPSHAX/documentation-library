---
title: std::basic_iostream::~basic_iostream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_iostream/~basic_iostream
---

ddcl |
virtual ~basic_iostream();
Destructs the input/output stream.

## Notes

This destructor does not perform any operation on the underlying stream buffer (`rdbuf()`): the destructors of the derived streams such as `std::basic_fstream` and `std::basic_stringstream` are responsible for calling the destructors of the stream buffers.
de:cpp/io/basic iostream/~basic iostream
es:cpp/io/basic iostream/~basic iostream
fr:cpp/io/basic iostream/~basic iostream
it:cpp/io/basic iostream/~basic iostream
ja:cpp/io/basic iostream/~basic iostream
pt:cpp/io/basic iostream/~basic iostream
ru:cpp/io/basic iostream/~basic iostream
zh:cpp/io/basic iostream/~basic iostream
