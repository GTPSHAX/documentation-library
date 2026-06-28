---
title: std::scoped_allocator_adaptor::deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/deallocate
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|since=c++11|
void deallocate( pointer p, size_type n ) noexcept;
```

Uses the outer allocator to deallocate the storage referenced by `p`, by calling `std::allocator_traits<OuterAlloc>::deallocate(outer_allocator(), p, n)`.

## Parameters


### Parameters

- `p` - pointer to the previously allocated memory
- `n` - the number of objects for which the memory was allocated

## Return value

(none)

## See also


| cpp/memory/allocator/dsc deallocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc deallocate | (see dedicated page) |

