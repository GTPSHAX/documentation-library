---
title: std::scoped_allocator_adaptor::max_size
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/max_size
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|since=c++11|
size_type max_size() const;
```

Reports the maximum allocation size supported by the outer allocator, by calling `std::allocator_traits<OuterAlloc>::max_size(outer_allocator())`.

## Parameters

(none)

## Return value

The maximum allocation size for OuterAlloc.

## See also


| cpp/memory/allocator/dsc max_size | (see dedicated page) |
| cpp/memory/allocator_traits/dsc max_size | (see dedicated page) |

