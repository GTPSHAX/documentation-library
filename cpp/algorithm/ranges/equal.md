---
title: std::ranges::equal
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/equal
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool
equal( I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<ranges::iterator_t<R1>, ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool
equal( R1&& r1, R2&& r2, Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
```

1. Returns `true` if the projected values of the range [first1, last1) are equal to the projected values of the range [first2, last2), and `false` otherwise.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
Two ranges are considered equal if they have the same number of elements and every pair of corresponding projected elements satisfies `pred`. That is, `std::invoke(pred, std::invoke(proj1, *first1), std::invoke(proj2, *first2))` returns `true` for all pairs of corresponding elements in both ranges.

## Parameters


### Parameters

- `[first1, last1)` - 
- `r1` - the first range of the elements to compare
- `[first2, last2)` - 
- `r2` - the second range of the elements to compare
- `pred` - binary predicate to apply to the projected elements
- `proj1` - projection to apply to the first range of elements
- `proj2` - projection to apply to the second range of elements

## Return value

If the length of the range [first1, last1) does not equal the length of the range [first2, last2), returns `false`.
If the elements in the two ranges are equal after projection, returns `true`.
Otherwise returns `false`.

## Notes

`ranges::equal` should not be used to compare the ranges formed by the iterators from `std::unordered_set`, `std::unordered_multiset`, `std::unordered_map`, or `std::unordered_multimap` because the order in which the elements are stored in those containers may be different even if the two containers store the same elements.
When comparing entire containers or string views for equality, `1=operator==` for the corresponding type are usually preferred.
`ranges::equal` is not guaranteed to be short-circuit. E.g. if the first pair elements of both ranges do not compare equal, the rest of elements may also be compared. Non-short-circuit comparison may happen when the ranges are compared with `std::memcmp` or implementation-specific vectorized algorithms.

## Complexity

At most `min(last1 - first1, last2 - first2)` applications of the predicate and corresponding projections.
However, if `S1` and `S2` both model `std::sized_sentinel_for` their respective iterators, and `last1 - first1 ! then no applications of the predicate are made (size mismatch is detected without looking at any elements).

## Possible implementation

eq fun
|1=
struct equal_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr bool
operator()(I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
if constexpr (std::sized_sentinel_for<S1, I1> and std::sized_sentinel_for<S2, I2>)
if (std::ranges::distance(first1, last1) != std::ranges::distance(first2, last2))
return false;
for (; first1 != last1; ++first1, (void)++first2)
if (!std::invoke(pred, std::invoke(proj1, *first1), std::invoke(proj2, *first2)))
return false;
return true;
}
template<ranges::input_range R1, ranges::input_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>, ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr bool
operator()(R1&& r1, R2&& r2, Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2),
std::ref(pred), std::ref(proj1), std::ref(proj2));
}
};
inline constexpr equal_fn equal;

## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <ranges>
#include <string_view>

constexpr bool is_palindrome(const std::string_view s)
{
    namespace views = std::views;
    auto forward = s {{!
```

auto backward = s | views::reverse | views::take(s.size() / 2);
return std::ranges::equal(forward, backward);
}
void test(const std::string_view s)
{
std::cout << std::quoted(s) << " is "
<< (is_palindrome(s) ? "" : "not ")
<< "a palindrome\n";
}
int main()
{
test("radar");
test("hello");
static_assert(is_palindrome("ABBA") and not is_palindrome("AC/DC"));
}
|output=
"radar" is a palindrome
"hello" is not a palindrome

## See also


| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc lexicographical_compare | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal_range | (see dedicated page) |
| cpp/utility/functional/dsc equal_to | (see dedicated page) |
| cpp/algorithm/dsc equal | (see dedicated page) |

