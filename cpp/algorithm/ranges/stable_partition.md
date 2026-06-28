---
title: std::ranges::stable_partition
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/stable_partition
---


```cpp
**Header:** `<`algorithm`>`
dcla|anchor=no|num=1|since=c++20|constexpr=c++26|1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
requires std::permutable<I>
ranges::subrange<I>
stable_partition( I first, S last, Pred pred, Proj proj = {} );
dcla|anchor=no|num=2|since=c++20|constexpr=c++26|1=
template< ranges::bidirectional_range R, class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
requires std::permutable<ranges::iterator_t<R>>
ranges::borrowed_subrange_t<R>
stable_partition( R&& r, Pred pred, Proj proj = {} );
```

1. Reorders the elements in the range [first, last) in such a way that the projection `proj` of all elements for which the predicate `pred` returns `true` precede the projection `proj` of elements for which predicate `pred` returns `false`. The algorithms is ''stable'', i.e. the relative order of elements is ''preserved''.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to reorder, sentinel=yes}})` - 
- `r` - the range of elements to reorder
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. An object equal to }, where `pivot` is an iterator to the first element of the second group.
2. Same as  if `r` is an lvalue or of a  type. Otherwise returns `std::ranges::dangling`.

## Complexity

Given `1= N = ranges::distance(first, last)`, the complexity is at worst } swaps, and only } swaps in case an extra memory buffer is used. Exactly  applications of the predicate `pred` and projection `proj`.

## Notes

This function attempts to allocate a temporary buffer. If the allocation fails, the less efficient algorithm is chosen.

## Possible implementation

This implementation does not use extra memory buffer and as such can be less efficient. See also the implementation in [https://github.com/microsoft/STL/blob/e745bad3b1d05b5b19ec652d68abb37865ffa454/stl/inc/algorithm#L5358-L5555 MSVC STL] and [https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L2365-L2394 libstdc++].
eq fun|1=
struct stable_partition_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
requires std::permutable<I>
constexpr ranges::subrange<I>
operator()(I first, S last, Pred pred, Proj proj = {}) const
{
first = ranges::find_if_not(first, last, pred, proj);
I mid = first;
while (mid != last)
{
mid = ranges::find_if(mid, last, pred, proj);
if (mid == last)
break;
I last2 = ranges::find_if_not(mid, last, pred, proj);
ranges::rotate(first, mid, last2);
first = ranges::next(first, ranges::distance(mid, last2));
mid = last2;
}
return {std::move(first), std::move(mid)};
}
template<ranges::bidirectional_range R, class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred>
requires std::permutable<ranges::iterator_t<R>>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(pred), std::move(proj));
}
};
inline constexpr stable_partition_fn stable_partition {};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

namespace rng = std::ranges;

template<std::permutable I, std::sentinel_for<I> S>
constexpr void stable_sort(I first, S last)
{
    if (first == last)
        return;

    auto pivot = *rng::next(first, rng::distance(first, last) / 2, last);
    auto left = [pivot](const auto& em) { return em < pivot; };
    auto tail1 = rng::stable_partition(first, last, left);
    auto right = [pivot](const auto& em) { return !(pivot < em); };
    auto tail2 = rng::stable_partition(tail1, right);

    stable_sort(first, tail1.begin());
    stable_sort(tail2.begin(), tail2.end());
}

void print(const auto rem, auto first, auto last, bool end = true)
{
    std::cout << rem;
    for (; first != last; ++first)
        std::cout << *first << ' ';
    std::cout << (end ? "\n" : "");
}

int main()
{
    const auto original = {9, 6, 5, 2, 3, 1, 7, 8};

    std::vector<int> vi {};
    auto even = [](int x) { return 0 == (x % 2); };

    print("Original vector:\t", original.begin(), original.end(), "\n");

    vi = original;
    const auto ret1 = rng::stable_partition(vi, even);
    print("Stable partitioned:\t", vi.begin(), ret1.begin(), 0);
    print("│ ", ret1.begin(), ret1.end());

    vi = original;
    const auto ret2 = rng::partition(vi, even);
    print("Partitioned:\t\t", vi.begin(), ret2.begin(), 0);
    print("│ ", ret2.begin(), ret2.end());


    vi = {16, 30, 44, 30, 15, 24, 10, 18, 12, 35};
    print("Unsorted vector: ", vi.begin(), vi.end());

    stable_sort(rng::begin(vi), rng::end(vi));
    print("Sorted vector:   ", vi.begin(), vi.end());
}
```


**Output:**
```
Original vector:        9 6 5 2 3 1 7 8
Stable partitioned:     6 2 8 │ 9 5 3 1 7
Partitioned:            8 6 2 │ 5 3 1 7 9
Unsorted vector: 16 30 44 30 15 24 10 18 12 35
Sorted vector:   10 12 15 16 18 24 30 30 35 44
```


## See also


| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_partitioned | (see dedicated page) |
| cpp/algorithm/dsc stable_partition | (see dedicated page) |

