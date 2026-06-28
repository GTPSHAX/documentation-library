---
title: std::ranges::replace
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/replace
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version 1|since1=c++20|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S,
class T1, class T2, class Proj = std::identity >
requires std::indirectly_writable<I, const T2&> &&
std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T1*>
constexpr I replace( I first, S last, const T1& old_value,
const T2& new_value, Proj proj = {} );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T1 = std::projected_value_t<I, Proj>, class T2 = T1 >
requires std::indirectly_writable<I, const T2&> &&
std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T1*>
constexpr I replace( I first, S last, const T1& old_value,
const T2& new_value, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26|
|dcl1=
template< ranges::input_range R,
class T1, class T2, class Proj = std::identity >
requires std::indirectly_writable<ranges::iterator_t<R>, const T2&> &&
std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T1*>
constexpr ranges::borrowed_iterator_t<R>
replace( R&& r, const T1& old_value,
const T2& new_value, Proj proj = {} );
|dcl2=
template< ranges::input_range R,
class Proj = std::identity,
class T1 = std::projected_value_t<ranges::iterator_t<R>, Proj>,
class T2 = T1 >
requires std::indirectly_writable<ranges::iterator_t<R>, const T2&> &&
std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T1*>
constexpr ranges::borrowed_iterator_t<R>
replace( R&& r, const T1& old_value,
const T2& new_value, Proj proj = {} );
dcl rev multi|num=3|anchor=Version_3|since1=c++20|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S,
class T, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
requires std::indirectly_writable<I, const T&>
constexpr I replace_if( I first, S last, Pred pred,
const T& new_value, Proj proj = {} );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity,
class T = std::projected_value_t<I, Proj>,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
requires std::indirectly_writable<I, const T&>
constexpr I replace_if( I first, S last, Pred pred,
const T& new_value, Proj proj = {} );
dcl rev multi|num=4|since1=c++20|until1=c++26
|dcl1=
template< ranges::input_range R, class T, class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
requires std::indirectly_writable<ranges::iterator_t<R>, const T&>
constexpr ranges::borrowed_iterator_t<R>
replace_if( R&& r, Pred pred, const T& new_value, Proj proj = {} );
|dcl2=
template< ranges::input_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
requires std::indirectly_writable<ranges::iterator_t<R>, const T&>
constexpr ranges::borrowed_iterator_t<R>
replace_if( R&& r, Pred pred, const T& new_value, Proj proj = {} );
```

Replaces all elements satisfying specific criteria with `new_value` in the range [first, last).
1. Replaces all elements that are equal to `old_value`, using `1=std::invoke(proj, *i) == old_value` to compare.
3. Replaces all elements for which the predicate `pred` evaluates to `true`, where evaluating expression is `std::invoke(pred, std::invoke(proj, *i))`.
@2,4@ Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to process, sentinel=yes}})` - 
- `r` - the range of elements to process
- `old_value` - the value of elements to replace
- `new_value` - the value to use as a replacement
- `pred` - predicate to apply to the projected elements
- `proj` - projection to apply to the elements

## Return value

An iterator equal to `last`.

## Complexity

Exactly `ranges::distance(first, last)` applications of the corresponding predicate `comp` and any projection `proj`.

## Notes

Because the algorithm takes `old_value` and `new_value` by reference, it may have unexpected behavior if either is a reference to an element of the range [first, last).

## Possible implementation

eq impl|
|title1=replace (1,2)|ver1=1|1=
struct replace_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class Proj = std::identity,
class T1 = std::projected_value_t<I, Proj>, class T2 = T1>
requires std::indirectly_writable<I, const T2&> &&
std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T1*>
constexpr I operator()(I first, S last, const T1& old_value,
const T2& new_value, Proj proj = {}) const
{
for (; first != last; ++first)
if (old_value == std::invoke(proj, *first))
*first = new_value;
return first;
}
template<ranges::input_range R, class Proj = std::identity
class T1 = std::projected_value_t<ranges::iterator_t<R>, Proj>,
class T2 = T1>
requires std::indirectly_writable<ranges::iterator_t<R>, const T2&> &&
std::indirect_binary_predicate<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T1*>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, const T1& old_value,
const T2& new_value, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), old_value,
new_value, std::move(proj));
}
};
inline constexpr replace_fn replace{};
|title2=replace_if (3,4)|ver2=3|2=
struct replace_if_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
class Proj = std::identity, class T = std::projected_value_t<I, Proj>,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
requires std::indirectly_writable<I, const T&>
constexpr I operator()(I first, S last, Pred pred,
const T& new_value, Proj proj = {}) const
{
for (; first != last; ++first)
if (!!std::invoke(pred, std::invoke(proj, *first)))
*first = new_value;
return std::move(first);
}
template<ranges::input_range R, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>
std::indirect_unary_predicate
<std::projected<ranges::iterator_t<R>, Proj>> Pred>
requires std::indirectly_writable<ranges::iterator_t<R>, const T&>
constexpr ranges::borrowed_iterator_t<R>
operator()(R&& r, Pred pred, const T& new_value, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(pred),
new_value, std::move(proj));
}
};
inline constexpr replace_if_fn replace_if{};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <complex>
#include <iostream>

void println(const auto& v)
{
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    namespace ranges = std::ranges;

    std::array p{1, 6, 1, 6, 1, 6};
    println(p);
    ranges::replace(p, 6, 9);
    println(p);

    std::array q{1, 2, 3, 6, 7, 8, 4, 5};
    println(q);
    ranges::replace_if(q, [](int x) { return 5 < x; }, 5);
    println(q);

    std::array<std::complex<double>, 2> nums{<!---->{<!---->{1, 3}, {1, 3}<!---->}<!---->};
    println(nums);
    #ifdef __cpp_lib_algorithm_default_value_type
        ranges::replace(nums, {1, 3}, {4, 2});
    #else
        ranges::replace(nums, std::complex<double>{1, 3}, std::complex<double>{4, 2});
    #endif
    println(nums);
}
```


**Output:**
```
1 6 1 6 1 6
1 9 1 9 1 9
1 2 3 6 7 8 4 5
1 2 3 5 5 5 4 5
(1,3) (1,3)
(4,2) (4,2)
```


## See also


| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/dsc replace | (see dedicated page) |

