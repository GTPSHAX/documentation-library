---
title: deduction guides for std::scoped_allocator_adaptor
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/deduction_guides
---


# deduction guides for tt|std::scoped_allocator_adaptor


```cpp
**Header:** `<`scoped_allocator`>`
dcl|since=c++17|
template< class OuterAlloc, class... InnerAllocs >
scoped_allocator_adaptor( OuterAlloc, InnerAllocs... )
-> scoped_allocator_adaptor<OuterAlloc, InnerAllocs...>;
```

One deduction guide is provided for `std::scoped_allocator_adaptor` to make it possible to deduce its outer allocator.

## Example

