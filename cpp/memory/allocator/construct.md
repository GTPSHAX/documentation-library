---
title: std::allocator::construct
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/construct
---


```cpp
**Header:** `<`memory`>`
dcl|num=1|until=c++11|
void construct( pointer p, const_reference val );
dcl|num=2|since=c++11|deprecated=c++17|removed=c++20|
template< class U, class... Args >
void construct( U* p, Args&&... args );
```

Constructs an object of type `T` in allocated uninitialized storage pointed to by `p`, using global placement-new.
1. Calls `::new((void*)p) T(val)`.
2. Calls `::new((void*)p) U(std::forward<Args>(args)...)`.

## Parameters


### Parameters

- `p` - pointer to allocated uninitialized storage
- `val` - the value to use as the copy constructor argument
- `args...` - the constructor arguments to use

## Defect reports


## See also


| cpp/memory/allocator_traits/dsc construct | (see dedicated page) |
| cpp/memory/dsc construct_at | (see dedicated page) |
| cpp/memory/new/dsc operator_new | (see dedicated page) |

