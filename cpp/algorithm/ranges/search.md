---
title: std::ranges::search
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/search
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity,
class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr ranges::subrange<I1>
search( I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>, Pred, Proj1, Proj2>
constexpr ranges::borrowed_subrange_t<R1>
search( R1&& r1, R2&& r2, Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
```

1. Searches for the ''first'' occurrence of the sequence of elements [first2, last2) in the range [first1, last1). Elements are compared using binary predicate `pred` after being projected with `proj2` and `proj1`, respectively.
2. Same as , but uses `r1` as the first source range and `r2` as the second source range, as if using `ranges::begin(r1)` as `first1`, `ranges::end(r1)` as `last1`, `ranges::begin(r2)` as `first2`, and `ranges::end(r2)` as `last2`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `r1` - the range of elements to examine (aka ''haystack'')
- `r2` - the range of elements to search for (aka ''needle'')
- `pred` - binary predicate to apply to the projected elements
- `proj1` - projection to apply to the elements in the first range
- `proj2` - projection to apply to the elements in the second range

## Return value

1. Returns a `ranges::subrange` value that is the first occurrence of the sequence [first2, last2) (aka ''needle'') in the range [first1, last1) (aka ''haystack''), after application of the projections `proj1` and `proj2` to the elements of both sequences respectively with consequencing application of the binary predicate `pred` to compare projected elements.
If no such occurrence is found, } is returned.
If the range to search for (aka ''needle'') is empty, that is `1=first2 == last2`, then the } is returned.
2. Same as  but the return type is `ranges::borrowed_subrange_t<R1>`.

## Complexity

At most `S * N` applications of the corresponding predicate and each projection, where <br>
`1=S = ranges::distance(first2, last2)` and `1=N = ranges::distance(first1, last1)`; <br>
`1=S = ranges::distance(r2)` and `1=N = ranges::distance(r1)`.

## Possible implementation

eq fun| 1=
struct search_fn
{
template<std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr ranges::subrange<I1>
operator()(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
for (;; ++first1)
{
I1 it1 = first1;
for (I2 it2 = first2;; ++it1, ++it2)
{
if (it2 == last2)
return {first1, it1};
if (it1 == last1)
return {it1, it1};
if (!std::invoke(pred, std::invoke(proj1, *it1), std::invoke(proj2, *it2)))
break;
}
}
}
template<ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>, Pred, Proj1, Proj2>
constexpr ranges::borrowed_subrange_t<R1>
operator()(R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2),
std::move(pred), std::move(proj1), std::move(proj2));
}
};
inline constexpr search_fn search {};

## Example


### Example


**Output:**
```
1) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
2) search("abcd abcd", "bcd"); found: "bcd"; subrange: {1, 4}
3) search("abcd abcd", ""); not found; subrange: {0, 0}
4) search("abcd abcd", "efg"); not found; subrange: {9, 9}
5) search("abcd abcd", "234"); found: "bcd"; subrange: {1, 4}
```


## See also


| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |
| cpp/algorithm/ranges/dsc includes | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/algorithm/ranges/dsc search_n | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |

