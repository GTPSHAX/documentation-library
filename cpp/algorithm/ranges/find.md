---
title: std::ranges::find
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/find
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S,
class T, class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr I find( I first, S last, const T& value, Proj proj = {} );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr I find( I first, S last, const T& value, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< ranges::input_range R, class T, class Proj = std::identity >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_iterator_t<R>
find( R&& r, const T& value, Proj proj = {} );
|dcl2=
template< ranges::input_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_iterator_t<R>
find( R&& r, const T& value, Proj proj = {} );
dcla|num=3|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr I find_if( I first, S last, Pred pred, Proj proj = {} );
dcl|num=4|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr ranges::borrowed_iterator_t<R>
find_if( R&& r, Pred pred, Proj proj = {} );
dcla|num=5|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
constexpr I find_if_not( I first, S last, Pred pred, Proj proj = {} );
dcl|num=6|since=c++20|1=
template< ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
constexpr ranges::borrowed_iterator_t<R>
find_if_not( R&& r, Pred pred, Proj proj = {} );
dcl|num=7|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
I find( Ep&& policy, I first, S last, const T& value, Proj proj = {} );
dcl|num=8|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
ranges::borrowed_iterator_t<R>
find( Ep&& policy, R&& r, const T& value, Proj proj = {} );
dcl|num=9|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
I find_if( Ep&& policy, I first, S last, Pred pred, Proj proj = {} );
dcl|num=10|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
ranges::borrowed_iterator_t<R>
find_if( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
dcl|num=11|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, std::sized_sentinel_for<I> S,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
I find_if_not( Ep&& policy, I first, S last, Pred pred, Proj proj = {} );
dcl|num=12|since=c++26|1=
template< /*execution-policy*/ Ep, /*sized-random-access-range*/ R,
class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred >
ranges::borrowed_iterator_t<R>
find_if_not( Ep&& policy, R&& r, Pred pred, Proj proj = {} );
```

For the definition of `/*execution-policy*/`, see this page; for the definition of `/*sized-random-access-range*/`, see this page.
Search for the first element (projected by `proj`) in the source range [first, last) or `r` that satisfies specific criteria:
@1,2@ `find` searches for the first element equal to the target value `value`.
@3,4@ `find_if` searches for the first element for which predicate `pred` returns `true`.
@5,6@ `find_if_not` searches for the first element for which predicate `pred` returns `false`.
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

Iterator to the first element satisfying the condition, or `last` if no such element is found.

## Complexity

Given  as `ranges::distance(first, last)` or `ranges::distance(r)`:
@1,2@ At most  comparisons and applications of `proj`.
@3-6@ At most  applications of `pred` and `proj`.
@7,8@ } comparisons and applications of `proj`.
@9-12@ } applications of `pred` and `proj`.

## Exceptions

@7-12@

## Notes


## Possible implementation

eq impl|title1=find|ver1=1|1=
struct find_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>>
requires std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr I operator()(I first, S last, const T& value, Proj proj = {}) const
{
for (; first != last; ++first)
if (std::invoke(proj, *first) == value)
return first;
return first;
}
template<ranges::input_range R, class T, class Proj = std::identity>
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, const T& value, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), value, std::ref(proj));
}
template<ranges::forward_range R, class T, class Proj = std::identity>
requires std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, const T& value, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
value, std::ref(proj));
}
};
inline constexpr find_fn find;
|title2=find_if|ver2=3|2=
struct find_if_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr I operator()(I first, S last, Pred pred, Proj proj = {}) const
{
for (; first != last; ++first)
if (std::invoke(pred, std::invoke(proj, *first)))
return first;
return first;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr find_if_fn find_if;
|title3=find_if_not|ver3=5|3=
struct find_if_not_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
constexpr I operator()(I first, S last, Pred pred, Proj proj = {}) const
{
for (; first != last; ++first)
if (!std::invoke(pred, std::invoke(proj, *first)))
return first;
return first;
}
template<ranges::input_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(pred), std::ref(proj));
}
template<ranges::forward_range R, class Proj = std::identity,
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r),
ranges::next(ranges::begin(r), ranges::end(r)),
std::ref(pred), std::ref(proj));
}
};
inline constexpr find_if_not_fn find_if_not;

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <format>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

void projector_example()
{
    struct folk_info
    {
        unsigned uid;
        std::string name, position;
    };

    std::vector<folk_info> folks
    {
        {0, "Ana", "dev"},
        {1, "Bob", "devops"},
        {2, "Eve", "ops"}
    };

    const auto who{"Eve"};
    if (auto it = std::ranges::find(folks, who, &folk_info::name); it != folks.end())
        std::cout << std::format("Profile:\n"
                                 "    UID: {}\n"
                                 "    Name: {}\n"
                                 "    Position: {}\n\n",
                                 it->uid, it->name, it->position);
}

int main()
{
    namespace ranges = std::ranges;

    projector_example();

    const int n1 = 3;
    const int n2 = 5;
    const auto v = {4, 1, 3, 2};

    if (ranges::find(v, n1) != v.end())
        std::cout << "v contains: " << n1 << '\n';
    else
        std::cout << "v does not contain: " << n1 << '\n';

    if (ranges::find(v.begin(), v.end(), n2) != v.end())
        std::cout << "v contains: " << n2 << '\n';
    else
        std::cout << "v does not contain: " << n2 << '\n';

    auto is_even = [](int x) { return x % 2 == 0; };

    if (auto result = ranges::find_if(v.begin(), v.end(), is_even); result != v.end())
        std::cout << "First even element in v: " << *result << '\n';
    else
        std::cout << "No even elements in v\n";

    if (auto result = ranges::find_if_not(v, is_even); result != v.end())
        std::cout << "First odd element in v: " << *result << '\n';
    else
        std::cout << "No odd elements in v\n";

    auto divides_13 = [](int x) { return x % 13 == 0; };

    if (auto result = ranges::find_if(v, divides_13); result != v.end())
        std::cout << "First element divisible by 13 in v: " << *result << '\n';
    else
        std::cout << "No elements in v are divisible by 13\n";

    if (auto result = ranges::find_if_not(v.begin(), v.end(), divides_13);
        result != v.end())
        std::cout << "First element indivisible by 13 in v: " << *result << '\n';
    else
        std::cout << "All elements in v are divisible by 13\n";

    std::vector<std::complex<double>> nums{<!---->{4, 2}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        // T gets deduced in (2) making list-initialization possible
        const auto it = ranges::find(nums, {4, 2});
    #else
        const auto it = ranges::find(nums, std::complex<double>{4, 2});
    #endif
    assert(it == nums.begin());
}
```


**Output:**
```
Profile:
    UID: 2
    Name: Eve
    Position: ops

v contains: 3
v does not contain: 5
First even element in v: 4
First odd element in v: 1
No elements in v are divisible by 13
First element indivisible by 13 in v: 4
```


## See also


| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |

