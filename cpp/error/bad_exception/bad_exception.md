---
title: std::bad_exception::bad_exception
type: Utilities
source: https://en.cppreference.com/w/cpp/error/bad_exception/bad_exception
---


```cpp
dcl rev multi|num=1|until1=c++11
|dcl1=
bad_exception() throw();
|notes2=<sup>(constexpr C++26)</sup>
|dcl2=
bad_exception() noexcept;
dcl rev multi|num=2|until1=c++11
|dcl1=
bad_exception( const bad_exception& other ) throw();
|notes2=<sup>(constexpr C++26)</sup>
|dcl2=
bad_exception( const bad_exception& other ) noexcept;
```

Constructs new `bad_exception` object.
1. Default constructor.  returns an implementation-defined string.
2. Copy constructor. Initializes the object with the contents of `other`<sup>(since C++11)</sup> . If `*this` and `other` both have dynamic type `std::bad_exception` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `other` - `bad_exception` object to initialize with
