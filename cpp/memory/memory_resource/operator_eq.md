---
title: std::pmr::operators (std::pmr::operator!=)
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/operator_eq
---


```cpp
**Header:** `<`memory_resource`>`
dcl|since=c++17|num=1|1=
bool operator==( const std::pmr::memory_resource& a,
const std::pmr::memory_resource& b ) noexcept;
dcl|since=c++17|until=c++20|num=2|1=
bool operator!=( const std::pmr::memory_resource& a,
const std::pmr::memory_resource& b ) noexcept;
```

Compares the `memory_resource`s `a` and `b` for equality. Two `memory_resource`s compare equal if and only if memory allocated from one `memory_resource` can be deallocated from the other and vice versa.
rrev|since=c++20|

## Return value

1. `1=&a == &b
2. `1=!(a == b)`

## See also


| cpp/memory/memory_resource/dsc is_equal | (see dedicated page) |

