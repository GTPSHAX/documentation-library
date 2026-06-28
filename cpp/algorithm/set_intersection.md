---
title: std::set_intersection
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/set_intersection
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class OutputIt >
OutputIt set_intersection( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class ForwardIt3 >
ForwardIt3 set_intersection( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class Compare >
OutputIt set_intersection( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class Compare >
ForwardIt3 set_intersection( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first, Compare comp );
```

Constructs a sorted range beginning at `d_first` consisting of elements that are found in both sorted ranges [first1, last1) and [first2, last2).
If [first1, last1) contains `m` elements that are equivalent to each other and [first2, last2) contains `n` elements that are equivalent to them, the first `std::min(m, n)` elements will be copied from [first1, last1) to the output range, preserving order.
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
|title1=set_intersection (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_intersection(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first)
{
while (first1 != last1 && first2 != last2)
{
if (*first1 < *first2)
++first1;
else
{
if (!(*first2 < *first1))
*d_first++ = *first1++; // *first1 and *first2 are equivalent.
++first2;
}
}
return d_first;
}
|title2=set_intersection (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt set_intersection(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first, Compare comp)
{
while (first1 != last1 && first2 != last2)
{
if (comp(*first1, *first2))
++first1;
else
{
if (!comp(*first2, *first1))
*d_first++ = *first1++; // *first1 and *first2 are equivalent.
++first2;
}
}
return d_first;
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
    std::vector<int> v1{7, 2, 3, 4, 5, 6, 7, 8};
    std::vector<int> v2{5, 7, 9, 7};
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());

    std::vector<int> v_intersection;
    std::set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(),
                          std::back_inserter(v_intersection));

    for (int n : v_intersection)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
5 7 7
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-291 | C++98 | it was unspecified how to handle equivalent elements in the input ranges | specified |


## See also


| cpp/algorithm/dsc set_union | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_intersection | (see dedicated page) |

