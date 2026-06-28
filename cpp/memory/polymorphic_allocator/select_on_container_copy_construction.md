---
title: std::pmr::polymorphic_allocator:: select_on_container_copy_construction
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/select_on_container_copy_construction
---


```cpp
dcl | since=c++17 |
polymorphic_allocator select_on_container_copy_construction() const;
```

Returns a default-constructed `polymorphic_allocator` object.

## Parameters

(none)

## Return value

A default-constructed `polymorphic_allocator` object.

## Notes

`polymorphic_allocator`s do not propagate on container copy construction.

## See also

