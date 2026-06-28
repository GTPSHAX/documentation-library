---
title: std::bad_exception::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/bad_exception/operator=
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
bad_exception& operator=( const bad_exception& other ) throw();
|notes2=<sup>(constexpr C++26)</sup>
|dcl2=
bad_exception& operator=( const bad_exception& other ) noexcept;
```

Assigns the contents of `other`. <sup>(since C++11)</sup> If `*this` and `other` both have dynamic type `std::exception` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another `bad_exception` object to assign

## Return value

`*this`.
