---
title: std::ranges::swap_ranges
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/swap_ranges
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2 >
requires std::indirectly_swappable<I1, I2>
constexpr swap_ranges_result<I1, I2>
swap_ranges( I1 first1, S1 last1, I2 first2, S2 last2 );
dcl|num=2|since=c++20|1=
template< ranges::input_range R1, ranges::input_range R2 >
requires std::indirectly_swappable<ranges::iterator_t<R1>, ranges::iterator_t<R2>>
constexpr swap_ranges_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>>
swap_ranges( R1&& r1, R2&& r2 );
dcl|num=3|since=c++20|1=
template< class I1, class I2 >
using swap_ranges_result = ranges::in_in_result<I1, I2>;
```

1. Exchanges elements between first range [first1, first1 + M) and second range [first2, first2 + M) via `ranges::iter_swap(first1 + i, first2 + i)`, where `1= M = ranges::min(ranges::distance(first1, last1), ranges::distance(first2, last2))`.
@@ The ranges [first1, last1) and [first2, last2) must not overlap.
2. Same as , but uses `r1` as the first range and `r2` as the second range, as if using `ranges::begin(r1)` as `first1`, `ranges::end(r1)` as `last1`, `ranges::begin(r2)` as `first2`, and `ranges::end(r2)` as `last2`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `r1` - the first range of elements to swap
- `r2` - the second range of elements to swap.

## Return value

}.

## Complexity

Exactly `M` swaps.

## Notes


## Possible implementation

eq fun|1=
struct swap_ranges_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2>
requires std::indirectly_swappable<I1, I2>
constexpr ranges::swap_ranges_result<I1, I2>
operator()(I1 first1, S1 last1, I2 first2, S2 last2) const
{
for (; !(first1 == last1 or first2 == last2); ++first1, ++first2)
ranges::iter_swap(first1, first2);
return {std::move(first1), std::move(first2)};
}
template<ranges::input_range R1, ranges::input_range R2>
requires std::indirectly_swappable<ranges::iterator_t<R1>, ranges::iterator_t<R2>>
constexpr ranges::swap_ranges_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>>
operator()(R1&& r1, R2&& r2) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2));
}
};
inline constexpr swap_ranges_fn swap_ranges {};

## Example


### Example


**Output:**
```
p : A B C D E
q : 1 2 3 4 5 6

p : 2 3 C D E
q : 1 A B 4 5 6

p : 1 A B 4 5
q : 2 3 C D E 6
```


## See also


| cpp/iterator/ranges/dsc iter_swap | (see dedicated page) |
| cpp/utility/ranges/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/algorithm/dsc iter_swap | (see dedicated page) |
| cpp/algorithm/dsc swap | (see dedicated page) |

