---
title: std::ranges::destroy_at
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/ranges/destroy_at
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++20|
template< std::destructible T >
constexpr void destroy_at( T* p ) noexcept;
```

If `T` is not an array type, calls the destructor of the object pointed to by `p`, as if by `p->~T()`. Otherwise, recursively destroys elements of `*p` in order, as if by calling `std::destroy(std::begin(*p), std::end(*p))`.

## Parameters


### Parameters

- `p` - a pointer to the object to be destroyed

## Possible implementation

eq fun|1=
struct destroy_at_fn
{
template<std::destructible T>
constexpr void operator()(T *p) const noexcept
{
if constexpr (std::is_array_v<T>)
for (auto &elem : *p)
operator()(std::addressof(elem));
else
p->~T();
}
};
inline constexpr destroy_at_fn destroy_at{};

## Notes

`destroy_at` deduces the type of object to be destroyed and hence avoids writing it explicitly in the destructor call.
When `destroy_at` is called in the evaluation of some constant expression `e`, the argument `p` must point to an object whose lifetime began within the evaluation of `e`.

## Example


## See also


| cpp/memory/ranges/dsc destroy | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_n | (see dedicated page) |
| cpp/memory/ranges/dsc construct_at | (see dedicated page) |
| cpp/memory/dsc destroy_at | (see dedicated page) |

