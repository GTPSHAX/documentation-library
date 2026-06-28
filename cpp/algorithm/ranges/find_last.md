---
title: std::ranges::find_last
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/find_last
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|since1=c++23|until1=c++26|dcl1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class T,
class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr ranges::subrange<I>
find_last( I first, S last, const T& value, Proj proj = {} );
|dcl2=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr ranges::subrange<I>
find_last( I first, S last, const T& value, Proj proj = {} );
dcl rev multi|num=2|since1=c++23|until1=c++26|dcl1=
template< ranges::forward_range R,
class T,
class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_subrange_t<R>
find_last( R&& r, const T& value, Proj proj = {} );
|dcl2=
template< ranges::forward_range R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_subrange_t<R>
find_last( R&& r, const T& value, Proj proj = {} );
dcla|num=3|since=c++23|1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr ranges::subrange<I>
find_last_if( I first, S last, Pred pred, Proj proj = {} );
dcl|num=4|since=c++23|1=
template< ranges::forward_range R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr ranges::borrowed_subrange_t<R>
find_last_if( R&& r, Pred pred, Proj proj = {} );
dcla|num=5|since=c++23|1=
template< std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr ranges::subrange<I>
find_last_if_not( I first, S last, Pred pred, Proj proj = {} );
dcl|num=6|since=c++23|1=
template< ranges::forward_range R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr ranges::borrowed_subrange_t<R>
find_last_if_not( R&& r, Pred pred, Proj proj = {} );
dcl|num=7|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
ranges::subrange<I> find_last( Ep&& policy, I first, S last,
const T& value, Proj proj = {} );
dcl|num=8|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
ranges::borrowed_subrange_t<R>
find_last( Ep&& policy, R&& r, const T& value, Proj proj = {} );
dcl|num=9|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
ranges::subrange<I> find_last_if( Ep&& policy, I first, S last,
Pred pred, Proj proj = {} );
dcl|num=10|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
ranges::borrowed_subrange_t<R>
find_last_if( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
dcl|num=11|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
ranges::subrange<I> find_last_if_not( Ep&& policy, I first, S last,
Pred pred, Proj proj = {} );
dcl|num=12|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
ranges::borrowed_subrange_t<R>
find_last_if_not( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
Returns the last element (projected by `proj`) in the source range [first, last) or `r` that satisfies specific criteria:
@1,2@ `find_last` searches for the last element equal to `value`.
@3,4@ `find_last_if` searches for the last element for which predicate `pred` returns `true`.
@5,6@ `find_last_if_not` searches for the last element for which predicate `pred` returns `false`.
@7-12@ Same as , but executed according to `policy`.

## Parameters


### Parameters

- `[first, last)` - 
- `r` - the source range
- `value` - the target value
- `pred` - the predicate to be applied to the (projected) elements
- `proj` - the projection to be applied to the elements
- `policy` - execution policy

## Return value

A subrange from the last element satisfying the condition to the end of the source range, or an empty range if no such element is found.

## Complexity

Given  as `ranges::distance(first, last)` or `ranges::distance(r)`:
@1,2@ At most  comparisons and applications of `proj`.
@3-6@ At most  applications of `pred` and `proj`.
@7,8@ } comparisons and applications of `proj`.
@9-12@ } applications of `pred` and `proj`.

## Exceptions

@7-12@

## Notes

`ranges::find_last`, `ranges::find_last_if`, `ranges::find_last_if_not` have better efficiency on common implementations if `I` models  or (better) .

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_algorithm_default_value_type` | 202403L | C++26 | List-initialization for algorithms |


## Possible implementation

These implementations only show the slower algorithm used when `I` models .
eq impl
|title1=find_last|ver1=1|1=
struct find_last_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>>
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr ranges::subrange<I>
operator()(I first, S last, const T &value, Proj proj = {}) const
{
// Note: if I is mere forward_iterator, we may only go from begin to end.
std::optional<I> found;
for (; first != last; ++first)
if (std::invoke(proj, *first) == value)
found = first;
if (!found)
return {first, first};
return {*found, ranges::next(*found, last)};
}
template<ranges::forward_range R,
class Proj = std::identity,
class T = std::projected_value_t<iterator_t<R>, Proj>>
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, const T &value, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
value, std::ref(proj));
}
};
inline constexpr find_last_fn find_last;
|title2=find_last_if|ver2=3|2=
struct find_last_if_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr ranges::subrange<I>
operator()(I first, S last, Pred pred, Proj proj = {}) const
{
// Note: if I is mere forward_iterator, we may only go from begin to end.
std::optional<I> found;
for (; first != last; ++first)
if (std::invoke(pred, std::invoke(proj, *first)))
found = first;
if (!found)
return {first, first};
return {*found, ranges::next(*found, last)};
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr find_last_if_fn find_last_if;
|title3=find_last_if_not|ver3=5|3=
struct find_last_if_not_fn
{
template<std::forward_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr ranges::subrange<I>
operator()(I first, S last, Pred pred, Proj proj = {}) const
{
// Note: if I is mere forward_iterator, we may only go from begin to end.
std::optional<I> found;
for (; first != last; ++first)
if (!std::invoke(pred, std::invoke(proj, *first)))
found = first;
if (!found)
return {first, first};
return {*found, ranges::next(*found, last)};
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_subrange_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr find_last_if_not_fn find_last_if_not;

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <forward_list>
#include <iomanip>
#include <iostream>
#include <string_view>

int main()
{
    namespace ranges = std::ranges;

    constexpr static auto v = {1, 2, 3, 1, 2, 3, 1, 2};

    {
        constexpr auto i1 = ranges::find_last(v.begin(), v.end(), 3);
        constexpr auto i2 = ranges::find_last(v, 3);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        constexpr auto i1 = ranges::find_last(v.begin(), v.end(), -3);
        constexpr auto i2 = ranges::find_last(v, -3);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    auto abs = [](int x) { return x < 0 ? -x : x; };

    {
        auto pred = [](int x) { return x == 3; };
        constexpr auto i1 = ranges::find_last_if(v.begin(), v.end(), pred, abs);
        constexpr auto i2 = ranges::find_last_if(v, pred, abs);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        auto pred = [](int x) { return x == -3; };
        constexpr auto i1 = ranges::find_last_if(v.begin(), v.end(), pred, abs);
        constexpr auto i2 = ranges::find_last_if(v, pred, abs);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    {
        auto pred = [](int x) { return x == 1 or x == 2; };
        constexpr auto i1 = ranges::find_last_if_not(v.begin(), v.end(), pred, abs);
        constexpr auto i2 = ranges::find_last_if_not(v, pred, abs);
        static_assert(ranges::distance(v.begin(), i1.begin()) == 5);
        static_assert(ranges::distance(v.begin(), i2.begin()) == 5);
    }
    {
        auto pred = [](int x) { return x == 1 or x == 2 or x == 3; };
        constexpr auto i1 = ranges::find_last_if_not(v.begin(), v.end(), pred, abs);
        constexpr auto i2 = ranges::find_last_if_not(v, pred, abs);
        static_assert(i1.begin() == v.end());
        static_assert(i2.begin() == v.end());
    }

    using P = std::pair<std::string_view, int>;
    std::forward_list<P> list
    {
        {"one", 1}, {"two", 2}, {"three", 3},
        {"one", 4}, {"two", 5}, {"three", 6},
    };
    auto cmp_one = [](const std::string_view &s) { return s == "one"; };

    // find latest element that satisfy the comparator, and projecting pair::first
    const auto subrange = ranges::find_last_if(list, cmp_one, &P::first);

    std::cout << "The found element and the tail after it are:\n";
    for (P const& e : subrange)
        std::cout << '{' << std::quoted(e.first) << ", " << e.second << "} ";
    std::cout << '\n';

#if __cpp_lib_algorithm_default_value_type
    const auto i3 = ranges::find_last(list, {"three", 3}); // (2) C++26
#else
    const auto i3 = ranges::find_last(list, P{"three", 3}); // (2) C++23
#endif
    assert(i3.begin()->first == "three" && i3.begin()->second == 3);
}
```


**Output:**
```
The found element and the tail after it are:
{"one", 4} {"two", 5} {"three", 6}
```


## See also


| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc includes | (see dedicated page) |
| cpp/algorithm/ranges/dsc binary_search | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |

