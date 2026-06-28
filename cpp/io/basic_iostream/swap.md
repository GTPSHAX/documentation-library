---
title: std::basic_iostream::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_iostream/swap
---

ddcl | since=c++11 | 1=
protected:
void swap( basic_iostream& other );
Exchanges the state with another input/output stream object. Effectively calls `basic_istream<CharT,Traits>::swap(other)`.
This member function is protected: it is called by the swap member functions of the derived stream classes `std::basic_stringstream` and `std::basic_fstream`, which know how to correctly swap the associated stream buffers.

## Parameters


### Parameters


## Return value

`*this`
de:cpp/io/basic iostream/swap
es:cpp/io/basic iostream/swap
fr:cpp/io/basic iostream/swap
it:cpp/io/basic iostream/swap
ja:cpp/io/basic iostream/swap
pt:cpp/io/basic iostream/swap
ru:cpp/io/basic iostream/swap
zh:cpp/io/basic iostream/swap
