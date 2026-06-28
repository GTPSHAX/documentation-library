---
title: std::is_sorted_until
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/is_sorted_until
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt >
ForwardIt is_sorted_until( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
ForwardIt is_sorted_until( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcla|num=3|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt, class Compare >
ForwardIt is_sorted_until( ForwardIt first, ForwardIt last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class Compare >
ForwardIt is_sorted_until( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
Compare comp );
```

Examines the range [first, last) and finds the largest range beginning at `first` in which the elements are sorted in non-descending order.
1. Finds the largest range whether elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Finds the largest range whether elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `ForwardIt`
- `Compare`

## Return value

The upper bound of the largest range beginning at `first` in which the elements are sorted in ascending order. That is, the last iterator `it` for which range [first, it) is sorted.
Returns `last` for empty ranges and ranges of length one.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@  applications of the comparator `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L3211 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L3614 libc++].
eq impl
|title1=is_sorted_until (1)|ver1=1|1=
template<class ForwardIt>
constexpr //< since C++20
ForwardIt is_sorted_until(ForwardIt first, ForwardIt last)
{
return std::is_sorted_until(first, last, std::less<>());
}
|title2=is_sorted_until (2)|ver2=3|2=
template<class ForwardIt, class Compare>
constexpr //< since C++20
ForwardIt is_sorted_until(ForwardIt first, ForwardIt last, Compare comp)
{
if (first != last)
{
ForwardIt next = first;
while (++next != last)
{
if (comp(*next, *first))
return next;
first = next;
}
}
return last;
}

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <random>
#include <string>

int main()
{
    std::random_device rd;
    std::mt19937 g(rd());
    const int N = 6;
    int nums[N] = {3, 1, 4, 1, 5, 9};

    const int min_sorted_size = 4;

    for (int sorted_size = 0; sorted_size < min_sorted_size;)
    {
        std::shuffle(nums, nums + N, g);
        int *const sorted_end = std::is_sorted_until(nums, nums + N);
        sorted_size = std::distance(nums, sorted_end);
        assert(sorted_size >= 1);

        for (const auto i : nums)
            std::cout << i << ' ';
        std::cout << ": " << sorted_size << " initial sorted elements\n"
                  << std::string(sorted_size * 2 - 1, '^') << '\n';
    }
}
```


**Output:**
```
4 1 9 5 1 3 : 1 initial sorted elements
^
4 5 9 3 1 1 : 3 initial sorted elements
^^^^^
9 3 1 4 5 1 : 1 initial sorted elements
^
1 3 5 4 1 9 : 3 initial sorted elements
^^^^^
5 9 1 1 3 4 : 2 initial sorted elements
^^^
4 9 1 5 1 3 : 2 initial sorted elements
^^^
1 1 4 9 5 3 : 4 initial sorted elements
^^^^^^^
```


## See also


| cpp/algorithm/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_sorted_until | (see dedicated page) |

