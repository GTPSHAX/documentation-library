---
title: std::partition_point
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partition_point
---

ddcl|header=algorithm|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt, class UnaryPred >
ForwardIt partition_point( ForwardIt first, ForwardIt last, UnaryPred p );
Examines the partitioned range [first, last) and locates the end of the first partition, that is, the first element that does not satisfy `p` or `last` if all elements satisfy `p`.
If the elements `elem` of [first, last) are not `partitioned` with respect to the expression `bool(p(elem))`, the behavior is undefined.

## Parameters


### Parameters

- `[3=to examine, range=partitioned}})` - 

**Type requirements:**

- `ForwardIt`
- `UnaryPred`

## Return value

The iterator past the end of the first partition within [first, last) or `last` if all elements satisfy `p`.

## Complexity

Given  as `std::distance(first, last)`, performs  applications of the predicate `p`.

## Notes

This algorithm is a more general form of `std::lower_bound`, which can be expressed in terms of `std::partition_point` with the predicate }.

## Possible implementation

eq fun|1=
template<class ForwardIt, class UnaryPred>
constexpr //< since C++20
ForwardIt partition_point(ForwardIt first, ForwardIt last, UnaryPred p)
{
for (auto length = std::distance(first, last); 0 < length; )
{
auto half = length / 2;
auto middle = std::next(first, half);
if (p(*middle))
{
first = std::next(middle);
length -= (half + 1);
}
else
length = half;
}
return first;
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>

auto print_seq = [](auto rem, auto first, auto last)
{
    for (std::cout << rem; first != last; std::cout << *first++ << ' ') {}
    std::cout << '\n';
};

int main()
{
    std::array v{1, 2, 3, 4, 5, 6, 7, 8, 9};

    auto is_even = [](int i) { return i % 2 == 0; };

    std::partition(v.begin(), v.end(), is_even);
    print_seq("After partitioning, v: ", v.cbegin(), v.cend());

    const auto pp = std::partition_point(v.cbegin(), v.cend(), is_even);
    const auto i = std::distance(v.cbegin(), pp);
    std::cout << "Partition point is at " << i << "; v[" << i << "] = " << *pp << '\n';

    print_seq("First partition (all even elements): ", v.cbegin(), pp);
    print_seq("Second partition (all odd elements): ", pp, v.cend());
}
```


**Output:**
```
After partitioning, v: 8 2 6 4 5 3 7 1 9
Partition point is at 4; v[4] = 5
First partition (all even elements): 8 2 6 4
Second partition (all odd elements): 5 3 7 1 9
```


## See also


| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_point | (see dedicated page) |

