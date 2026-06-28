---
title: std::merge
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/merge
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class OutputIt >
OutputIt merge( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class ForwardIt3 >
ForwardIt3 merge( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class Compare >
OutputIt merge( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class Compare >
ForwardIt3 merge( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first, Compare comp );
```

Merges two sorted ranges [first1, last1) and [first2, last2) into one sorted range beginning at `d_first`.
1. If [first1, last1) or [first2, last2) is not `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, the behavior is undefined.
3. If [first1, last1) or [first2, last2) is not sorted with respect to `comp`, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@
This merge function is stable, which means that for equivalent elements in the original two ranges, the elements from the first range (preserving their original order) precede the elements from the second range (preserving their original order).
If the output range overlaps with [first1, last1) or [first2, last2), the behavior is undefined.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `d_first` - the beginning of the destination range
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `InputIt1, InputIt2`
- `ForwardIt1, ForwardIt2, ForwardIt3`
- `OutputIt`
- `Compare`

## Return value

An output iterator to element past the last element copied.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
1. At most +N-1 comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. +N) comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. At most +N-1 applications of the comparison function `comp`.
4. +N) applications of the comparison function `comp`.

## Exceptions


## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L4856 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L4348 libc++].
eq impl
|title1=merge (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt merge(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first)
{
for (; first1 != last1; ++d_first)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (*first2 < *first1)
{
*d_first = *first2;
++first2;
}
else
{
*d_first = *first1;
++first1;
}
}
return std::copy(first2, last2, d_first);
}
|title2=merge (3)|ver2=3|2=
template<class InputIt1, class InputIt2,
class OutputIt, class Compare>
OutputIt merge(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp)
{
for (; first1 != last1; ++d_first)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (comp(*first2, *first1))
{
*d_first = *first2;
++first2;
}
else
{
*d_first = *first1;
++first1;
}
}
return std::copy(first2, last2, d_first);
}

## Notes

This algorithm performs a similar task as `std::set_union` does. Both consume two sorted input ranges and produce a sorted output with elements from both inputs. The difference between these two algorithms is with handling values from both input ranges which compare equivalent (see notes on *LessThanComparable*). If any equivalent values appeared `n` times in the first range and `m` times in the second, `std::merge` would output all `n + m` occurrences whereas `std::set_union` would output `std::max(n, m)` ones only. So `std::merge` outputs exactly `std::distance(first1, last1) + std::distance(first2, last2)` values and `std::set_union` may produce fewer.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <random>
#include <vector>

auto print = [](const auto rem, const auto& v)
{
    std::cout << rem;
    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
};

int main()
{
    // fill the vectors with random numbers
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<> dis(0, 9);

    std::vector<int> v1(10), v2(10);
    std::generate(v1.begin(), v1.end(), std::bind(dis, std::ref(mt)));
    std::generate(v2.begin(), v2.end(), std::bind(dis, std::ref(mt)));

    print("Originally:\nv1: ", v1);
    print("v2: ", v2);

    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());

    print("After sorting:\nv1: ", v1);
    print("v2: ", v2);

    // merge
    std::vector<int> dst;
    std::merge(v1.begin(), v1.end(), v2.begin(), v2.end(), std::back_inserter(dst));

    print("After merging:\ndst: ", dst);
}
```


**Output:**
```
Originally:
v1: 2 6 5 7 4 2 2 6 7 0
v2: 8 3 2 5 0 1 9 6 5 0
After sorting:
v1: 0 2 2 2 4 5 6 6 7 7
v2: 0 0 1 2 3 5 5 6 8 9
After merging:
dst: 0 0 0 1 2 2 2 2 3 4 5 5 5 6 6 6 7 7 8 9
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-780 | C++98 | the merge operation was not defined | defined |


## See also


| cpp/algorithm/dsc inplace_merge | (see dedicated page) |
| cpp/algorithm/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/dsc set_union | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc merge | (see dedicated page) |

