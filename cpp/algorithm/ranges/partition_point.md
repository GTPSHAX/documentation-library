---
title: std::ranges::partition_point
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/partition_point
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr I
partition_point( I first, S last, Pred pred, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R,
class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr ranges::borrowed_iterator_t<R>
partition_point( R&& r, Pred pred, Proj proj = {} );
```

Examines the partitioned (as if by `ranges::partition`) range [first, last) or `r` and locates the end of the first partition, that is, the projected element that does not satisfy `pred` or `last` if all projected elements satisfy `pred`.

## Parameters


### Parameters

- `[3=to examine, range=partially-ordered)` - 
- `r` - the partially-ordered range to examine
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

The iterator past the end of the first partition within [first, last) or the iterator equal to `last` if all projected elements satisfy `pred`.

## Complexity

Given `1=N = ranges::distance(first, last)`, performs $O(log N)$ applications of the predicate `pred` and projection `proj`.
However, if sentinels don't model `std::sized_sentinel_for<I>`, the number of iterator increments is $O(N)$.

## Notes

This algorithm is a more general form of `ranges::lower_bound`, which can be expressed in terms of `ranges::partition_point` with the predicate }.

## Example


### Example


**Output:**
```
After partitioning, v: 2 4 6 8 5 3 7 1 9
Partition point is at 4; v[4] = 5
First partition (all even elements): 2 4 6 8
Second partition (all odd elements): 5 3 7 1 9
```


## See also


| cpp/algorithm/ranges/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/dsc partition_point | (see dedicated page) |

