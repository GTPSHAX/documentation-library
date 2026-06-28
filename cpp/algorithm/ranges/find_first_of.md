---
title: std::ranges::find_first_of
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/find_first_of
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr I1
find_first_of( I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr ranges::borrowed_iterator_t<R1>
find_first_of( R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=3|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I1, std::sized_sentinel_for<I1> S1,
std::random_access_iterator I2, std::sized_sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
I1 find_first_of( Ep&& policy, I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=4|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R1,
/*sized-random-access-range*/ R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
ranges::borrowed_iterator_t<R1>
find_first_of( Ep&& policy, R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
Searches the source range for any of the elements in the target range. The elements (projected by `proj1` and `proj2` respectively) are compared using the binary predicate `pred`.
1. The source range is [first1, last1), and the target range is [first2, last2).
2. The source range is `r1`, and the target range is `r2`.
@3,4@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `r1` - the source range
- `r2` - the target range
- `pred` - the predicate to be applied to the (projected) elements
- `proj1` - the projection to be applied to the elements in the source range
- `proj2` - the projection to be applied to the elements in the target range
- `policy` - execution policy

## Return value

Iterator to the first element in the source range that matches an element from the target range.
If the target range is empty or if no such element is found, returns:
@1,3@ `last1`
@2,4@ `ranges::next(ranges::begin(r1), ranges::end(r1))`

## Complexity

Given  as `ranges::distance(first1, last1)` or `ranges::distance(r1)`, and  as `ranges::distance(first2, last2)` or `ranges::distance(r2)`:
@1,2@ At most ⋅N applications of `pred` and `proj`.
@3,4@ } applications of `pred` and `proj`.

## Exceptions

@3,4@

## Possible implementation

eq fun|1=
struct find_first_of_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr I1 operator()(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
for (; first1 != last1; ++first1)
for (auto i = first2; i != last2; ++i)
if (std::invoke(pred, std::invoke(proj1, *first1), std::invoke(proj2, *i)))
return first1;
return first1;
}
template<ranges::input_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr ranges::borrowed_iterator_t<R1>
operator()(R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2),
ranges::next(ranges::begin(r2), ranges::end(r2)),
std::move(pred), std::move(proj1), std::move(proj2));
}
template<ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr ranges::borrowed_iterator_t<R1>
operator()(R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1),
ranges::next(ranges::begin(r1), ranges::end(r1)),
ranges::begin(r2),
ranges::next(ranges::begin(r2), ranges::end(r2)),
std::move(pred), std::move(proj1), std::move(proj2));
}
};
inline constexpr find_first_of_fn find_first_of{};

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>

int main()
{
    using std::ranges::find_first_of;

    constexpr static auto haystack = {1, 2, 3, 4};
    constexpr static auto needles  = {0, 3, 4, 3};

    constexpr auto found1 = find_first_of(haystack.begin(), haystack.end(),
                                          needles.begin(), needles.end());
    static_assert(std::distance(haystack.begin(), found1) == 2);

    constexpr auto found2 = find_first_of(haystack, needles);
    static_assert(std::distance(haystack.begin(), found2) == 2);

    constexpr static auto negatives = {-6, -3, -4, -3};
    constexpr auto not_found = find_first_of(haystack, negatives);
    static_assert(not_found == haystack.end());

    constexpr auto found3 = find_first_of(haystack, negatives,
        [](int x, int y) { return x == -y; }); // uses a binary comparator
    static_assert(std::distance(haystack.begin(), found3) == 2);

    struct P { int x, y; };
    constexpr static auto p1 = {P{1, -1}, P{2, -2}, P{3, -3}, P{4, -4}<!---->};
    constexpr static auto p2 = {P{5, -5}, P{6, -3}, P{7, -5}, P{8, -3}<!---->};

    // Compare only P::y data members by projecting them:
    const auto found4 = find_first_of(p1, p2, {}, &P::y, &P::y);
    std::cout << "First equivalent element {" << found4->x << ", " << found4->y
              << "} was found at position " << std::distance(p1.begin(), found4)
              << ".\n";
}
```


**Output:**
```
First equivalent element {3, -3} was found at position 2.
```


## See also


| cpp/algorithm/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc search_n | (see dedicated page) |

