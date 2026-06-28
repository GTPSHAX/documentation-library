---
title: std::scoped_allocator_adaptor::outer_allocator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/outer_allocator
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl | num=1 | since=c++11 |
outer_allocator_type& outer_allocator() noexcept;
dcl | num=2 | since=c++11 |
const outer_allocator_type& outer_allocator() const noexcept;
```

Obtains a reference to the outer allocator used to declare this class.
1. Returns `static_cast<OuterAlloc&>(*this)`.
2. Returns `static_cast<const OuterAlloc&>(*this)`.

## Parameters

(none)

## Return value

A reference to `OuterAlloc`.

## See also

