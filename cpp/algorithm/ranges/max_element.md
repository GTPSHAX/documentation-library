---
title: std::ranges::max_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/max_element
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less >
constexpr I
max_element( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::forward_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
constexpr ranges::borrowed_iterator_t<R>
max_element( R&& r, Comp comp = {}, Proj proj = {} );
```

1. Finds the greatest element in the range [first, last).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the  to examine
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

Iterator to the greatest element in the range [first, last). If several elements in the range are equivalent to the greatest element, returns the iterator to the first such element. Returns the iterator that compares equal to `last` if the range is empty (i.e. if `1=first == last`).

## Complexity

Exactly $max(N - 1, 0)$ comparisons, where `1=N = ranges::distance(first, last)`.

## Possible implementation

eq fun
|1=
struct max_element_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_strict_weak_order<std::projected<I, Proj>> Comp = ranges::less>
constexpr I operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
if (first == last)
return last;
auto largest = first;
while (++first != last)
if (std::invoke(comp, std::invoke(proj, *largest), std::invoke(proj, *first)))
largest = first;
return largest;
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
inline constexpr max_element_fn max_element;

## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>

int main()
{
    namespace ranges = std::ranges;

    const auto v = {3, 1, -14, 1, 5, 9, -14, 9};

    auto result = ranges::max_element(v.begin(), v.end());
    std::cout << "Max element at pos " << ranges::distance(v.begin(), result) << '\n';

    auto abs_compare = [](int a, int b) { return std::abs(a) < std::abs(b); };
    result = ranges::max_element(v, abs_compare);
    std::cout << "Absolute max element at pos "
              << ranges::distance(v.begin(), result) << '\n';
}
```


**Output:**
```
Max element at pos 5
Absolute max element at pos 2
```


## See also


| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/dsc max_element | (see dedicated page) |

