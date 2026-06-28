---
title: std::lower_bound
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/lower_bound
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
ForwardIt lower_bound( ForwardIt first, ForwardIt last,
const T& value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr ForwardIt lower_bound( ForwardIt first, ForwardIt last,
const T& value );
dcl rev multi|num=2|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T, class Compare >
ForwardIt lower_bound( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type,
class Compare >
constexpr ForwardIt lower_bound( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
```

Searches for the first element in the partitioned range [first, last) which is '''not''' ordered before `value`.
1. The order is determined by `operator<`:
rev|until=c++20|
Returns the first iterator `iter` in [first, last) where `bool(*iter < value)` is `false`, or `last` if no such `iter` exists.
If the elements `elem` of [first, last) are not `partitioned` with respect to the expression `bool(elem < value)`, the behavior is undefined.
rev|since=c++20|
Equivalent to }.
2. The order is determined by `comp`:
@@ Returns the first iterator `iter` in [first, last) where `bool(comp(*iter, value))` is `false`, or `last` if no such `iter` exists.
@@ If the elements `elem` of [first, last) are not `partitioned` with respect to the expression `bool(comp(elem, value))`, the behavior is undefined.

## Parameters


### Parameters

- `[3=to examine, range=partitioned}})` - 
- `value` - value to compare the elements to

**Type requirements:**

- `ForwardIt`
- `Compare`

## Return value

Iterator to the first element of the range [first, last) not ordered before `value`, or `last` if no such element is found.

## Complexity

Given  as `std::distance(first, last)`:
1. At most } comparisons with `value` using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most } applications of the comparator `comp`.
However, if `ForwardIt` is not a *RandomAccessIterator*, the number of iterator increments is linear in . Notably, `std::map`, `std::multimap`, `std::set`, and `std::multiset` iterators are not random access, and so their member `lower_bound` functions should be preferred.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algobase.h#L1023 libstdc++] and [https://github.com/llvm/llvm-project/blob/8350d9c23d76fb95f42674a1563cbe8c32582dd5/libcxx/include/__algorithm/lower_bound.h#L32 libc++].
eq impl
|title1=lower_bound (1)|ver1=1|1=
template<class ForwardIt, class T = typename std::iterator_traits<ForwardIt>::value_type>
ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T& value)
{
return std::lower_bound(first, last, value, std::less{});
}
|title2=lower_bound (2)|ver2=2|2=
template<class ForwardIt, class T = typename std::iterator_traits<ForwardIt>::value_type,
class Compare>
ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T& value, Compare comp)
{
ForwardIt it;
typename std::iterator_traits<ForwardIt>::difference_type count, step;
count = std::distance(first, last);
while (count > 0)
{
it = first;
step = count / 2;
std::advance(it, step);
if (comp(*it, value))
{
first = ++it;
count -= step + 1;
}
else
count = step;
}
return first;
}

## Notes

Although `std::lower_bound` only requires [first, last) to be partitioned, this algorithm is usually used in the case where [first, last) is sorted, so that the binary search is valid for any `value`.
Unlike `std::binary_search`, `std::lower_bound` does not require `operator<` or `comp` to be asymmetric (i.e., `a < b` and `b < a` always have different results). In fact, it does not even require `value < *iter` or `comp(value, *iter)` to be well-formed for any iterator `iter` in [first, last).

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <iostream>
#include <vector>

struct PriceInfo { double price; };

int main()
{
    const std::vector<int> data{1, 2, 4, 5, 5, 6};

    for (int i = 0; i < 8; ++i)
    {
        // Search for first element x such that i ≤ x
        auto lower = std::lower_bound(data.begin(), data.end(), i);

        std::cout << i << " ≤ ";
        lower != data.end()
            ? std::cout << *lower << " at index " << std::distance(data.begin(), lower)
            : std::cout << "not found";
        std::cout << '\n';
    }

    std::vector<PriceInfo> prices{{100.0}, {101.5}, {102.5}, {102.5}, {107.3
```

for (const double to_find : {102.5, 110.2})
{
auto prc_info = std::lower_bound(prices.begin(), prices.end(), to_find,
[](const PriceInfo& info, double value)
{
return info.price < value;
});
prc_info != prices.end()
? std::cout << prc_info->price << " at index " << prc_info - prices.begin()
: std::cout << to_find << " not found";
std::cout << '\n';
}
using CD = std::complex<double>;
std::vector<CD> nums1, 0}, {2, 2}, {2, 1}, {3, 0;
auto cmpz = [](CD x, CD y) { return x.real() < y.real(); };
#ifdef __cpp_lib_algorithm_default_value_type
auto it = std::lower_bound(nums.cbegin(), nums.cend(), {2, 0}, cmpz);
#else
auto it = std::lower_bound(nums.cbegin(), nums.cend(), CD{2, 0}, cmpz);
#endif
assert((*it == CD{2, 2}));
}
|output=
0 ≤ 1 at index 0
1 ≤ 1 at index 0
2 ≤ 2 at index 1
3 ≤ 4 at index 2
4 ≤ 4 at index 2
5 ≤ 5 at index 3
6 ≤ 6 at index 5
7 ≤ not found
102.5 at index 2
110.2 not found

## Defect reports


## See also


| cpp/algorithm/dsc equal_range | (see dedicated page) |
| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc partition_point | (see dedicated page) |
| cpp/algorithm/dsc upper_bound | (see dedicated page) |
| cpp/container/dsc lower_bound|set | (see dedicated page) |
| cpp/container/dsc lower_bound|multiset | (see dedicated page) |
| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |

