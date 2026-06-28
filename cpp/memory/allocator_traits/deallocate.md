---
title: std::allocator_traits::deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/deallocate
---


```cpp
**Header:** `<`memory`>`
dcla|since=c++11|constexpr=c++20|
static void deallocate( Alloc& a, pointer p, size_type n );
```

Uses the allocator `a` to deallocate the storage referenced by `p`, by calling `a.deallocate(p, n)`.

## Parameters


### Parameters

- `a` - allocator to use
- `p` - pointer to the previously allocated storage
- `n` - the number of objects the storage was allocated for

## Return value

(none)

## Example

