---
title: std::destroy
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/destroy
---


```cpp
**Header:** `<`memory`>`
dcl rev multi|num=1
|since1=c++17|dcl1=
template< class ForwardIt >
void destroy( ForwardIt first, ForwardIt last );
|since2=c++20|dcl2=
template< class ForwardIt >
constexpr void destroy( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
void destroy( ExecutionPolicy&& policy, ForwardIt first, ForwardIt last );
```

1. Destroys elements in the target range [first, last) as if by

```cpp
for (; first != last; ++first)
    std::destroy_at(std::addressof(*first));
```

2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Exceptions

2.

## Possible implementation

eq fun|1=
template<class ForwardIt>
constexpr // since C++20
void destroy(ForwardIt first, ForwardIt last)
{
for (; first != last; ++first)
std::destroy_at(std::addressof(*first));
}

## Example


## See also


| cpp/memory/dsc destroy_n | (see dedicated page) |
| cpp/memory/dsc destroy_at | (see dedicated page) |
| cpp/memory/ranges/dsc destroy | (see dedicated page) |

