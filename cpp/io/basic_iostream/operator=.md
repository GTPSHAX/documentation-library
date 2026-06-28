---
title: std::basic_iostream::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_iostream/operator=
---


```cpp
dcl | num=1 | 1=
basic_iostream& operator=( const basic_iostream& other ) = delete;
dcl | num=2 | since=c++11 | 1=
protected:
basic_iostream& operator=( basic_iostream&& other );
```

Assigns another stream object.
1. Copy assignment is not allowed.
2. Move assigns another stream object. Effectively calls `swap(rhs)`. This move assignment operator is protected: it is called by the move assignment operators of the derived stream classes `std::basic_stringstream` and `std::basic_fstream` which know how to properly move-assign the associated stream buffers.

## Parameters


### Parameters


## Return value

`*this`

## See also

de:cpp/io/basic iostream/operator=
es:cpp/io/basic iostream/operator=
fr:cpp/io/basic iostream/operator=
it:cpp/io/basic iostream/operator=
ja:cpp/io/basic iostream/operator=
pt:cpp/io/basic iostream/operator=
ru:cpp/io/basic iostream/operator=
zh:cpp/io/basic iostream/operator=
