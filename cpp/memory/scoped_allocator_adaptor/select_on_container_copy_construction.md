---
title: std::scoped_allocator_adaptor:: select_on_container_copy_construction
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/select_on_container_copy_construction
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl | since=c++11 |
scoped_allocator_adaptor select_on_container_copy_construction() const;
```

Creates a new instance of `std::scoped_allocator_adaptor`, where the outer allocator base class and each inner allocator subobject are obtained by calling `std::allocator_traits<A>::select_on_container_copy_construction()`.

## Parameters

(none)

## Return value

A new `std::scoped_allocator_adaptor` object, constructed from correctly copied allocators.

## See also

