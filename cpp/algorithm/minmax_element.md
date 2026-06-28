---
title: std::minmax_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/minmax_element
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|notes=<sup>(constexpr C++17)</sup>|
template< class ForwardIt >
std::pair<ForwardIt, ForwardIt>
minmax_element( ForwardIt first, ForwardIt last );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt >
std::pair<ForwardIt, ForwardIt>
minmax_element( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last );
dcla|num=3|since=c++11|notes=<sup>(constexpr C++17)</sup>|
template< class ForwardIt, class Compare >
std::pair<ForwardIt, ForwardIt>
minmax_element( ForwardIt first, ForwardIt last, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class Compare >
std::pair<ForwardIt, ForwardIt>
minmax_element( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, Compare comp );
```

Finds the smallest and greatest element in the range [first, last).
1. Elements are compared using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
3. Elements are compared using the comparison function `comp`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

a pair consisting of an iterator to the smallest element as the first element and an iterator to the greatest element as the second. Returns `std::make_pair(first, first)` if the range is empty. If several elements are equivalent to the smallest element, the iterator to the first such element is returned. If several elements are equivalent to the largest element, the iterator to the last such element is returned.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ At most mathjax-or|\(\scriptsize \max(\left\lfloor \frac{3}{2}(N-1) \right\rfloor, 0)\)|max(⌊(N-1)⌋,0) comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ At most mathjax-or|\(\scriptsize \max(\left\lfloor \frac{3}{2}(N-1) \right\rfloor, 0)\)|max(⌊(N-1)⌋,0) applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=minmax_element|ver1=1|1=
template<class ForwardIt>
std::pair<ForwardIt, ForwardIt>
minmax_element(ForwardIt first, ForwardIt last)
{
using value_type = typename std::iterator_traits<ForwardIt>::value_type;
return std::minmax_element(first, last, std::less<value_type>());
}
|title2=minmax_element|ver2=3|2=
template<class ForwardIt, class Compare>
std::pair<ForwardIt, ForwardIt>
minmax_element(ForwardIt first, ForwardIt last, Compare comp)
{
auto min = first, max = first;
if (first == last  ++first == last)
return {min, max};
if (comp(*first, *min))
min = first;
else
max = first;
while (++first != last)
{
auto i = first;
if (++first == last)
{
if (comp(*i, *min))
min = i;
else if (!(comp(*i, *max)))
max = i;
break;
}
else
{
if (comp(*first, *i))
{
if (comp(*first, *min))
min = first;
if (!(comp(*i, *max)))
max = i;
}
else
{
if (comp(*i, *min))
min = i;
if (!(comp(*first, *max)))
max = first;
}
}
}
return {min, max};
}

## Notes

This algorithm is different from `std::make_pair(std::min_element(), std::max_element())`, not only in efficiency, but also in that this algorithm finds the ''last'' biggest element while `std::max_element` finds the ''first'' biggest element.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>

int main()
{
    const auto v = {3, 9, 1, 4, 2, 5, 9};
    const auto [min, max] = std::minmax_element(begin(v), end(v));

    std::cout << "min = " << *min << ", max = " << *max << '\n';
}
```


**Output:**
```
min = 1, max = 9
```


## See also


| cpp/algorithm/dsc min_element | (see dedicated page) |
| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |

