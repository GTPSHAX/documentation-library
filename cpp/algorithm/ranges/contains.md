---
title: std::ranges::contains
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/contains
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|since1=c++23|until1=c++26|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S,
class T,
class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr bool contains( I first, S last, const T& value, Proj proj = {} );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr bool contains( I first, S last, const T& value, Proj proj = {} );
dcl rev multi|num=2|since1=c++23|until1=c++26|dcl1=
template< ranges::input_range R,
class T,
class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr bool contains( R&& r, const T& value, Proj proj = {} );
|dcl2=
template< ranges::input_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr bool contains( R&& r, const T& value, Proj proj = {} );
dcla|num=3|since=c++23|1=
template< std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool contains_subrange( I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=4|since=c++23|1=
template< ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable
<ranges::iterator_t<R1>, ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool contains_subrange( R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=5|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
bool contains( Ep&& policy, I first, S last, const T& value, Proj proj = {} );
dcl|num=6|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
bool contains( Ep&& policy, R&& r, const T& value, Proj proj = {} );
dcl|num=7|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I1, std::sized_sentinel_for<I1> S1,
std::random_access_iterator I2, std::sized_sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
bool contains_subrange( Ep&& policy, I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=8|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R1, /*sized-random-access-range*/ R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable
<ranges::iterator_t<R1>, ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
bool contains_subrange( Ep&& policy, R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
@1,2@ Checks whether or not the source range contains the target value `value`.
:@1@ The source range is [first, last).
:@2@ The source range is `r`.
@3,4@ Checks whether or not the target range is a subrange of the source range.
:@3@ The source range is [first1, last1), and the target range is [first2, last2).
:@4@ The source range is `r1`, and the target range is `r2`.
@5-8@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[first/first1, last/last1)` - 
- `[first2, last2)` - 
- `r/r1` - the source range
- `value` - the target value
- `r2` - the target range
- `pred/pred1` - the predicate to be applied to the (projected) elements in the source range
- `pred2` - the predicate to be applied to the (projected) elements in the target range
- `proj/proj1` - the projection to be applied to the elements in the source range
- `proj2` - the projection to be applied to the elements in the target range
- `policy` - execution policy

## Return value

1. `1=ranges::find(std::move(first), last, value, proj) != last`
2. `1=ranges::find(r, value, proj) != ranges::end(r)`
3. `1=first2 == last2
4. `ranges::empty(r2)
@5-8@ Same as , but inserts `std::forward<Ep>(policy)` to the argument list of  or  as the first argument.

## Complexity

Given
*  as `ranges::distance(first, last)` or `ranges::distance(r)`,
*  as `ranges::distance(first1, last1)` or `ranges::distance(r1)`, and
*  as `ranges::distance(first2, last2)` or `ranges::distance(r2)`:
@1,2@ At most  comparisons and applications of `proj`.
@3,4@ At most ·N applications of `pred` and `proj`.
@5,6@ } comparisons and applications of `proj`.
@7,8@ } applications of `pred` and `proj`.

## Exceptions

@5-8@

## Notes

In C++20, one may implement `contains` with `1=ranges::find(haystack, needle) != ranges::end(haystack)` or `contains_subrange` with `1=!ranges::search(haystack, needle).empty()`.
`ranges::contains_subrange`, like `ranges::search`, and unlike `std::search`, has no support for  (such as `std::boyer_moore_searcher`).

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_ranges_contains` | 202207L | C++23 | `ranges::contains` and `ranges::contains_subrange` |
| `__cpp_lib_algorithm_default_value_type` | 202403L | C++26 | List-initialization for algorithms |


## Possible implementation

eq impl
|title1=contains (1,2)|ver1=1|1=
struct contains_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>>
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr bool operator()(I first, S last, const T& value, Proj proj = {}) const
{
return ranges::find(std::move(first), last, value, proj) != last;
}
template<ranges::input_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>>
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr bool operator()(R&& r, const T& value, Proj proj = {}) const
{
return ranges::find(r, value, proj) != ranges::end(r);
}
};
inline constexpr contains_fn contains{};
|title2=contains_subrange (3,4)|ver2=3|2=
struct contains_subrange_fn
{
template<std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool operator()(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (first2 == last2)
!ranges::search(first1, last1, first2, last2,
pred, proj1, proj2).empty();
}
template<ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>, Pred, Proj1, Proj2>
constexpr bool operator()(R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return ranges::empty(r2)
!ranges::search(r1, r2, pred, proj1, proj2).empty();
}
};
inline constexpr contains_subrange_fn contains_subrange{};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <complex>

namespace ranges = std::ranges;

int main()
{
    constexpr auto haystack = std::array{3, 1, 4, 1, 5};
    constexpr auto needle = std::array{1, 4, 1};
    constexpr auto bodkin = std::array{2, 5, 2};

    static_assert
    (
        ranges::contains(haystack, 4) &&
       !ranges::contains(haystack, 6) &&
        ranges::contains_subrange(haystack, needle) &&
       !ranges::contains_subrange(haystack, bodkin)
    );

    constexpr std::array<std::complex<double>, 3> nums{<!---->{<!---->{1, 2}, {3, 4}, {5, 6}<!---->}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        static_assert(ranges::contains(nums, {3, 4}));
    #else
        static_assert(ranges::contains(nums, std::complex<double>{3, 4}));
    #endif
}
```


## See also


| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc binary_search | (see dedicated page) |
| cpp/algorithm/ranges/dsc includes | (see dedicated page) |
| cpp/algorithm/ranges/dsc all_any_none_of | (see dedicated page) |

