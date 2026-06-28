---
title: std::ranges::binary_search
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/binary_search
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr bool binary_search( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
|dcl2=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less >
constexpr bool binary_search( I first, S last, const T& value,
Comp comp = {}, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< ranges::forward_range R,
class T, class Proj = std::identity,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr bool binary_search( R&& r, const T& value,
Comp comp = {}, Proj proj = {} );
|dcl2=
template< ranges::forward_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less >
constexpr bool binary_search( R&& r, const T& value,
Comp comp = {}, Proj proj = {} );
```

1. Checks if a projected element equivalent to `value` appears within the range [first, last).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
For `ranges::binary_search` to succeed, the range [first, last) must be at least partially ordered with respect to `value`, i.e. it must satisfy all of the following requirements:
* partitioned with respect to `std::invoke(comp, std::invoke(proj, element), value)` (that is, all projected elements for which the expression is `true` precedes all elements for which the expression is `false`).
* partitioned with respect to `!std::invoke(comp, value, std::invoke(proj, element))`.
* for all elements, if `std::invoke(comp, std::invoke(proj, element), value)` is `true` then `!std::invoke(comp, value, std::invoke(proj, element))` is also `true`.
A fully-sorted range meets these criteria.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the range of elements to examine
- `value` - value to compare the elements to
- `comp` - comparison function to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

`true` if an element equal to `value` is found, `false` otherwise.

## Complexity

The number of comparisons and projections performed is logarithmic in the distance between `first` and `last` (at most $log comparisons and projections). However, for iterator-sentinel pair that does not model `std::random_access_iterator`, number of iterator increments is linear.

## Notes

`std::ranges::binary_search` doesn't return an iterator to the found element when an element whose projection equals `value` is found. If an iterator is desired, `std::ranges::lower_bound` should be used instead.

## Possible implementation

eq fun|1=
struct binary_search_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity, class T = std::projected_value_t<I, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<I, Proj>> Comp = ranges::less>
constexpr bool operator()(I first, S last, const T& value,
Comp comp = {}, Proj proj = {}) const
{
auto x = ranges::lower_bound(first, last, value, comp, proj);
return (!(x == last) && !(std::invoke(comp, value, std::invoke(proj, *x))));
}
template<ranges::forward_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_strict_weak_order
<const T*, std::projected<ranges::iterator_t<R>,
Proj>> Comp = ranges::less>
constexpr bool operator()(R&& r, const T& value, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), value,
std::move(comp), std::move(proj));
}
};
inline constexpr binary_search_fn binary_search;

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <iostream>
#include <ranges>
#include <vector>

int main()
{
    constexpr static auto haystack = {1, 3, 4, 5, 9};
    static_assert(std::ranges::is_sorted(haystack));

    for (const int needle : std::views::iota(1)
                          {{!
```

{
std::cout << "Searching for " << needle << ": ";
std::ranges::binary_search(haystack, needle)
? std::cout << "found " << needle << '\n'
: std::cout << "no dice!\n";
}
using CD = std::complex<double>;
std::vector<CD> nums1, 1}, {2, 3}, {4, 2}, {4, 3;
auto cmpz = [](CD x, CD y){ return abs(x) < abs(y); };
#ifdef __cpp_lib_algorithm_default_value_type
assert(std::ranges::binary_search(nums, {4, 2}, cmpz));
#else
assert(std::ranges::binary_search(nums, CD{4, 2}, cmpz));
#endif
}
|output=
Searching for 1: found 1
Searching for 2: no dice!
Searching for 3: found 3

## See also


| cpp/algorithm/ranges/dsc equal_range | (see dedicated page) |
| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |
| cpp/algorithm/dsc binary_search | (see dedicated page) |

