---
title: std::pmr::polymorphic_allocator::destroy
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/destroy
---

ddcl|since=c++17|deprecated=c++20|notes=|
template< class U >
void destroy( U* p );
Destroys the object pointed to by `p`, as if by calling `p->~U()`.

## Parameters


### Parameters

- `p` - pointer to the object being destroyed

## Notes

This function is deprecated via , because its functionality can be provided by the default implementation of `std::allocator_traits::destroy` and hence extraneous.
This function is undeprecated via .

## See also


| cpp/memory/allocator_traits/dsc destroy | (see dedicated page) |

