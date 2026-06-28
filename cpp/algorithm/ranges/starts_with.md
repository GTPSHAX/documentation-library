---
title: std::ranges::starts_with
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/starts_with
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool
starts_with( I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++23|1=
template< ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool
starts_with( R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
```

Checks whether the second range matches the prefix of the first range.
1. Let `N1` and `N2` denote the size of ranges [first1, last1) and [first2, last2) respectively. If `N1 < N2`, returns `false`. Otherwise, returns `true` only if every element in the range [first2, last2) is equal to the corresponding element in [first1, first1 + N2). Comparison is done by applying the binary predicate `pred` to elements in two ranges projected by `proj1` and `proj2` respectively.
2. Same as , but uses `r1` and `r2` as the source ranges, as if using `ranges::begin(r1)` as `first1`, `ranges:begin(r2)` as `first2`, `ranges::end(r1)` as `last1`, and `ranges::end(r2)` as `last2`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `r1` - the range of elements to examine
- `[first2, last2)` - 
- `r2` - the range of elements to be used as the prefix
- `pred` - the binary predicate that compares the projected elements
- `proj1` - the projection to apply to the elements of the range to examine
- `proj2` - the projection to apply to the elements of the range to be used as the prefix

## Return value

`true` if the second range matches the prefix of the first range, `false` otherwise.

## Complexity

Linear: at most `min(N1, N2)` applications of the predicate and both projections.

## Possible implementation

eq fun|1=
struct starts_with_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool operator()(I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return ranges::mismatch(std::move(first1), last1, std::move(first2), last2,
std::move(pred), std::move(proj1), std::move(proj2)
).in2 == last2;
}
template<ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool operator()(R1&& r1, R2&& r2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2),
std::move(pred), std::move(proj1), std::move(proj2));
}
};
inline constexpr starts_with_fn starts_with {};

## Notes


## Example

| std::views::take(3)));
}
|output=true false true false

## See also


| cpp/algorithm/ranges/dsc ends_with | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |

