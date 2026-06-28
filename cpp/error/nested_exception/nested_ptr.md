---
title: std::nested_exception::nested_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/error/nested_exception/nested_ptr
---

ddcla|since=c++11|constexpr=c++26|1=
std::exception_ptr nested_ptr() const noexcept;
Returns a pointer to the stored exception, if any.

## Parameters

(none)

## Return value

A `std::exception_ptr` to the stored exception if one is stored, default-initialized `std::exception_ptr` otherwise.
