---
title: std::ranges::sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/sort
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I
sort( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::random_access_range R, class Comp = ranges::less,
class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
sort( R&& r, Comp comp = {}, Proj proj = {} );
```

Sorts the elements in the range [first, last) in non-descending order. The order of equivalent elements is not guaranteed to be preserved.
A sequence is sorted with respect to a comparator `comp` if for any iterator `it` pointing to the sequence and any non-negative integer `n` such that `it + n` is a valid iterator pointing to an element of the sequence, `std::invoke(comp, std::invoke(proj, *(it + n)), std::invoke(proj, *it))` evaluates to `false`.
1. Elements are compared using the given binary comparison function `comp`.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to sort, sentinel=yes}})` - 
- `r` - the range to sort
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

An iterator equal to `last`.

## Complexity

mathjax-or|\(\scriptsize \mathcal{O}(N\cdot\log{(N)})\)|𝓞(N&middot;log(N)) comparisons and projections, where `1=N = ranges::distance(first, last)`.

## Possible implementation

Note that typical implementations use [Introsort](https://en.wikipedia.org/wiki/Introsort). See also the implementation in [https://github.com/microsoft/STL/blob/e745bad3b1d05b5b19ec652d68abb37865ffa454/stl/inc/algorithm#L7575-L7641 MSVC STL] and [https://github.com/gcc-mirror/gcc/blob/54258e22b0846aaa6bd3265f592feb161eecda75/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1808-L1834 libstdc++].
eq fun|1=
struct sort_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr I
operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
if (first == last)
return first;
<!--
const auto pivot = *ranges::next(first, ranges::distance(first, last) / 2, last);
auto tail1 = ranges::partition(first, last, [&pivot, &comp, &proj](const auto& em) {
return std::invoke(comp, std::invoke(proj, em), std::invoke(proj, pivot)); });
auto tail2 = ranges::partition(tail1, [&pivot, &comp, &proj](const auto& em) {
return !std::invoke(comp, std::invoke(proj, pivot), std::invoke(proj, em)); });
(*this)(first, tail1.begin(), std::ref(comp), std::ref(proj));
(*this)(tail2, std::ref(comp), std::ref(proj));
return {ranges::next(first, last)};
-->
I last_iter = ranges::next(first, last);
ranges::make_heap(first, last_iter, std::ref(comp), std::ref(proj));
ranges::sort_heap(first, last_iter, std::ref(comp), std::ref(proj));
return last_iter;
}
template<ranges::random_access_range R, class Comp = ranges::less,
class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(comp), std::move(proj));
}
};
inline constexpr sort_fn sort {};

## Notes

`std::sort` uses `std::iter_swap` to swap elements, whereas `ranges::sort` instead uses `ranges::iter_swap` (which performs ADL for `iter_swap`, unlike `std::iter_swap`)

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <iomanip>
#include <iostream>

void print(auto comment, auto const& seq, char term = ' ')
{
    for (std::cout << comment << '\n'; auto const& elem : seq)
        std::cout << elem << term;
    std::cout << '\n';
}

struct Particle
{
    std::string name; double mass; // MeV
    template<class Os> friend
    Os& operator<<(Os& os, Particle const& p)
    {
        return os << std::left << std::setw(8) << p.name << " : " << p.mass << ' ';
    }
};

int main()
{
    std::array s {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};

    namespace ranges = std::ranges;

    ranges::sort(s);
    print("Sort using the default operator<", s);

    ranges::sort(s, ranges::greater());
    print("Sort using a standard library compare function object", s);

    struct
    {
        bool operator()(int a, int b) const { return a < b; }
    } customLess;
    ranges::sort(s.begin(), s.end(), customLess);
    print("Sort using a custom function object", s);

    ranges::sort(s, [](int a, int b) { return a > b; });
    print("Sort using a lambda expression", s);

    Particle particles[]
    {
        {"Electron", 0.511}, {"Muon", 105.66}, {"Tau", 1776.86},
        {"Positron", 0.511}, {"Proton", 938.27}, {"Neutron", 939.57}
    };
    ranges::sort(particles, {}, &Particle::name);
    print("\nSort by name using a projection", particles, '\n');
    ranges::sort(particles, {}, &Particle::mass);
    print("Sort by mass using a projection", particles, '\n');
}
```


**Output:**
```
Sort using the default operator<
0 1 2 3 4 5 6 7 8 9
Sort using a standard library compare function object
9 8 7 6 5 4 3 2 1 0
Sort using a custom function object
0 1 2 3 4 5 6 7 8 9
Sort using a lambda expression
9 8 7 6 5 4 3 2 1 0

Sort by name using a projection
Electron : 0.511
Muon     : 105.66
Neutron  : 939.57
Positron : 0.511
Proton   : 938.27
Tau      : 1776.86

Sort by mass using a projection
Electron : 0.511
Positron : 0.511
Muon     : 105.66
Proton   : 938.27
Neutron  : 939.57
Tau      : 1776.86
```


## See also


| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc sort | (see dedicated page) |

