---
title: std::reference_wrapper::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper/operator=
---

ddcl|since=c++11|notes=<sup>(constexpr C++20)</sup>|1=
reference_wrapper& operator=( const reference_wrapper& other ) noexcept;
Copy assignment operator. Drops the current reference and stores a reference to `other.get()`.

## Parameters


### Parameters

- `other` - reference wrapper to copy

## Return value

`*this`
