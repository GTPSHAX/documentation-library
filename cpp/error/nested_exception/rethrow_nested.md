---
title: std::nested_exception::rethrow_nested
type: Utilities
source: https://en.cppreference.com/w/cpp/error/nested_exception/rethrow_nested
---

ddcla|since=c++11|constexpr=c++26|1=
noreturn void rethrow_nested() const;
Rethrows the stored exception. If there is no stored exceptions (i.e. `nested_ptr()` returns null pointer), then `std::terminate` is called.

## Parameters

(none)

## Return value

(none)
