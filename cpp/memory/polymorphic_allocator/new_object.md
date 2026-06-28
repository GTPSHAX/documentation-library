---
title: std::pmr::polymorphic_allocator::new_object
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/new_object
---

ddcl|since=c++20|
template< class U, class... CtorArgs >
U* new_object( CtorArgs&&... ctor_args );
Allocates and constructs an object of type `U`.
Given `alloc` is a `std::pmr::polymorphic_allocator<T>`:

```cpp
U* p = alloc.new_object<U>(std::forward<CtorArgs>(ctor_args)...);
```

is equivalent to

```cpp
U* p = alloc.allocate_object<U>();
try
{
    alloc.construct(p, std::forward<CtorArgs>(ctor_args)...);
}
catch (...)
{
    alloc.deallocate_object(p);
    throw;
}
```


## Parameters


### Parameters

- `ctor_args` - the arguments to forward to the constructor of `U`

## Return value

A pointer to the allocated and constructed object.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization as a shortcut to avoid having to rebind from `std::pmr::polymorphic_allocator<T>` to `std::pmr::polymorphic_allocator<U>`, and having to call `allocate`, `construct`, and `deallocate` individually.
Since `U` is not deduced, it must be provided as a template argument when calling this function.

## Exceptions

May throw any exceptions thrown by the call to `allocate_object` or the constructor of `U`.

## See also


| cpp/memory/polymorphic_allocator/dsc allocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator traits/dsc allocate | (see dedicated page) |
| cpp/memory/memory resource/dsc allocate | (see dedicated page) |

