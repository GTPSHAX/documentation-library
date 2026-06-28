---
title: std::piecewise_construct
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/piecewise_construct
---


```cpp
**Header:** `<`utility`>`
dcl|num=1|since=c++11|1=
struct piecewise_construct_t { explicit piecewise_construct_t() = default; };
|
constexpr std::piecewise_construct_t piecewise_construct{};
```

1. `std::piecewise_construct_t` is an empty class tag type used to disambiguate between different functions that take two tuple arguments.
2. The constant `std::piecewise_construct` is an instance of .
The overloads that do not use `std::piecewise_construct_t` assume that each tuple argument becomes the element of a pair. The overloads that use `std::piecewise_construct_t` assume that each tuple argument is used to construct, piecewise, a new object of specified type, which will become the element of the pair.

## Standard library

The following standard library types and functions use it as a disambiguation tag:


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/memory/dsc uses_allocator_construction_args | (see dedicated page) |
| cpp/ranges/dsc repeat_view | (see dedicated page) |


## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2510 | C++11 | the default constructor was non-explicit, which could lead to ambiguity | made explicit |


## See also

