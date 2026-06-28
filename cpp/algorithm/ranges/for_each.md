---
title: std::ranges::for_each
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/for_each
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirectly_unary_invocable<std::projected<I, Proj>> Fun >
constexpr for_each_result<I, Fun>
for_each( I first, S last, Fun f, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirectly_unary_invocable
<std::projected<ranges::iterator_t<R>, Proj>> Fun >
constexpr for_each_result<ranges::borrowed_iterator_t<R>, Fun>
for_each( R&& r, Fun f, Proj proj = {} );
dcl|num=3|since=c++26|1=
template< /*execution-policy*/ Ep, std::random_access_iterator I,
std::sized_sentinel_for<I> S, class Proj = std::identity,
std::indirectly_unary_invocable<std::projected<I, Proj>> Fun >
I for_each( Ep&& policy, I first, S last, Fun f, Proj proj = {} );
dcl|num=4|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R, class Proj = std::identity,
std::indirectly_unary_invocable
<std::projected<ranges::iterator_t<R>, Proj>> Fun >
ranges::borrowed_iterator_t<R>
for_each( Ep&& policy, R&& r, Fun f, Proj proj = {} );
dcl|num=5|since=c++20|1=
template< class I, class F >
using for_each_result = ranges::in_fun_result<I, F>;
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
Applies the given invocable object `f` to each element (projected by `proj`) in the target range [first, last) or `r`. If `f` returns a result, the result is ignored.
@1,2@ `f` is applied in order from the beginning of the target range.
@3,4@ `f` might not be applied in order. The algorithm is executed according to `policy`.
@@ Unlike other , `for_each` is not allowed to make arbitrary copies of elements from the target range.

## Parameters


### Parameters

- `[range=target, simple=yes}})` - 
- `r` - the target range
- `f` - the invocable object to be applied to the (projected) elements
- `proj` - the projection to be applied to the elements
- `policy` - execution policy

## Return value

1. }
2. rev inl|since=c++26|} if `R` models , otherwise }
3. `last`
4. <sup>(since C++26)</sup> `ranges::next(ranges::begin(r), ranges::end(r))` if `R` models `ranges::end(r)`

## Complexity

@1,3@ Exactly `ranges::distance(first, last)` applications of `f` and `proj`.
@2,4@ Exactly `ranges::distance(r)` applications of `f` and `proj`.

## Exceptions

@3,4@

## Notes

If the projection returns a mutable reference, `f` may modify the elements in the target range.
For overloads , `f` can be a stateful invocable object. The invocable object in the return value can be considered as the final state of the batch operation.
For overloads , multiple copies of `f` may be created to perform parallel invocation. The return value does not contain an invocable object because parallelization often does not permit efficient state accumulation.

## Possible implementation

eq fun|1=
struct for_each_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirectly_unary_invocable<std::projected<I, Proj>> Fun>
constexpr ranges::for_each_result<I, Fun>
operator()(I first, S last, Fun f, Proj proj = {}) const
{
for (; first != last; ++first)
std::invoke(f, std::invoke(proj, *first));
return {std::move(first), std::move(f)};
}
template<ranges::input_range R, class Proj = std::identity,
std::indirectly_unary_invocable
<std::projected<ranges::iterator_t<R>, Proj>> Fun>
constexpr ranges::for_each_result<ranges::borrowed_iterator_t<R>, Fun>
operator()(R&& r, Fun f, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(f), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirectly_unary_invocable
<std::projected<ranges::iterator_t<R>, Proj>> Fun>
constexpr ranges::for_each_result<ranges::borrowed_iterator_t<R>, Fun>
operator()(R&& r, Fun f, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::move(f), std::ref(proj));
}
};
inline constexpr for_each_fn for_each;

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Sum
{
    void operator()(int n) { sum += n; }
    int sum {0};
};

int main()
{
    namespace ranges = std::ranges;

    std::vector<int> nums {3, 4, 2, 8, 15, 267};

    auto print = [](const auto& n) { std::cout << ' ' << n; };

    std::cout << "before:";
    ranges::for_each(std::as_const(nums), print);
    print('\n');

    ranges::for_each(nums, [](int& n) { ++n; });

    // calls Sum::operator() for each number
    auto [i, s] = ranges::for_each(nums.begin(), nums.end(), Sum());
    assert(i == nums.end());

    std::cout << "after: ";
    ranges::for_each(nums.cbegin(), nums.cend(), print);

    std::cout << "\n" "sum: " << s.sum << '\n';

    using pair = std::pair<int, std::string>; 
    std::vector<pair> pairs {{1,"one"}, {2,"two"}, {3,"tree"
```

std::cout << "project the pair::first: ";
ranges::for_each(pairs, print, [](const pair& p) { return p.first; });
std::cout << "\n" "project the pair::second:";
ranges::for_each(pairs, print, &pair::second);
print('\n');
}
|output=
before: 3 4 2 8 15 267
after:  4 5 3 9 16 268
sum: 305
project the pair::first:  1 2 3
project the pair::second: one two tree

## See also


| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/algorithm/ranges/dsc for_each_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/language/dsc range-for | (see dedicated page) |

