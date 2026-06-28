---
title: std::sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/sort
---


```cpp
**Header:** `<`algorithm`>`
|
template< class RandomIt >
void sort( RandomIt first, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
void sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt last );
|
template< class RandomIt, class Compare >
void sort( RandomIt first, RandomIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
void sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt last, Compare comp );
```

Sorts the elements in the range [first, last) in non-descending order. The order of equal elements is not guaranteed to be preserved.
1. Elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `last - first`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@  applications of the comparator `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1950 libstdc++] and [https://github.com/llvm/llvm-project/blob/e7fc254875ca9e82b899d5354fae9b5b779ff485/libcxx/include/__algorithm/sort.h#L264 libc++].

## Notes

Before `LWG713`, the complexity requirement allowed `sort()` to be implemented using only [Quicksort](https://en.wikipedia.org/wiki/Quicksort), which may need ) comparisons in the worst case.
[Introsort](https://en.wikipedia.org/wiki/Introsort) can handle all cases with  comparisons (without incurring additional overhead in the average case), and thus is usually used for implementing `sort()`.
libc++ has not implemented the corrected time complexity requirement [https://reviews.llvm.org/D113413 until LLVM 14].

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <string_view>

int main()
{
    std::array<int, 10> s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};

    auto print = [&s](std::string_view const rem)
    {
        for (auto a : s)
            std::cout << a << ' ';
        std::cout << ": " << rem << '\n';
    };

    std::sort(s.begin(), s.end());
    print("sorted with the default operator<");

    std::sort(s.begin(), s.end(), std::greater<int>());
    print("sorted with the standard library compare function object");

    struct
    {
        bool operator()(int a, int b) const { return a < b; }
    }
    customLess;

    std::sort(s.begin(), s.end(), customLess);
    print("sorted with a custom function object");

    std::sort(s.begin(), s.end(), [](int a, int b)
                                  {
                                      return a > b;
                                  });
    print("sorted with a lambda expression");
}
```


**Output:**
```
0 1 2 3 4 5 6 7 8 9 : sorted with the default operator<
9 8 7 6 5 4 3 2 1 0 : sorted with the standard library compare function object
0 1 2 3 4 5 6 7 8 9 : sorted with a custom function object
9 8 7 6 5 4 3 2 1 0 : sorted with a lambda expression
```


## Defect reports


## See also


| cpp/algorithm/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort | (see dedicated page) |

