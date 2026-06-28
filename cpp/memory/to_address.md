---
title: std::to_address
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/to_address
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|since=c++20|1=
template< class Ptr >
constexpr auto to_address( const Ptr& p ) noexcept;
dcl|num=2|since=c++20|1=
template< class T >
constexpr T* to_address( T* p ) noexcept;
```

Obtain the address represented by `p` without forming a reference to the object pointed to by `p`.
1. Fancy pointer overload: If the expression `std::pointer_traits<Ptr>::to_address(p)` is well-formed, returns the result of that expression. Otherwise, returns `std::to_address(p.operator->())`.
2. Raw pointer overload: If `T` is a function type, the program is ill-formed. Otherwise, returns `p` unmodified.

## Parameters


### Parameters

- `p` - fancy or raw pointer

## Return value

Raw pointer that represents the same address as `p` does.

## Possible implementation

eq fun|1=
template<class T>
constexpr T* to_address(T* p) noexcept
{
static_assert(!std::is_function_v<T>);
return p;
}
template<class T>
constexpr auto to_address(const T& p) noexcept
{
if constexpr (requires{ std::pointer_traits<T>::to_address(p); })
return std::pointer_traits<T>::to_address(p);
else
return std::to_address(p.operator->());
}

## Notes

`std::to_address` can be used even when `p` does not reference storage that has an object constructed in it, in which case `std::addressof(*p)` cannot be used because there is no valid object for the parameter of `std::addressof` to bind to.
The fancy pointer overload of `std::to_address` inspects the `std::pointer_traits<Ptr>` specialization. If instantiating that specialization is itself ill-formed (typically because `element_type` cannot be defined), that results in a hard error outside the immediate context and renders the program ill-formed.
`std::to_address` may additionally be used on iterators that satisfy `std::contiguous_iterator`.

## Example


## See also


| cpp/memory/dsc pointer_traits | (see dedicated page) |
| cpp/memory/pointer_traits/dsc to_address | (see dedicated page) |

