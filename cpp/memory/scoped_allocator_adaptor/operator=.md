---
title: std::scoped_allocator_adaptor::operator=
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/operator=
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|num=1|1=
scoped_allocator_adaptor& operator=( const scoped_allocator_adaptor& other ) = default;
dcl|num=2|1=
scoped_allocator_adaptor& operator=( scoped_allocator_adaptor&& other ) = default;
```

1. Explicitly defaulted copy assignment operator that copy assigns the base class (`OuterAlloc`, the outer allocator) and all inner allocators.
2. Explicitly defaulted move assignment operator that move assigns the base class (`OuterAlloc`, the outer allocator) and all inner allocators.

## Parameters


### Parameters

- `other` - another `std::scoped_allocator_adaptor`
