---
title: std::exception::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/exception/operator=
---


```cpp
dcl rev multi|until1=c++11|dcl1=
exception& operator=( const exception& other ) throw();
|notes2=<sup>(constexpr C++26)</sup>
|dcl2=
exception& operator=( const exception& other ) noexcept;
```

Copy assignment operator. Assigns the contents of `other`.
If `*this` and `other` both have dynamic type `std::exception` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another exception to assign the contents of

## Defect reports

