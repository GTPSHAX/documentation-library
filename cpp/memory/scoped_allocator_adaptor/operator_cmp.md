---
title: operators (std::scoped_allocator_adaptor)
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/operator_cmp
---


# 1=operator==,!=small|(std::scoped_allocator_adaptor)


```cpp
**Header:** `<`scoped_allocator`>`
dcl|since=c++11|1=
template< class OuterAlloc1, class OuterAlloc2, class... InnerAllocs >
bool operator==( const scoped_allocator_adaptor<OuterAlloc1, InnerAllocs...>& lhs,
const scoped_allocator_adaptor<OuterAlloc2, InnerAllocs...>& rhs ) noexcept;
dcl|since=c++11|until=c++20|1=
template< class OuterAlloc1, class OuterAlloc2, class... InnerAllocs >
bool operator!=( const scoped_allocator_adaptor<OuterAlloc1, InnerAllocs...>& lhs,
const scoped_allocator_adaptor<OuterAlloc2, InnerAllocs...>& rhs ) noexcept;
```

Compares two scoped allocator adaptors. Two such allocators are equal if:
* `lhs.outer_allocator() , and
* if `sizeof...(InnerAllocs) > 0`, `lhs.inner_allocator() .
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - scoped allocator adaptors to compare

## Return value

1. Returns `true` if `lhs` and `rhs` are equal, `false` otherwise.
2. Returns `true` if `lhs` and `rhs` are not equal, `false` otherwise.
