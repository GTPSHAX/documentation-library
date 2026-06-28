---
title: std::partial_sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partial_sort
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class RandomIt >
void partial_sort( RandomIt first, RandomIt middle, RandomIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class RandomIt >
void partial_sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt middle, RandomIt last );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class RandomIt, class Compare >
void partial_sort( RandomIt first, RandomIt middle, RandomIt last,
Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class RandomIt, class Compare >
void partial_sort( ExecutionPolicy&& policy,
RandomIt first, RandomIt middle, RandomIt last,
Compare comp );
```

Rearranges elements such that the range [first, middle) contains the sorted `middle − first` smallest elements in the range [first, last).
The order of equal elements is not guaranteed to be preserved. The order of the remaining elements in the range [middle, last) is unspecified.
1. Elements are `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are sorted with respect to `comp`.
@2,4@ Same as , but executed according to `policy`.
@@
If any of the following conditions is satisfied, the behavior is undefined:
* [first, middle) or [middle, last) is not a valid range.
rev|until=c++11|
* The type of `*first` is not *Swappable*.
rev|since=c++11|
* `RandomIt` is not *ValueSwappable*.
* The type of `*first` is not *MoveConstructible*.
* The type of `*first` is not *MoveAssignable*.

## Parameters


### Parameters

- `middle` - the range [first, middle) will contain sorted elements
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `RandomIt`
- `Compare`

## Complexity

Given  as `middle - first`,  as `last - first`:
@1,2@ Approximately  comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ Approximately  applications of the comparator `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1915 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L5025 libc++].
eq impl
|title1=partial_sort (1)|ver1=1|1=
template<typename RandomIt>
constexpr //< since C++20
void partial_sort(RandomIt first, RandomIt middle, RandomIt last)
{
typedef typename std::iterator_traits<RandomIt>::value_type VT;
std::partial_sort(first, middle, last, std::less<VT>());
}
|title2=partial_sort (3)|ver2=3|2=
namespace impl
{
template<typename RandomIt, typename Compare>
constexpr //< since C++20
void sift_down(RandomIt first, RandomIt last, const Compare& comp)
{
// sift down element at “first”
const auto length = static_cast<std::size_t>(last - first);
std::size_t current = 0;
std::size_t next = 2;
while (next < length)
{
if (comp(*(first + next), *(first + (next - 1))))
--next;
if (!comp(*(first + current), *(first + next)))
return;
std::iter_swap(first + current, first + next);
current = next;
next = 2 * current + 2;
}
--next;
if (next < length && comp(*(first + current), *(first + next)))
std::iter_swap(first + current, first + next);
}
template<typename RandomIt, typename Compare>
constexpr //< since C++20
void heap_select(RandomIt first, RandomIt middle, RandomIt last, const Compare& comp)
{
std::make_heap(first, middle, comp);
for (auto i = middle; i != last; ++i)
{
if (comp(*i, *first))
{
std::iter_swap(first, i);
sift_down(first, middle, comp);
}
}
}
} // namespace impl
template<typename RandomIt, typename Compare>
constexpr //< since C++20
void partial_sort(RandomIt first, RandomIt middle, RandomIt last, Compare comp)
{
impl::heap_select(first, middle, last, comp);
std::sort_heap(first, middle, comp);
}

## Notes


### Algorithm

The algorithm used is typically ''heap select'' to select the smallest elements, and ''heap sort'' to sort the selected elements in the heap in ascending order.
To select elements, a heap is used (see [Heap (data structure)#Applications|heap](https://en.wikipedia.org/wiki/Heap (data structure)#Applications|heap)). For example, for `operator<` as comparison function, ''max-heap'' is used to select `middle − first` smallest elements.
[Heapsort|Heap sort](https://en.wikipedia.org/wiki/Heapsort|Heap sort) is used after selection to sort [first, middle) selected elements (see `std::sort_heap`).

### Intended use

`std::partial_sort` algorithms are intended to be used for ''small constant numbers'' of [first, middle) selected elements.

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <iostream>

void print(const auto& s, int middle)
{
    for (int a : s)
        std::cout << a << ' ';
    std::cout << '\n';
    if (middle > 0)
    {
        while (middle-- > 0)
            std::cout << "--";
        std::cout << '^';
    }
    else if (middle < 0)
    {
        for (auto i = s.size() + middle; --i; std::cout << "  ")
        {}

        for (std::cout << '^'; middle++ < 0; std::cout << "--")
        {}
    }
    std::cout << '\n';
};

int main()
{
    std::array<int, 10> s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    print(s, 0);
    std::partial_sort(s.begin(), s.begin() + 3, s.end());
    print(s, 3);
    std::partial_sort(s.rbegin(), s.rbegin() + 4, s.rend());
    print(s, -4);
    std::partial_sort(s.rbegin(), s.rbegin() + 5, s.rend(), std::greater{});
    print(s, -5);
}
```


**Output:**
```
5 7 4 2 8 6 1 9 0 3

0 1 2 7 8 6 5 9 4 3
------^
4 5 6 7 8 9 3 2 1 0
          ^--------
4 3 2 1 0 5 6 7 8 9
        ^----------
```


## Defect reports


## See also


| cpp/algorithm/dsc nth_element | (see dedicated page) |
| cpp/algorithm/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |

