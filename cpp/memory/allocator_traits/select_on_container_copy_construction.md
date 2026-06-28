---
title: std::allocator_traits::select_on_container_copy_construction
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/select_on_container_copy_construction
---


```cpp
**Header:** `<`memory`>`
dcla|since=c++11|constexpr=c++20|
static Alloc select_on_container_copy_construction( const Alloc& a );
```

If possible, obtains the copy-constructed version of the allocator `a`, by calling `a.select_on_container_copy_construction()`. If the above is not possible (e.g. `Alloc` does not have the member function `select_on_container_copy_construction()`), then returns `a`, unmodified.
This function is called by the copy constructors of all standard library containers. It allows the allocator used by the constructor's argument to become aware that the container is being copied and modify state if necessary.

## Parameters


### Parameters

- `a` - allocator used by a standard container passed as an argument to a container copy constructor

## Return value

The allocator to use by the copy-constructed standard containers.

## See also


| cpp/memory/scoped_allocator_adaptor/dsc select_on_container_copy_construction | (see dedicated page) |

