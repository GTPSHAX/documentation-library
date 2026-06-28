---
title: std::ranges::stable_sort
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/stable_sort
---


```cpp
**Header:** `<`algorithm`>`
dcla|anchor=no|num=1|since=c++20|constexpr=c++26|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
I stable_sort( I first, S last, Comp comp = {}, Proj proj = {} );
dcla|anchor=no|num=2|since=c++20|constexpr=c++26|1=
template< ranges::random_access_range R, class Comp = ranges::less,
class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
ranges::borrowed_iterator_t<R>
stable_sort( R&& r, Comp comp = {}, Proj proj = {} );
```

Sorts the elements in the range [first, last) in non-descending order. The order of equivalent elements is ''stable'', i.e. guaranteed to be preserved.
A sequence is sorted with respect to a comparator `comp` if for any iterator `it` pointing to the sequence and any non-negative integer `n` such that `it + n` is a valid iterator pointing to an element of the sequence, `std::invoke(comp, std::invoke(proj, *(it + n)), std::invoke(proj, *it)` evaluates to `false`.
1. Elements are compared using the given binary comparison function `comp`.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to sort, sentinel=yes}})` - 
- `r` - the range to sort
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

An iterator equal to `last`.

## Complexity

} comparisons, if extra memory is available; where  is `ranges::distance(first, last)`. } comparisons otherwise. Twice as many projections as the number of comparisons in both cases.

## Notes


## Possible implementation

This implementation only shows the slower algorithm used when no additional memory is available. See also implementation in [https://github.com/microsoft/STL/blob/e745bad3b1d05b5b19ec652d68abb37865ffa454/stl/inc/algorithm#L7842-L8094 MSVC STL] and [https://github.com/gcc-mirror/gcc/blob/54258e22b0846aaa6bd3265f592feb161eecda75/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1836-L1862 libstdc++].
eq fun|1=
struct stable_sort_fn
{
template<std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr //< since C++26
I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
auto count = ranges::distance(first, last);
auto mid = first + count / 2;
auto last_it = first + count;
if (count <= 1)
return last_it;
(*this)(first, mid, std::ref(comp), std::ref(proj));
(*this)(mid, last_it, std::ref(comp), std::ref(proj));
ranges::inplace_merge(first, mid, last_it);
return last_it;
}
template<ranges::random_access_range R, class Comp = ranges::less,
class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr //< since C++26
ranges::borrowed_iterator_t<R> operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(comp), std::move(proj));
}
};
inline constexpr stable_sort_fn stable_sort{};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <iomanip>
#include <iostream>

void print(const auto& seq)
{
    for (const auto& elem : seq)
        std::cout << elem << ' ';
    std::cout << '\n';
}

struct Particle
{
    std::string name; double mass; // MeV
    friend std::ostream& operator<<(std::ostream& os, const Particle& p)
    {
        return os << '\n' << std::left << std::setw(8) << p.name << " : " << p.mass;
    }
};

int main()
{
    std::array s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};

    // sort using the default operator<
    std::ranges::stable_sort(s);
    print(s);

    // sort using a standard library compare function object
    std::ranges::stable_sort(s, std::ranges::greater());
    print(s);

    // sort using a custom function object
    struct
    {
        bool operator()(int a, int b) const { return a < b; }
    } customLess;
    std::ranges::stable_sort(s.begin(), s.end(), customLess);
    print(s);

    // sort using a lambda expression
    std::ranges::stable_sort(s, [](int a, int b) { return a > b; });
    print(s);

    // sort with projection
    Particle particles[]
    {
        {"Electron", 0.511}, {"Muon", 105.66}, {"Tau", 1776.86},
        {"Positron", 0.511}, {"Proton", 938.27}, {"Neutron", 939.57}
    };
    print(particles);
    std::ranges::stable_sort(particles, {}, &Particle::name); //< sorts by name
    print(particles);
    std::ranges::stable_sort(particles, {}, &Particle::mass); //< sorts by mass
    print(particles);
}
```


**Output:**
```
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0

Electron : 0.511
Muon     : 105.66
Tau      : 1776.86
Positron : 0.511
Proton   : 938.27
Neutron  : 939.57

Electron : 0.511
Muon     : 105.66
Neutron  : 939.57
Positron : 0.511
Proton   : 938.27
Tau      : 1776.86

Electron : 0.511
Positron : 0.511
Muon     : 105.66
Proton   : 938.27
Neutron  : 939.57
Tau      : 1776.86
```


## See also


| cpp/algorithm/ranges/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |

