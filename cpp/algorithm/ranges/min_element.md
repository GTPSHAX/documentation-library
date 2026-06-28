---
title: std::ranges::min_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/min_element
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less >
constexpr I
min_element( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
min_element( R&& r, Comp comp = {}, Proj proj = {} );
```

1. Finds the smallest element in the range [first, last).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the  to examine
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

Iterator to the smallest element in the range [first, last). If several elements in the range are equivalent to the smallest element, returns the iterator to the first such element. Returns the iterator that compares equal to `last` if the range is empty (i.e., `1=first == last`).

## Complexity

Exactly $max(N - 1, 0)$ comparisons, where `1=N = ranges::distance(first, last)`.

## Possible implementation

eq fun
|1=
struct min_element_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
if (first == last)
return last;
auto smallest = first;
while (++first != last)
if (std::invoke(comp, std::invoke(proj, *first), std::invoke(proj, *smallest)))
smallest = first;
return smallest;
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
inline constexpr min_element_fn min_element;

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>

int main()
{
    namespace ranges = std::ranges;

    std::array v{3, 1, -13, 1, 3, 7, -13};

    auto iterator = ranges::min_element(v.begin(), v.end());
    auto position = ranges::distance(v.begin(), iterator);
    std::cout << "min element is v[" << position << "] == " << *iterator << '\n';

    auto abs_compare = [](int a, int b) { return (std::abs(a) < std::abs(b)); };
    iterator = ranges::min_element(v, abs_compare);
    position = ranges::distance(v.begin(), iterator);
    std::cout << "{{!
```

}
|output=
min element is v[2] == -13
|min| element is v[1] == 1

## See also


| cpp/algorithm/ranges/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/dsc min_element | (see dedicated page) |

