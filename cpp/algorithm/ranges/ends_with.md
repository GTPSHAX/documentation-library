---
title: std::ranges::ends_with
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/ends_with
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires (std::forward_iterator<I1>  std::sized_sentinel_for<S1, I1>) &&
(std::forward_iterator<I2>  std::sized_sentinel_for<S2, I2>) &&
std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool ends_with( I1 first1, S1 last1,
I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcla|num=2|since=c++23|1=
template< ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires (ranges::forward_range<R1>  ranges::sized_range<R1>) &&
(ranges::forward_range<R2>  ranges::sized_range<R2>) &&
std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool ends_with( R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
```

Checks whether the second range matches the suffix of the first range.
1. Let `N1` be `ranges::distance(first1, last1)` and `N2` be `ranges::distance(first2, last2)`:
* If `N1 < N2` is `true`, returns `false`.
* Otherwise, returns .
2. Let `N1` be `ranges::distance(r1)` and `N2` be `ranges::distance(r2)`.
* If `N1 < N2` is `true`, returns `false`.
* Otherwise, returns .

## Parameters


### Parameters

- `[first1, last1)` - 
- `r1` - the range of elements to examine
- `[first2, last2)` - 
- `r2` - the range of elements to be used as the suffix
- `pred` - the binary predicate that compares the projected elements
- `proj1` - the projection to apply to the elements of the range to examine
- `proj2` - the projection to apply to the elements of the range to be used as the suffix

## Return value

`true` if the second range matches the suffix of the first range, `false` otherwise.

## Complexity

Generally linear: at most  applications of the predicate and both projections. The predicate and both projections are not applied if `N1 < N2` is `true`.
If both `N1` and `N2` can be calculated in constant time (i.e. both iterator-sentinel type pairs model , or both range types model ) and `N1 < N2` is `true`, the time complexity is constant.

## Possible implementation

eq fun|1=
struct ends_with_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires (std::forward_iterator<I1>  std::sized_sentinel_for<S1, I1>) &&
(std::forward_iterator<I2>  std::sized_sentinel_for<S2, I2>) &&
std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool operator()(I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
const auto n1 = ranges::distance(first1, last1);
const auto n2 = ranges::distance(first2, last2);
if (n1 < n2)
return false;
ranges::advance(first1, n1 - n2);
return ranges::equal(std::move(first1), last1,
std::move(first2), last2,
pred, proj1, proj2);
}
template<ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires (ranges::forward_range<R1>  ranges::sized_range<R1>) &&
(ranges::forward_range<R2>  ranges::sized_range<R2>) &&
std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool operator()(R1&& r1, R2&& r2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
const auto n1 = ranges::distance(r1);
const auto n2 = ranges::distance(r2);
if (n1 < n2)
return false;
return ranges::equal(views::drop(ranges::ref_view(r1),
n1 - static_cast<decltype(n1)>(n2)),
r2, pred, proj1, proj2);
}
};
inline constexpr ends_with_fn ends_with{};

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <array>

static_assert
(
    ! std::ranges::ends_with("for", "cast") &&
    std::ranges::ends_with("dynamic_cast", "cast") &&
    ! std::ranges::ends_with("as_const", "cast") &&
    std::ranges::ends_with("bit_cast", "cast") &&
    ! std::ranges::ends_with("to_underlying", "cast") &&
    std::ranges::ends_with(std::array{1, 2, 3, 4}, std::array{3, 4}) &&
    ! std::ranges::ends_with(std::array{1, 2, 3, 4}, std::array{4, 5})
);

int main() {}
```


## Defect reports


## See also


| cpp/algorithm/ranges/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |

