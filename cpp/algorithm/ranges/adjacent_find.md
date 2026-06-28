---
title: std::ranges::adjacent_find
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/adjacent_find
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_binary_predicate<
std::projected<I, Proj>,
std::projected<I, Proj>> Pred = ranges::equal_to >
constexpr I
adjacent_find( I first, S last, Pred pred = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::forward_range R, class Proj = std::identity,
std::indirect_binary_predicate<
std::projected<ranges::iterator_t<R>, Proj>,
std::projected<ranges::iterator_t<R>, Proj>> Pred = ranges::equal_to >
constexpr ranges::borrowed_iterator_t<R>
adjacent_find( R&& r, Pred pred = {}, Proj proj = {} );
```

Searches the range [first, last) for the first two consecutive equal elements.
1. Elements are compared using `pred` (after projecting with the projection `proj`).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the range of the elements to examine
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

An iterator to the first of the first pair of identical elements, that is, the first iterator `it` such that `bool(std::invoke(pred, std::invoke(proj1, *it), std::invoke(proj, *(it + 1))))` is `true`.
If no such elements are found, an iterator equal to `last` is returned.

## Complexity

Exactly `min((result - first) + 1, (last - first) - 1)` applications of the predicate and projection where `result` is the return value.

## Possible implementation

eq fun|1=
struct adjacent_find_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_binary_predicate<
std::projected<I, Proj>,
std::projected<I, Proj>> Pred = ranges::equal_to>
constexpr I operator()(I first, S last, Pred pred = {}, Proj proj = {}) const
{
if (first == last)
return first;
auto next = ranges::next(first);
for (; next != last; ++next, ++first)
if (std::invoke(pred, std::invoke(proj, *first), std::invoke(proj, *next)))
return first;
return next;
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_binary_predicate<
std::projected<ranges::iterator_t<R>, Proj>,
std::projected<ranges::iterator_t<R>, Proj>> Pred = ranges::equal_to>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj));
}
};
inline constexpr adjacent_find_fn adjacent_find;

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <ranges>

constexpr bool some_of(auto&& r, auto&& pred) // some but not all
{
    return std::ranges::cend(r) != std::ranges::adjacent_find(r,
        [&pred](auto const& x, auto const& y)
        {
            return pred(x) != pred(y);
        });
}

// test some_of
constexpr auto a = {0, 0, 0, 0}, b = {1, 1, 1, 0}, c = {1, 1, 1, 1};
auto is_one = [](auto x){ return x == 1; };
static_assert(!some_of(a, is_one) && some_of(b, is_one) && !some_of(c, is_one));

int main()
{
    const auto v = {0, 1, 2, 3, 40, 40, 41, 41, 5}; /*
                                ^^          ^^       */
    namespace ranges = std::ranges;

    if (auto it = ranges::adjacent_find(v.begin(), v.end()); it == v.end())
        std::cout << "No matching adjacent elements\n";
    else
        std::cout << "The first adjacent pair of equal elements is at ["
                  << ranges::distance(v.begin(), it) << "] == " << *it << '\n';

    if (auto it = ranges::adjacent_find(v, ranges::greater()); it == v.end())
        std::cout << "The entire vector is sorted in ascending order\n";
    else
        std::cout << "The last element in the non-decreasing subsequence is at ["
                  << ranges::distance(v.begin(), it) << "] == " << *it << '\n';
}
```


**Output:**
```
The first adjacent pair of equal elements is at [4] == 40
The last element in the non-decreasing subsequence is at [7] == 41
```


## See also


| cpp/algorithm/ranges/dsc unique | (see dedicated page) |
| cpp/algorithm/dsc adjacent_find | (see dedicated page) |

