---
title: std::set_union
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/set_union
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class OutputIt >
OutputIt set_union( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class ForwardIt3 >
ForwardIt3 set_union( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class Compare >
OutputIt set_union( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2,
OutputIt d_first, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class Compare >
ForwardIt3 set_union( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2,
ForwardIt3 d_first, Compare comp );
```

Constructs a sorted union beginning at `d_first` consisting of the set of elements present in one or both sorted ranges [first1, last1) and [first2, last2).
If [first1, last1) contains `m` elements that are equivalent to each other and [first2, last2) contains `n` elements that are equivalent to them, then all `m` elements will be copied from [first1, last1) to the output range, preserving order, and then the final `std::max(n - m, 0)` elements will be copied from [first2, last2) to the output range, also preserving order.
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
- `ForwardIt1, ForwardIt2, ForwardIt3`
- `OutputIt`
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
|title1=set_union (1)|ver1=1|1=
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_union(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first)
{
for (; first1 != last1; ++d_first)
{
if (first2 == last2)
return std::copy(first1, last1, d_first);
if (*first2 < *first1)
*d_first = *first2++;
else
{
*d_first = *first1;
if (!(*first1 < *first2))
++first2;
++first1;
}
}
return std::copy(first2, last2, d_first);
}
|title2=set_union (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class OutputIt, class Compare>
OutputIt set_union(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, OutputIt d_first, Compare comp)
{
for (; first1 != last1; ++d_first)
{
if (first2 == last2)
// Finished range 2, include the rest of range 1:
return std::copy(first1, last1, d_first);
if (comp(*first2, *first1))
*d_first = *first2++;
else
{
*d_first = *first1;
if (!comp(*first1, *first2)) // Equivalent => don't need to include *first2.
++first2;
++first1;
}
}
// Finished range 1, include the rest of range 2:
return std::copy(first2, last2, d_first);
}

## Notes

This algorithm performs a similar task as `std::merge` does. Both consume two sorted input ranges and produce a sorted output with elements from both inputs. The difference between these two algorithms is with handling values from both input ranges which compare equivalent (see notes on *LessThanComparable*). If any equivalent values appeared `n` times in the first range and `m` times in the second, `std::merge` would output all `n + m` occurrences whereas `std::set_union` would output `std::max(n, m)` ones only. So `std::merge` outputs exactly `std::distance(first1, last1) + std::distance(first2, last2)` values and `std::set_union` may produce fewer.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

void println(const std::vector<int>& v)
{
    for (int i : v)
        std::cout << i << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v1, v2, dest;

    v1 = {1, 2, 3, 4, 5};
    v2 = {3, 4, 5, 6, 7};

    std::set_union(v1.cbegin(), v1.cend(),
                   v2.cbegin(), v2.cend(),
                   std::back_inserter(dest));
    println(dest);

    dest.clear();

    v1 = {1, 2, 3, 4, 5, 5, 5};
    v2 = {3, 4, 5, 6, 7};

    std::set_union(v1.cbegin(), v1.cend(),
                   v2.cbegin(), v2.cend(),
                   std::back_inserter(dest));
    println(dest);
}
```


**Output:**
```
1 2 3 4 5 6 7 
1 2 3 4 5 5 5 6 7
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-291 | C++98 | it was unspecified how to handle equivalent elements in the input ranges | specified |


## See also


| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc merge | (see dedicated page) |
| cpp/algorithm/dsc set_difference | (see dedicated page) |
| cpp/algorithm/dsc set_intersection | (see dedicated page) |
| cpp/algorithm/dsc set_symmetric_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_union | (see dedicated page) |

