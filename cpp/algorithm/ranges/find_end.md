---
title: std::ranges::find_end
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/find_end
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr ranges::subrange<I1>
find_end( I1 first1, S1 last1, I2 first2, S2 last2,
Pred pred = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++20|1=
template< ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr ranges::borrowed_subrange_t<R1>
find_end( R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=3|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I1, std::sized_sentinel_for<I1> S1,
std::random_access_iterator I2, std::sized_sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = identity, class Proj2 = identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
ranges::subrange<I1> find_end( Ep&& policy, I1 first1, S1 last1,
I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=4|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R1,
/*sized-random-access-range*/ R2,
class Pred = ranges::equal_to,
class Proj1 = identity, class Proj2 = identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
ranges::borrowed_subrange_t<R1>
find_end( Ep&& policy, R1&& r1, R2&& r2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
Searches for the last occurrence of the target range in the source range. The elements (projected by `proj1` and `proj2` respectively) are compared using the binary predicate `pred`.
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

A subrange corresponding to the last occurrence of the target range in the source range.
If the target range is empty or it does not appear in the source range, an empty range is returned.

## Complexity

Given  as `ranges::distance(first1, last1)` or `ranges::distance(r1)`, and  as `ranges::distance(first2, last2)` or `ranges::distance(r2)`:
@1,2@ At most ⋅(N-N+1) applications of `pred` and `proj`.
@3,4@ } applications of `pred` and `proj`.

## Exceptions

@3,4@

## Notes

An implementation can improve efficiency of the search if the iterator types model  by searching from the end towards the begin. Modelling  may improve the comparison speed. All this however does not change the theoretical complexity of the worst case.

## Possible implementation

eq fun|1=
struct find_end_fn
{
template<std::forward_iterator I1, std::sentinel_for<I1> S1,
std::forward_iterator I2, std::sentinel_for<I2> S2,
class Pred = ranges::equal_to,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_comparable<I1, I2, Pred, Proj1, Proj2>
constexpr ranges::subrange<I1>
operator()(I1 first1, S1 last1, I2 first2, S2 last2, Pred pred = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
if (first2 == last2)
{
auto last_it = ranges::next(first1, last1);
return {last_it, last_it};
}
auto result = ranges::search(std::move(first1), last1,
first2, last2, pred, proj1, proj2);
if (result.empty())
return result;
for (;;)
{
auto new_result = ranges::search(std::next(result.begin()), last1,
first2, last2, pred, proj1, proj2);
if (new_result.empty())
return result;
else
result = std::move(new_result);
}
}
template<ranges::forward_range R1, ranges::forward_range R2,
class Pred = ranges::equal_to,
class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_comparable<ranges::iterator_t<R1>,
ranges::iterator_t<R2>,
Pred, Proj1, Proj2>
constexpr ranges::borrowed_subrange_t<R1>
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
inline constexpr find_end_fn find_end{};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cctype>
#include <iostream>
#include <ranges>
#include <string_view>

void print(const auto haystack, const auto needle)
{
    const auto pos = std::distance(haystack.begin(), needle.begin());
    std::cout << "In \"";
    for (const auto c : haystack)
        std::cout << c;
    std::cout << "\" found \"";
    for (const auto c : needle)
        std::cout << c;
    std::cout << "\" at position [" << pos << ".." << pos + needle.size() << ")\n"
        << std::string(4 + pos, ' ') << std::string(needle.size(), '^') << '\n';
}

int main()
{
    using namespace std::literals;
    using std::ranges::find_end;

    constexpr auto secret{"password password word..."sv};
    constexpr auto wanted{"password"sv};

    constexpr auto found1 = find_end(secret.cbegin(), secret.cend(),
                                     wanted.cbegin(), wanted.cend());
    print(secret, found1);

    constexpr auto found2 = find_end(secret, "word"sv);
    print(secret, found2);

    const auto found3 = find_end(secret, "ORD"sv,
        [](const char x, const char y)
        { // uses a binary predicate
            return std::tolower(x) == std::tolower(y);
        });
    print(secret, found3);

    const auto found4 = find_end(secret, "SWORD"sv, {}, {},
        [](char c) { return std::tolower(c); }); // projects the 2nd range
    print(secret, found4);

    static_assert(find_end(secret, "PASS"sv).empty()); // => not found
}
```


**Output:**
```
In "password password word..." found "password" at position [9..17)
             ^^^^^^^^
In "password password word..." found "word" at position [18..22)
                      ^^^^
In "password password word..." found "ord" at position [19..22)
                       ^^^
In "password password word..." found "sword" at position [12..17)
                ^^^^^
```


## See also


| cpp/algorithm/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc search_n | (see dedicated page) |

