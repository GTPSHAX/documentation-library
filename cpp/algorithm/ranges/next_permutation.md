---
title: std::ranges::next_permutation
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/next_permutation
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr next_permutation_result<I>
next_permutation( I first, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::bidirectional_range R, class Comp = ranges::less,
class Proj = std::identity >
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr next_permutation_result<ranges::borrowed_iterator_t<R>>
next_permutation( R&& r, Comp comp = {}, Proj proj = {} );
dcl|since=c++20|num=3|1=
template< class I >
using next_permutation_result = ranges::in_found_result<I>;
```

1. Transforms the range [first, last) into the next [permutation](https://en.wikipedia.org/wiki/permutation), where the set of all permutations is ordered ''lexicographically'' with respect to binary comparison function object `comp` and projection function object `proj`. Returns } if such a ''"next permutation"'' exists; otherwise transforms the range into the lexicographically first permutation (an ascending order), and returns }.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to ''permute'', sentinel=yes}})` - 
- `r` - the  of elements to ''permute''
- `comp` - comparison *FunctionObject* which returns `true` if the first argument is ''less'' than the second
- `proj` - projection to apply to the elements

## Return value

1. } if the new permutation is lexicographically ''greater'' than the old one. } if the last permutation was reached and the range was reset to the first permutation.
2. Same as  except that the return type is `ranges::next_permutation_result<ranges::borrowed_iterator_t<R>>`.

## Exceptions

Any exceptions thrown from iterator operations or the element swap.

## Complexity

At most  swaps, where  is `ranges::distance(first, last)` in case  or `ranges::distance(r)` in case . Averaged over the entire sequence of permutations, typical implementations use about 3 comparisons and 1.5 swaps per call.

## Notes


## Possible implementation

eq fun|1=
struct next_permutation_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity>
requires std::sortable<I, Comp, Proj>
constexpr ranges::next_permutation_result<I>
operator()(I first, S last, Comp comp = {}, Proj proj = {}) const
{
// check that the sequence has at least two elements
if (first == last)
return {std::move(first), false};
I i_last{ranges::next(first, last)};
I i{i_last};
if (first == --i)
return {std::move(i_last), false};
// main "permutating" loop
for (;;)
{
I i1{i};
if (std::invoke(comp, std::invoke(proj, *--i), std::invoke(proj, *i1)))
{
I j{i_last};
while (!std::invoke(comp, std::invoke(proj, *i), std::invoke(proj, *--j)))
{}
std::iter_swap(i, j);
std::reverse(i1, i_last);
return {std::move(i_last), true};
}
// permutation "space" is exhausted
if (i == first)
{
std::reverse(first, i_last);
return {std::move(i_last), false};
}
}
}
template<ranges::bidirectional_range R, class Comp = ranges::less,
class Proj = std::identity>
requires std::sortable<ranges::iterator_t<R>, Comp, Proj>
constexpr ranges::next_permutation_result<ranges::borrowed_iterator_t<R>>
operator()(R&& r, Comp comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r),
std::move(comp), std::move(proj));
}
};
inline constexpr next_permutation_fn next_permutation {};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <compare>
#include <functional>
#include <iostream>
#include <string>

struct S
{
    char c;
    int i;
    auto operator<=>(const S&) const = default;
    friend std::ostream& operator<<(std::ostream& os, const S& s)
    {
        return os << "{'" << s.c << "', " << s.i << "}";
    }
};

auto print = [](auto const& v, char term = ' ')
{
    std::cout << "{ ";
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '}' << term;
};

int main()
{
    std::cout << "Generate all permutations (iterators case):\n";
    std::string s{"abc"};
    do
    {
        print(s);
    }
    while (std::ranges::next_permutation(s.begin(), s.end()).found);

    std::cout << "\n" "Generate all permutations (range case):\n";
    std::array a{'a', 'b', 'c'};
    do
    {
        print(a);
    }
    while (std::ranges::next_permutation(a).found);

    std::cout << "\n" "Generate all permutations using comparator:\n";
    using namespace std::literals;
    std::array z{"█"s, "▄"s, "▁"s};
    do
    {
        print(z);
    }
    while (std::ranges::next_permutation(z, std::greater()).found);

    std::cout << "\n" "Generate all permutations using projection:\n";
    std::array<S, 3> r{S{'A',3}, S{'B',2}, S{'C',1}<!---->};
    do
    {
        print(r, '\n');
    }
    while (std::ranges::next_permutation(r, {}, &S::c).found);
}
```


**Output:**
```
Generate all permutations (iterators case):
{ a b c } { a c b } { b a c } { b c a } { c a b } { c b a }
Generate all permutations (range case):
{ a b c } { a c b } { b a c } { b c a } { c a b } { c b a }
Generate all permutations using comparator:
{ █ ▄ ▁ } { █ ▁ ▄ } { ▄ █ ▁ } { ▄ ▁ █ } { ▁ █ ▄ } { ▁ ▄ █ }
Generate all permutations using projection:
{ {'A', 3} {'B', 2} {'C', 1} }
{ {'A', 3} {'C', 1} {'B', 2} }
{ {'B', 2} {'A', 3} {'C', 1} }
{ {'B', 2} {'C', 1} {'A', 3} }
{ {'C', 1} {'A', 3} {'B', 2} }
{ {'C', 1} {'B', 2} {'A', 3} }
```


## See also


| cpp/algorithm/ranges/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_permutation | (see dedicated page) |
| cpp/algorithm/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/dsc is_permutation | (see dedicated page) |

