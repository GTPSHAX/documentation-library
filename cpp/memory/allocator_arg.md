---
title: std::allocator_arg
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/allocator_arg
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|since=c++11|1=
struct allocator_arg_t { explicit allocator_arg_t() = default; };
|1=
constexpr std::allocator_arg_t allocator_arg {};
```

1. `std::allocator_arg_t` is an empty class type used to disambiguate the overloads of constructors and member functions of allocator-aware objects, including `std::tuple`<sup>(until C++17)</sup> , `std::function`, `std::packaged_task`, and `std::promise`.
2. `std::allocator_arg` is an instance of  that can be passed to the constructors and member functions of such permitted types.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2510 | C++11 | the default constructor was non-explicit, which could lead to ambiguity | made explicit |


## See also


| cpp/memory/dsc uses_allocator | (see dedicated page) |

