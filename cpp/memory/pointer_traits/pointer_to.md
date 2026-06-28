---
title: std::pointer_traits::pointer_to
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/pointer_traits/pointer_to
---


```cpp
**Header:** `<`memory`>`
specialization|
static pointer
pointer_to( element_type& r );
dcl rev multi|num=2
|since1=c++11|dcl1=
static pointer
pointer_to( element_type& r ) noexcept;
|notes1=
|since2=c++20|dcl2=
static constexpr pointer
pointer_to( element_type& r ) noexcept;
|notes2=
```

Constructs a dereferenceable pointer or pointer-like object ("fancy pointer") to its argument.
1. The version of this function in the non-specialized `std::pointer_traits` template simply calls `Ptr::pointer_to(r)`, and if Ptr does not provide a static member function `pointer_to`, instantiation of this function is a compile-time error.
2. The version of this function in the specialization of `std::pointer_traits` for pointer types returns `std::addressof(r)`.

## Parameters


### Parameters

- `r` - reference to an object of type `element_type&`, except if element_type is `void`, in which case the type of `r` is unspecified

## Return value

A dereferenceable pointer to `r`, of the type `pointer_traits<>::pointer`.

## Exceptions

1. Unspecified (typically same as `Ptr::pointer_to`).

## Notes

The [https://www.boost.org/doc/libs/release/doc/html/boost/intrusive/pointer_traits.html Boost.Intrusive library version] of this function returns `pointer(std::addressof(r))` if `Ptr::pointer_to` does not exist.

## See also


| cpp/memory/dsc addressof | (see dedicated page) |
| cpp/memory/allocator/dsc address | (see dedicated page) |
| cpp/memory/pointer_traits/dsc to_address | (see dedicated page) |
| cpp/memory/dsc to_address | (see dedicated page) |

