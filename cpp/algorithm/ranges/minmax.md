---
title: std::ranges::minmax
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/minmax
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr ranges::minmax_result<const T&>
minmax( const T& a, const T& b, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less >
constexpr ranges::minmax_result<T>
minmax( std::initializer_list<T> r, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=3|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less >
requires std::indirectly_copyable_storable<ranges::iterator_t<R>, ranges::range_value_t<R>*>
constexpr ranges::minmax_result<ranges::range_value_t<R>>
minmax( R&& r, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=4|1=
template< class T >
using minmax_result = ranges::min_max_result<T>;
```

Returns the smallest and the greatest of the given projected values.
1. Returns references to the smaller and the greater of `a` and `b`.
2. Returns the smallest and the greatest of the values in the initializer list `r`.
3. Returns the smallest and the greatest of the values in the range `r`.
For overloads , the behavior is undefined if the range is empty (as determined by `ranges::distance(r)`).

## Parameters


### Parameters

- `a, b` - the values to compare
- `r` - a non-empty range of values to compare
- `comp` - comparison to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

1. } if, according to their respective projected value, `b` is smaller than `a`; otherwise it returns }.
@2,3@ }, where `s` and `l` are respectively the smallest and largest values in `r`, according to their projected value. If several values are equivalent to the smallest and largest, returns the leftmost smallest value, and the rightmost largest value.

## Complexity

1. Exactly one comparison and two applications of the projection.
@2,3@ At most `3 / 2 * ranges::distance(r)` comparisons and twice as many applications of the projection.

## Possible implementation

eq fun
|1=
struct minmax_fn
{
template<class T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr ranges::minmax_result<const T&>
operator()(const T& a, const T& b, Comp comp = {}, Proj proj = {}) const
{
if (std::invoke(comp, std::invoke(proj, b), std::invoke(proj, a)))
return {b, a};
return {a, b};
}
template<std::copyable T, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<const T*, Proj>> Comp = ranges::less>
constexpr ranges::minmax_result<T>
operator()(std::initializer_list<T> r, Comp comp = {}, Proj proj = {}) const
{
auto result = ranges::minmax_element(r, std::ref(comp), std::ref(proj));
return {*result.min, *result.max};
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_strict_weak_order<
std::projected<ranges::iterator_t<R>, Proj>> Comp = ranges::less>
requires std::indirectly_copyable_storable<ranges::iterator_t<R>,
ranges::range_value_t<R>*>
constexpr ranges::minmax_result<ranges::range_value_t<R>>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
auto first = ranges::begin(r);
const auto last = ranges::end(r);
auto min = static_cast<range_value_t<R>>(*first), max = min;
while (++first != last) {
auto x = static_cast<range_value_t<R>>(*first);
if (++first == last) {
if (std::invoke(comp, std::invoke(proj, x), std::invoke(proj, min)))
min = x;
else if (!std::invoke(comp, std::invoke(proj, x), std::invoke(proj, max)))
max = x;
break;
}
if (std::invoke(comp, std::invoke(proj, *first), std::invoke(proj, x))) {
if (std::invoke(comp, std::invoke(proj, *first), std::invoke(proj, min)))
min = *first;
if (!std::invoke(comp, std::invoke(proj, x), std::invoke(proj, max)))
max = x;
} else {
if (std::invoke(comp, std::invoke(proj, x), std::invoke(proj, min)))
min = x;
if (!std::invoke(comp, std::invoke(proj, *first), std::invoke(proj, max)))
max = *first;
}
}
return {min, max};
}
};
inline constexpr minmax_fn minmax;

## Notes

For overload , if one of the parameters is a temporary, the reference returned becomes a dangling reference at the end of the full expression that contains the call to `minmax`:

```cpp
int n = 1;
auto p = std::ranges::minmax(n, n + 1);
int m = p.min; // ok
int x = p.max; // undefined behavior

// Note that structured bindings have the same issue
auto [mm, xx] = std::ranges::minmax(n, n + 1);
xx; // undefined behavior
```


## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <random>

int main()
{
    namespace ranges = std::ranges;

    constexpr std::array v{3, 1, 4, 1, 5, 9, 2, 6, 5};

    std::random_device rd;
    std::mt19937_64 generator(rd());
    std::uniform_int_distribution<> distribution(0, ranges::distance(v)); // [0..9]

    // auto bounds = ranges::minmax(distribution(generator), distribution(generator));
    // UB: dangling references: bounds.min and bounds.max have the type `const int&`.

    const int x1 = distribution(generator);
    const int x2 = distribution(generator);
    auto bounds = ranges::minmax(x1, x2); // OK: got references to lvalues x1 and x2

    std::cout << "v[" << bounds.min << ":" << bounds.max << "]: ";
    for (int i = bounds.min; i < bounds.max; ++i)
        std::cout << v[i] << ' ';
    std::cout << '\n';

    auto [min, max] = ranges::minmax(v);
    std::cout << "smallest: " << min << ", " << "largest: " << max << '\n';
}
```


**Output:**
```
v[3:9]: 1 5 9 2 6 5 
smallest: 1, largest: 9
```


## See also


| cpp/algorithm/ranges/dsc min | (see dedicated page) |
| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |

