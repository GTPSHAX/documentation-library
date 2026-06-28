---
title: std::scoped_allocator_adaptor::inner_allocator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/inner_allocator
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl | num=1 | since=c++11 |
inner_allocator_type& inner_allocator() noexcept;
dcl | num=2 | since=c++11 |
const inner_allocator_type& inner_allocator() const noexcept;
```

Obtains a reference to the inner allocator used to declare this `scoped_allocator_adaptor`.
If `1=sizeof...(InnerAllocs) == 0`, that is, no inner allocators were declared, returns `*this`. Otherwise returns a reference to `std::scoped_allocator_adaptor<InnerAllocs...>`, that is, a scoped allocator composed of all inner allocators of `*this`, with the first inner allocator becoming the outer allocator.

## Parameters

(none)

## Return value

A reference to the inner allocator, which is itself a `std::scoped_allocator_adaptor`.

## See also

