---
title: std::ranges::minmax_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/minmax_element
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less >
constexpr minmax_element_result<I>
minmax_element( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
constexpr minmax_element_result<ranges::borrowed_iterator_t<R>>
minmax_element( R&& r, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=3|1=
template< class I >
using minmax_element_result = ranges::min_max_result<I>;
```

1. Finds the smallest and largest elements in the range [first, last).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the  to examine
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements.

## Return value

An object consisting of an iterator to the smallest element as the first element and an iterator to the greatest element as the second. Returns } if the range is empty. If several elements are equivalent to the smallest element, the iterator to the first such element is returned. If several elements are equivalent to the largest element, the iterator to the last such element is returned.

## Complexity

At most `std::max(std::floor(1.5 * (N − 1)), 0.0)` applications of the comparison and twice as many applications of the projection, where `1=N = ranges::distance(first, last)`.

## Possible implementation

eq fun
|1=
struct minmax_element_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less>
constexpr ranges::minmax_element_result<I>
operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
auto min = first, max = first;
if (first == last  ++first == last)
return {min, max};
if (std::invoke(comp, std::invoke(proj, *first),
std::invoke(proj, *min)))
min = first;
else
max = first;
while (++first != last)
{
auto i = first;
if (++first == last)
{
if (std::invoke(comp, std::invoke(proj, *i),
std::invoke(proj, *min)))
min = i;
else if (!(std::invoke(comp, std::invoke(proj, *i),
std::invoke(proj, *max))))
max = i;
break;
}
else
{
if (std::invoke(comp, std::invoke(proj, *first),
std::invoke(proj, *i)))
{
if (std::invoke(comp, std::invoke(proj, *first),
std::invoke(proj, *min)))
min = first;
if (!(std::invoke(comp, std::invoke(proj, *i),
std::invoke(proj, *max))))
max = i;
}
else
{
if (std::invoke(comp, std::invoke(proj, *i),
std::invoke(proj, *min)))
min = i;
if (!(std::invoke(comp, std::invoke(proj, *first),
std::invoke(proj, *max))))
max = first;
}
}
}
return {min, max};
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less>
constexpr ranges::minmax_element_result<ranges::borrowed_iterator_t<R>>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(comp), std::ref(proj));
}
};
inline constexpr minmax_element_fn minmax_element;

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
namespace ranges = std::ranges;

int main()
{
    const auto v = {3, 9, 1, 4, 1, 2, 5, 9};
    const auto [min, max] = ranges::minmax_element(v);
    std::cout
        << "min = " << *min << ", at [" << ranges::distance(v.begin(), min) << "]\n"
        << "max = " << *max << ", at [" << ranges::distance(v.begin(), max) << "]\n";
}
```


**Output:**
```
min = 1, at [2]
max = 9, at [7]
```


## See also


| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |

