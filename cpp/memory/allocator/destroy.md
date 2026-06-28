---
title: std::allocator::destroy
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/destroy
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|until=c++11|
void destroy( pointer p );
dcl|num=2|since=c++11|deprecated=c++17|removed=c++20|
template< class U >
void destroy( U* p );
```

Calls the destructor of the object pointed to by `p`.
1. Calls `p->~T()`.
2. Calls `p->~U()`.

## Parameters


### Parameters

- `p` - pointer to the object that is going to be destroyed

## Defect reports


## See also


| cpp/memory/allocator_traits/dsc destroy | (see dedicated page) |

