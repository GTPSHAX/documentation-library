---
title: std::ranges::all_of
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/all_any_none_of
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr bool all_of( I first, S last, Pred pred, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr bool all_of( R&& r, Pred pred, Proj proj = {} );
dcla|num=3|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr bool any_of( I first, S last, Pred pred, Proj proj = {} );
dcl|num=4|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr bool any_of( R&& r, Pred pred, Proj proj = {} );
dcla|num=5|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr bool none_of( I first, S last, Pred pred, Proj proj = {} );
dcl|num=6|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr bool none_of( R&& r, Pred pred, Proj proj = {} );
dcl|num=7|since=c++26|1=
template< /*execution-policy*/ Ep, std::random_access_iterator I,
std::sized_sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
bool all_of( Ep&& policy, I first, S last, Pred pred, Proj proj = {} );
dcl|num=8|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
bool all_of( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
dcl|num=9|since=c++26|1=
template< /*execution-policy*/ Ep, std::random_access_iterator I,
std::sized_sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
bool any_of( Ep&& policy, I first, S last, Pred pred, Proj proj = {} );
dcl|num=10|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
bool any_of( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
dcl|num=11|since=c++26|1=
template< /*execution-policy*/ Ep, std::random_access_iterator I,
std::sized_sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
bool none_of( Ep&& policy, I first, S last, Pred pred, Proj proj = {} );
dcl|num=12|since=c++26|1=
template< /*execution-policy*/ Ep,
/*sized-random-access-range*/ R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
bool none_of( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
@1,2@ Checks if unary predicate `pred` returns `false` for at least one element (projected by `proj`) in the range [first, last) or `r`.
@3,4@ Checks if unary predicate `pred` returns `true` for at least one element (projected by `proj`) in the range [first, last) or `r`.
@5,6@ Checks if unary predicate `pred` returns `true` for none of the elements (projected by `proj`) in the range [first, last) or `r`.
@7-12@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[3=to examine, sentinel=yes}})` - 
- `r` - the range of the elements to examine
- `pred` - the predicate to be applied to the (projected) elements
- `proj` - the projection to be applied to the elements
- `policy` - execution policy

## Return value


## Complexity

At most `range::distance(first, last)` or `range::distance(r)` applications of `pred` and the `proj`.

## Exceptions

@7-12@

## Possible implementation

eq impl
|title1=all_of (1,2)|ver1=1|1=
struct all_of_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr bool operator()(I first, S last, Pred pred, Proj proj = {}) const
{
return ranges::find_if_not(first, last, std::ref(pred), std::ref(proj)) == last;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r), ranges::end(r),
std::ref(pred), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr all_of_fn all_of;
|title2=any_of (3,4)|ver2=3|2=
struct any_of_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr bool operator()(I first, S last, Pred pred, Proj proj = {}) const
{
return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) != last;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r), ranges::end(r),
std::ref(pred), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr any_of_fn any_of;
|title3=none_of (5,6)|ver3=5|3=
struct none_of_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr bool operator()(I first, S last, Pred pred, Proj proj = {}) const
{
return ranges::find_if(first, last, std::ref(pred), std::ref(proj)) == last;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r), ranges::end(r),
std::ref(pred), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr bool operator()(R&& r, Pred pred, Proj proj = {}) const
{
return operator()(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr none_of_fn none_of;

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

namespace ranges = std::ranges;

constexpr bool some_of(auto&& r, auto&& pred) // some but not all
{
    return not (ranges::all_of(r, pred) or ranges::none_of(r, pred));
}

constexpr auto w = {1, 2, 3};
static_assert(!some_of(w, [](int x) { return x < 1; }));
static_assert( some_of(w, [](int x) { return x < 2; }));
static_assert(!some_of(w, [](int x) { return x < 4; }));

int main()
{
    std::vector<int> v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout << "Among the numbers: ";
    ranges::copy(v, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    if (ranges::all_of(v.cbegin(), v.cend(), [](int i) { return i % 2 == 0; }))
        std::cout << "All numbers are even\n";

    if (ranges::none_of(v, std::bind(std::modulus<int>(), std::placeholders::_1, 2)))
        std::cout << "None of them are odd\n";

    auto DivisibleBy = [](int d)
    {
        return [d](int m) { return m % d == 0; };
    };

    if (ranges::any_of(v, DivisibleBy(7)))
        std::cout << "At least one number is divisible by 7\n";
}
```


**Output:**
```
Among the numbers: 2 4 6 8 10 12 14 16 18 20
All numbers are even
None of them are odd
At least one number is divisible by 7
```


## See also


| cpp/algorithm/dsc all_any_none_of | (see dedicated page) |

