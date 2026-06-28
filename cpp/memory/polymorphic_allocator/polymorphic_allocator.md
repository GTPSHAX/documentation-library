---
title: std::pmr::polymorphic_allocator::polymorphic_allocator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/polymorphic_allocator
---


```cpp
dcl|num=1|1=
polymorphic_allocator() noexcept;
dcl|num=2|1=
polymorphic_allocator( const polymorphic_allocator& other ) = default;
dcl|num=3|1=
template< class U >
polymorphic_allocator( const polymorphic_allocator<U>& other ) noexcept;
dcl|num=4|1=
polymorphic_allocator( std::pmr::memory_resource* r );
```

Constructs a new `polymorphic_allocator`.
1. Constructs a `polymorphic_allocator` using the return value of `std::pmr::get_default_resource()` as the underlying memory resource.
@2,3@ Constructs a `polymorphic_allocator` using `other.resource()` as the underlying memory resource.
4. Constructs a `polymorphic_allocator` using `r` as the underlying memory resource. This constructor provides an implicit conversion from `std::pmr::memory_resource*`.

## Parameters


### Parameters

- `other` - another `polymorphic_allocator` to copy from
- `r` - pointer to the memory resource to use. May not be null

## Exceptions

4. Throws nothing.

## Notes

Copying a container using a `polymorphic_allocator` will not call the allocator's copy constructor. Instead, the new container will use the return value of ``select_on_container_copy_construction`` (a default-constructed `polymorphic_allocator`) as its allocator.

## See also


| cpp/memory/polymorphic_allocator/dsc select_on_container_copy_construction | (see dedicated page) |

