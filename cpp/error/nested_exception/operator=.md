---
title: std::nested_exception::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/nested_exception/operator=
---

ddcla|since=c++11|constexpr=c++26|1=
nested_exception& operator=( const nested_exception& other ) noexcept = default;
Replaces the stored exception with the one held in `other`.

## Parameters


### Parameters

- `other` - nested exception to replace the contents with 

## Return value

`*this`
