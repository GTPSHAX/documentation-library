---
title: std::stable_partition
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/stable_partition
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++26|
template< class BidirIt, class UnaryPred >
BidirIt stable_partition( BidirIt first, BidirIt last, UnaryPred p );
dcl|since=c++17|num=2|
template< class ExecutionPolicy, class BidirIt, class UnaryPred >
BidirIt stable_partition( ExecutionPolicy&& policy,
BidirIt first, BidirIt last, UnaryPred p );
```

1. Reorders the elements in the range [first, last) in such a way that all elements for which the predicate `p` returns `true` precede the elements for which predicate `p` returns `false`. Relative order of the elements is preserved.
2. Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `BidirIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `BidirIt`
- `UnaryPred`

## Return value

Iterator to the first element of the second group.

## Complexity

Given  as `std::distance(first, last)`:
1. Exactly  applications of `p`.
@@  swaps if there is enough extra memory, otherwise at most } swaps.
2.  applications of `p`.
@@  swaps.

## Exceptions


## Notes

This function attempts to allocate a temporary buffer. If the allocation fails, the less efficient algorithm is chosen.
Implementations in [https://github.com/llvm/llvm-project/blob/eda14ebf6a43d9ada6a2be3d1b06b8b6036eb774/libcxx/include/__algorithm/stable_partition.h#L316 libc++] and [https://github.com/gcc-mirror/gcc/blob/d2a499a9881c7c079d2a722b57c7fcf022a864dd/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1608 libstdc++] also accept ranges denoted by *ForwardIterator*s as an extension.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{0, 0, 3, -1, 2, 4, 5, 0, 7};
    std::stable_partition(v.begin(), v.end(), [](int n) { return n > 0; });
    for (int n : v)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
3 2 4 5 7 0 0 -1 0
```


## Defect reports


## See also


| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_partition | (see dedicated page) |

