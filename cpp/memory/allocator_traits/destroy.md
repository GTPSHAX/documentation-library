---
title: std::allocator_traits::destroy
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/destroy
---


```cpp
**Header:** `<`memory`>`
dcla|since=c++11|constexpr=c++20|
template< class T >
static void destroy( Alloc& a, T* p );
```

Calls the destructor of the object pointed to by `p`. If possible, does so by calling `a.destroy(p)`. If not possible (e.g. `Alloc` does not have the member function `destroy()`), then calls <sup>(until C++20)</sup> the destructor of `*p` directly, as `p->~T()`<sup>(since C++20)</sup> `std::destroy_at(p)`.

## Parameters


### Parameters

- `a` - allocator to use for destruction
- `p` - pointer to the object being destroyed

## Return value

(none)

## Notes

Because this function provides the automatic fall back to direct call to the destructor, the member function `destroy()` is an optional *Allocator* requirement since C++11.

## Example

