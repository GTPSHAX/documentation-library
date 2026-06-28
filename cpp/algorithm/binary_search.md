---
title: std::binary_search
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/binary_search
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
bool binary_search( ForwardIt first, ForwardIt last,
const T& value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr bool binary_search( ForwardIt first, ForwardIt last,
const T& value );
dcl rev multi|num=2|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T, class Compare >
bool binary_search( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type,
class Compare >
constexpr bool binary_search( ForwardIt first, ForwardIt last,
const T& value, Compare comp );
```

Checks if an element equivalent to `value` appears within the partitioned range [first, last).
1. The equivalence is checked using `operator<`:
rev|until=c++20|
If `!bool(*iter < value) && !bool(value < *iter)` is `true` for some iterator `iter` in [first, last), returns `true`. Otherwise returns `false`.
If any of the following conditions is satisfied, the behavior is undefined:
* For any element `elem` of [first, last), `bool(elem < value)` does not imply `!bool(value < elem)`.
* The elements `elem` of [first, last) are not `partitioned` with respect to expressions `bool(elem < value)` and `!bool(value < elem)`.
rev|since=c++20|
Equivalent to }.
2. The equivalence is checked using `comp`:
@@ If `!bool(comp(*iter, value)) && !bool(comp(value, *iter))` is `true` for some iterator `iter` in [first, last), returns `true`. Otherwise returns `false`.
@@ If any of the following conditions is satisfied, the behavior is undefined:
* For any element `elem` of [first, last), `bool(comp(elem, value))` does not imply `!bool(comp(value, elem))`.
* The elements `elem` of [first, last) are not `partitioned` with respect to expressions `bool(comp(elem, value))` and `!bool(comp(value, elem))`.

## Parameters


### Parameters

- `[3=to examine, range=partitioned}})` - 
- `value` - value to compare the elements to

**Type requirements:**

- `ForwardIt`
- `Compare`

## Return value

`true` if an element equivalent to `value` is found, `false` otherwise.

## Complexity

Given  as `std::distance(first, last)`:
1. At most } comparisons with `value` using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most } applications of the comparator `comp`.
However, if `ForwardIt` is not a *RandomAccessIterator*, the number of iterator increments is linear in .

## Notes

Although `std::binary_search` only requires [first, last) to be partitioned, this algorithm is usually used in the case where [first, last) is sorted, so that the binary search is valid for any `value`.
`std::binary_search` only checks whether an equivalent element exists. To obtain an iterator to that element (if exists), `std::lower_bound` should be used instead.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/d9375e490072d1aae73a93949aa158fcd2a27018/libstdc%2B%2B-v3/include/bits/stl_algo.h#L2236 libstdc++] and [https://github.com/llvm-mirror/libcxx/blob/a12cb9d211019d99b5875b6d8034617cbc24c2cc/include/algorithm#L4320 libc++].
eq impl
|title1=binary_search (1)|ver1=1|1=
template<class ForwardIt, class T = typename std::iterator_traits<ForwardIt>::value_type>
bool binary_search(ForwardIt first, ForwardIt last, const T& value)
{
return std::binary_search(first, last, value, std::less{});
}
|title2=binary_search (2)|ver2=2|2=
template<class ForwardIt, class T = typename std::iterator_traits<ForwardIt>::value_type,
class Compare>
bool binary_search(ForwardIt first, ForwardIt last, const T& value, Compare comp)
{
first = std::lower_bound(first, last, value, comp);
return (!(first == last) and !(comp(value, *first)));
}

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <iostream>
#include <vector>

int main()
{
    const auto haystack = {1, 3, 4, 5, 9};

    for (const auto needle : {1, 2, 3})
    {
        std::cout << "Searching for " << needle << '\n';
        if (std::binary_search(haystack.begin(), haystack.end(), needle))
            std::cout << "Found " << needle << '\n';
        else
            std::cout << "Not found!\n";
    }

    using CD = std::complex<double>;
    std::vector<CD> nums{<!---->{1, 1}, {2, 3}, {4, 2}, {4, 3}<!---->};
    auto cmpz = [](CD x, CD y){ return abs(x) < abs(y); };
    #ifdef __cpp_lib_algorithm_default_value_type
        assert(std::binary_search(nums.cbegin(), nums.cend(), {4, 2}, cmpz));
    #else
        assert(std::binary_search(nums.cbegin(), nums.cend(), CD{4, 2}, cmpz));
    #endif
}
```


**Output:**
```
Searching for 1
Found 1
Searching for 2
Not found!
Searching for 3
Found 3
```


## Defect reports


## See also


| cpp/algorithm/dsc equal_range | (see dedicated page) |
| cpp/algorithm/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc binary_search | (see dedicated page) |

