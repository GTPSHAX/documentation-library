---
title: std::set_symmetric_difference
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/set_symmetric_difference
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class OutputIt >
OutputIt set_symmetric_difference
( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class ForwardIt3 >
ForwardIt3 set_symmetric_difference
( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class Compare >
OutputIt set_symmetric_difference
( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class Compare >
ForwardIt3 set_symmetric_difference
( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first, Compare comp );
```

Computes symmetric difference of two sorted ranges: the elements that are found in either of the ranges, but not in both of them are copied to the range beginning at `d_first`. The output range is also sorted.
If [first1, last1) contains `m` elements that are equivalent to each other and [first2, last2) contains `n` elements that are equivalent to them, then `std::abs(m - n)` of those elements will be copied to the output range, preserving order:
* if `m > n`, the final `m - n` of these elements from [first1, last1).
* if `m < n`, the final `n - m` of these elements from [first2, last2).
1. If [first1, last1) or [first2, last2) is not `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, the behavior is undefined.
3. If [first1, last1) or [first2, last2) is not sorted with respect to `comp`, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@
If the output range overlaps with [first1, last1) or [first2, last2), the behavior is undefined.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `d_first` - the beginning of the output range
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `InputIt1, InputIt2`
- `OutputIt`
- `ForwardIt1, ForwardIt2, ForwardIt3`
- `Compare`

## Return value

Iterator past the end of the constructed range.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
@1,2@ At most +N)-1 comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ At most +N)-1 applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=set_symmetric_difference (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_symmetric_difference(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first)
{
while (first1 != last1)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (*first1 < *first2)
*d_first++ = *first1++;
else
{
if (*first2 < *first1)
*d_first++ = *first2;
else
++first1;
++first2;
}
}
return std::copy(first2, last2, d_first);
}
|title2=set_symmetric_difference (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt set_symmetric_difference(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp)
{
while (first1 != last1)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (comp(*first1, *first2))
*d_first++ = *first1++;
else
{
if (comp(*first2, *first1))
*d_first++ = *first2;
else
++first1;
++first2;
}
}
return std::copy(first2, last2, d_first);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> v1{1, 2, 3, 4, 5, 6, 7, 8};
    std::vector<int> v2{5, 7, 9, 10};
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());

    std::vector<int> v_symDifference;

    std::set_symmetric_difference(v1.begin(), v1.end(), v2.begin(), v2.end(),
                                  std::back_inserter(v_symDifference));

    for (int n : v_symDifference)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 3 4 6 8 9 10
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-291 | C++98 | it was unspecified how to handle equivalent elements in the input ranges | specified |


## See also


| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc set_difference | (see dedicated page) |
| cpp/algorithm/dsc set_union | (see dedicated page) |
| cpp/algorithm/dsc set_intersection | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_symmetric_difference | (see dedicated page) |

