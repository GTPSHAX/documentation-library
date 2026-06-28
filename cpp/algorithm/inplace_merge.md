---
title: std::inplace_merge
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/inplace_merge
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++26|
template< class BidirIt >
void inplace_merge( BidirIt first, BidirIt middle, BidirIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class BidirIt >
void inplace_merge( ExecutionPolicy&& policy,
BidirIt first, BidirIt middle, BidirIt last );
dcla|num=3|constexpr=c++26|
template< class BidirIt, class Compare >
void inplace_merge( BidirIt first, BidirIt middle, BidirIt last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class BidirIt, class Compare >
void inplace_merge( ExecutionPolicy&& policy,
BidirIt first, BidirIt middle, BidirIt last,
Compare comp );
```

Merges two consecutive sorted ranges [first, middle) and [middle, last) into one sorted range [first, last).
1. If [first, middle) or [middle, last) is not `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, the behavior is undefined.
3. If [first, middle) or [middle, last) is not sorted with respect to `comp`, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@
This merge function is stable, which means that for equivalent elements in the original two ranges, the elements from the first range (preserving their original order) precede the elements from the second range (preserving their original order).
If any of the following conditions is satisfied, the behavior is undefined:
* [first, middle) or [middle, last) is not a valid range.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `BiditIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `first` - the beginning of the first sorted range
- `middle` - the end of the first sorted range and the beginning of the second
- `last` - the end of the second sorted range
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `BidirIt`
- `Compare`

## Complexity

Given  as `std::distance(first, last)`:
1. Exactly  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|} if enough additional memory is available,  comparisons otherwise.
2.  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Exactly  applications of the comparison function `comp` if enough additional memory is available,  applications otherwise.
4.  applications of the comparison function `comp`.

## Exceptions


## Possible implementation

See the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L2508 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L4452 libc++].

## Notes

This function attempts to allocate a temporary buffer. If the allocation fails, the less efficient algorithm is chosen.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

template<class Iter>
void merge_sort(Iter first, Iter last)
{
    if (last - first > 1)
    {
        Iter middle = first + (last - first) / 2;
        merge_sort(first, middle);
        merge_sort(middle, last);
        std::inplace_merge(first, middle, last);
    }
}

int main()
{
    std::vector<int> v{8, 2, -2, 0, 11, 11, 1, 7, 3};
    merge_sort(v.begin(), v.end());
    for (const auto& n : v)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
-2 0 1 2 3 7 8 11 11
```


## See also


| cpp/algorithm/dsc merge | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc inplace_merge | (see dedicated page) |

