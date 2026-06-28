---
title: std::destroy_at
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/destroy_at
---


```cpp
**Header:** `<`memory`>`
dcl rev multi
|since1=c++17|dcl1=
template< class T >
void destroy_at( T* p );
|since2=c++20|dcl2=
template< class T >
constexpr void destroy_at( T* p );
```

If `T` is not an array type, calls the destructor of the object pointed to by `p`, as if by `p->~T()`.
If `T` is an array type, <sup>(until C++20)</sup> the program is ill-formed<sup>(since C++20)</sup> recursively destroys elements of `*p` in order, as if by calling `std::destroy(std::begin(*p), std::end(*p))`.

## Parameters


### Parameters

- `p` - a pointer to the object to be destroyed

## Possible implementation

eq fun|1=
template<class T>
constexpr void destroy_at(T* p)
{
if constexpr (std::is_array_v<T>)
for (auto &elem : *p)
(destroy_at)(std::addressof(elem));
else
p->~T();
}
// C++17 version:
// template<class T> void destroy_at(T* p) { p->~T(); }

## Notes

`destroy_at` deduces the type of object to be destroyed and hence avoids writing it explicitly in the destructor call.
rrev|since=c++20|
When `destroy_at` is called in the evaluation of some constant expression `e`, the argument `p` must point to an object whose lifetime began within the evaluation of `e`.

## Example


## See also


| cpp/memory/dsc destroy | (see dedicated page) |
| cpp/memory/dsc destroy_n | (see dedicated page) |
| cpp/memory/dsc construct_at | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_at | (see dedicated page) |

