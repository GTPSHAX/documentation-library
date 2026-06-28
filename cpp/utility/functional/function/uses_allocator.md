---
title: std::uses_allocator<std::function>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/uses_allocator
---


```cpp
dcl | since=c++11 | until=c++17 |
template< class R, class... ArgTypes, class Alloc >
struct uses_allocator<std::function<R(ArgTypes...)>, Alloc> : std::true_type { };
```

This specialization of `std::uses_allocator` informs other library components that all objects of type `std::function` support ''uses-allocator construction'', even though they do not have a nested `allocator_type`.

## Notes

`std::function`'s allocator support was poorly specified and inconsistently implemented. Some implementations do not support uses-allocator construction at all, some provide the needed constructor overloads but ignore the supplied allocator argument, and some provide the overloads and use the supplied allocator for construction but not when the `std::function` is reassigned. As a result, allocator support was removed in C++17.

## See also

