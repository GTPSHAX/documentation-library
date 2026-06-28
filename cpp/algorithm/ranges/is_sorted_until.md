---
title: std::ranges::is_sorted_until
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/is_sorted_until
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>>
Comp = ranges::less >
constexpr I
is_sorted_until( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< std::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>>
Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
is_sorted_until( R&& r, Comp comp = {}, Proj proj = {} );
```

Examines the range [first, last) and finds the largest range beginning at `first` in which the elements are sorted in non-descending order.
A sequence is sorted with respect to a comparator `comp` if for any iterator `it` pointing to the sequence and any non-negative integer `n` such that `it + n` is a valid iterator pointing to an element of the sequence, `std::invoke(comp, std::invoke(proj, *(it + n)), std::invoke(proj, *it))` evaluates to `false`.
1. Elements are compared using the given binary comparison function `comp`.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to find its sorted upper bound, sentinel=yes}})` - 
- `r` - the range to find its sorted  upper bound
- `comp` - comparison function to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

The upper bound of the largest range beginning at `first` in which the elements are sorted in non-descending order. That is, the last iterator `it` for which range [first, it) is sorted.

## Complexity

Linear in the distance between `first` and `last`.

## Possible implementation

eq fun
|1=
struct is_sorted_until_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>>
Comp = ranges::less>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
if (first == last)
return first;
for (auto next = first; ++next != last; first = next)
if (std::invoke(comp, std::invoke(proj, *next), std::invoke(proj, *first)))
return next;
return first;
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(comp), std::ref(proj));
}
};
inline constexpr is_sorted_until_fn is_sorted_until;

## Notes

`ranges::is_sorted_until` returns an iterator equal to `last` for empty ranges and ranges of length one.

## Example


### Example

```cpp
#include <array>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <random>

int main()
{
    std::random_device rd;
    std::mt19937 g {rd()};
    std::array nums {3, 1, 4, 1, 5, 9};

    constexpr int min_sorted_size = 4;
    int sorted_size = 0;
    do
    {
        std::ranges::shuffle(nums, g);
        const auto sorted_end = std::ranges::is_sorted_until(nums);
        sorted_size = std::ranges::distance(nums.begin(), sorted_end);

        std::ranges::copy(nums, std::ostream_iterator<int>(std::cout, " "));
        std::cout << " : " << sorted_size << " leading sorted element(s)\n";
    }
    while (sorted_size < min_sorted_size);
}
```


**Output:**
```
4 1 9 5 1 3  : 1 leading sorted element(s)
4 5 9 3 1 1  : 3 leading sorted element(s)
9 3 1 4 5 1  : 1 leading sorted element(s)
1 3 5 4 1 9  : 3 leading sorted element(s)
5 9 1 1 3 4  : 2 leading sorted element(s)
4 9 1 5 1 3  : 2 leading sorted element(s)
1 1 4 9 5 3  : 4 leading sorted element(s)
```


## See also


| cpp/algorithm/ranges/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/dsc is_sorted_until | (see dedicated page) |

