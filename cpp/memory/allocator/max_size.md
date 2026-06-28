---
title: std::allocator::max_size
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/max_size
---


```cpp
dcl rev multi|until1=c++11|dcl1=
size_type max_size() const throw();
|notes2=|dcl2=
size_type max_size() const noexcept;
```

Returns the maximum theoretically possible value of `n`, for which the call  could succeed.
In most implementations, this returns `std::numeric_limits<size_type>::max() / sizeof(value_type)`.

## Return value

The maximum supported allocation size.

## See also


| cpp/memory/allocator_traits/dsc max_size | (see dedicated page) |

