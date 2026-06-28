---
title: std::scoped_allocator_adaptor::scoped_allocator_adaptor
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/scoped_allocator_adaptor
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|num=1|since=c++11|
scoped_allocator_adaptor();
dcl|num=2|since=c++11|
template< class OuterA2 >
scoped_allocator_adaptor(
OuterA2&& outerAlloc, const InnerAllocs&... innerAllocs
) noexcept;
dcl|num=3|since=c++11|
scoped_allocator_adaptor(
const scoped_allocator_adaptor& other
) noexcept;
dcl|num=4|since=c++11|
scoped_allocator_adaptor(
scoped_allocator_adaptor&& other
) noexcept;
dcl|num=5|since=c++11|
template< class OuterA2 >
scoped_allocator_adaptor(
const scoped_allocator_adaptor<OuterA2, InnerAllocs...>& other
) noexcept;
dcl|num=6|since=c++11|
template< class OuterA2 >
scoped_allocator_adaptor(
scoped_allocator_adaptor<OuterA2, InnerAllocs...>&& other
) noexcept;
```

1. Default constructor: value-initializes the `OuterAlloc` base class and the inner allocator member object, if used by the implementation.
2. Constructs the base class `OuterAlloc` from `std::forward<OuterA2>(outerAlloc)`, and the inner allocators with `innerAllocs...`. .
3. Copy-constructor: initializes each allocator from the corresponding allocator of `other`.
4. Move-constructor: moves each allocator from the corresponding allocator of `other` into `*this`.
5. Initializes each allocator from the corresponding allocator of `other`. .
6. Initializes each allocator from the corresponding allocator of `other`, using move semantics. .

## Parameters


### Parameters

- `outerAlloc` - constructor argument for the outer allocator
- `innerAllocs...` - constructor arguments for the inner allocators
- `other` - another `std::scoped_allocator_adaptor`

## Defect reports


## See also


| cpp/memory/scoped_allocator_adaptor/dsc allocate | (see dedicated page) |
| cpp/memory/scoped_allocator_adaptor/dsc construct | (see dedicated page) |

