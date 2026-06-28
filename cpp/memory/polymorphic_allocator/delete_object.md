---
title: std::pmr::polymorphic_allocator::delete_object
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/delete_object
---

ddcl|since=c++20|
template< class U >
void delete_object( U* p );
Destroys the object of type `U` and deallocates storage allocated for it.
Equivalent to<br>
c|std::allocator_traits<polymorphic_allocator>::destroy(*this, p);
deallocate_object(p);

## Parameters


### Parameters

- `p` - pointer to the object to destroy and deallocate

## Exceptions

Throws nothing.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization.

## See also


| cpp/memory/polymorphic_allocator/dsc deallocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc deallocate_object | (see dedicated page) |
| cpp/memory/allocator traits/dsc deallocate | (see dedicated page) |
| cpp/memory/memory resource/dsc deallocate | (see dedicated page) |

