---
title: std::basic_streambuf::basic_streambuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/basic_streambuf
---


```cpp
dcl|num=1|
protected:
basic_streambuf();
dcl|num=2|since=c++11|
protected:
basic_streambuf(const basic_streambuf& rhs);
```

1. Constructs the `basic_streambuf` object, initializes the six pointer members (`eback()`, `gptr()`, `egptr()`, `pbase()`, `pptr()`, and `epptr()`) to null pointer values, and the locale member to `std::locale()`, a copy of the global C++ locale at the time of construction.
2. Constructs a copy of `rhs`, initializing the six pointers and the locale object with the copies of the values held by `rhs`. Note that this is a shallow copy: the pointers of the newly-constructed basic_streambuf are pointing into the same character array as the pointers of `rhs`.
Both constructors are protected, and are only called by the concrete streambuf classes, such as `std::basic_filebuf`, `std::basic_stringbuf`, or `std::strstreambuf`.

## Parameters


### Parameters

- `rhs` - a streambuf object to copy

## Notes

Until C++11, it was unspecified whether `basic_streambuf` or any of its derived classes is *CopyConstructible* (), and different C++ library implementations provided different options.

## Example

