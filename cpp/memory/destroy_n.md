---
title: std::destroy_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/destroy_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++17|constexpr=c++20|
template< class ForwardIt, class Size >
ForwardIt destroy_n( ForwardIt first, Size count );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class Size >
ForwardIt destroy_n( ExecutionPolicy&& policy, ForwardIt first, Size count );
```

1. Destroys the first `count` elements in the target range [first, last) as if by

```cpp
for (; count > 0; (void) ++first, --count)
    std::destroy_at(std::addressof(*first));
return first;
```

2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `first` - the beginning of the range of elements to destroy
- `count` - the number of elements to destroy
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

As described above.

## Exceptions

2.

## Example


## See also


| cpp/memory/dsc destroy | (see dedicated page) |
| cpp/memory/dsc destroy_at | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_n | (see dedicated page) |

