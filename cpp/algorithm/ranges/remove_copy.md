---
title: std::ranges::remove_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/remove_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O, class T, class Proj = std::identity >
requires std::indirectly_copyable<I, O> &&
std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr remove_copy_result<I, O>
remove_copy( I first, S last, O result, const T& value, Proj proj = {} );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O, class Proj = std::identity,
class T = std::projected_value_t<I, Proj> >
requires std::indirectly_copyable<I, O> &&
std::indirect_binary_predicate
<ranges::equal_to, std::projected<I, Proj>, const T*>
constexpr remove_copy_result<I, O>
remove_copy( I first, S last, O result, const T& value, Proj proj = {} );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< ranges::input_range R,
std::weakly_incrementable O, class T, class Proj = std::identity >
requires std::indirectly_copyable<ranges::iterator_t<R>, O> &&
std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr remove_copy_result<ranges::borrowed_iterator_t<R>, O>
remove_copy( R&& r, O result, const T& value, Proj proj = {} );
|dcl2=
template< ranges::input_range R,
std::weakly_incrementable O, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj> >
requires std::indirectly_copyable<ranges::iterator_t<R>, O> &&
std::indirect_binary_predicate
<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr remove_copy_result<ranges::borrowed_iterator_t<R>, O>
remove_copy( R&& r, O result, const T& value, Proj proj = {} );
dcla|num=3|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O, class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred >
requires std::indirectly_copyable<I, O>
constexpr remove_copy_if_result<I, O>
remove_copy_if( I first, S last, O result, Pred pred, Proj proj = {} );
dcl|num=4|since=c++20|1=
template< ranges::input_range R,
std::weakly_incrementable O, class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred >
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr remove_copy_if_result<ranges::borrowed_iterator_t<R>, O>
remove_copy_if( R&& r, O result, Pred pred, Proj proj = {} );
dcl|num=5|since=c++20|1=
template< class I, class O >
using remove_copy_result = ranges::in_out_result<I, O>;
dcl|num=6|since=c++20|1=
template< class I, class O >
using remove_copy_if_result = ranges::in_out_result<I, O>;
```

Copies elements from the source range [first, last), to the destination range beginning at `result`, omitting the elements which (after being projected by `proj`) satisfy specific criteria. The behavior is undefined if the source and destination ranges overlap.
1. Ignores all elements that are equal to `value`.
3. Ignores all elements for which predicate `pred` returns `true`.
@2,4@ Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to process, range=source)` - 
- `r` - the source range of elements
- `result` - the beginning of the destination range
- `value` - the value of the elements '''not''' to copy
- `comp` - the binary predicate to compare the projected elements
- `proj` - the projection to apply to the elements

## Return value

}, where `N` is the number of elements copied.

## Complexity

Exactly `ranges::distance(first, last)` applications of the corresponding predicate `comp` and any projection `proj`.

## Notes

The algorithm is stable, i.e. preserves the relative order of the copied elements.

## Possible implementation

eq impl|title1=remove_copy (1,2)|ver1=1|1=
struct remove_copy_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O, class Proj = std::identity,
class T = std::projected_value_t<I, Proj>>
requires std::indirectly_copyable<I, O> &&
std::indirect_binary_predicate<ranges::equal_to,
std::projected<I, Proj>, const T*>
constexpr ranges::remove_copy_result<I, O>
operator()(I first, S last, O result, const T& value, Proj proj = {}) const
{
for (; !(first == last); ++first)
if (value != std::invoke(proj, *first))
{
*result = *first;
++result;
}
return {std::move(first), std::move(result)};
}
template<ranges::input_range R,
std::weakly_incrementable O, class Proj = std::identity,
class T = std::projected_value_t<ranges::iterator_t<R>, Proj>>
requires std::indirectly_copyable<ranges::iterator_t<R>, O> &&
std::indirect_binary_predicate<ranges::equal_to,
std::projected<ranges::iterator_t<R>, Proj>, const T*>
constexpr ranges::remove_copy_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result, const T& value, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result), value,
std::move(proj));
}
};
inline constexpr remove_copy_fn remove_copy {};
|title2=remove_copy_if (3,4)|ver2=3|2=
struct remove_copy_if_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_unary_predicate<std::projected<I, Proj>> Pred>
requires std::indirectly_copyable<I, O>
constexpr ranges::remove_copy_if_result<I, O>
operator()(I first, S last, O result, Pred pred, Proj proj = {}) const
{
for (; first != last; ++first)
if (false == std::invoke(pred, std::invoke(proj, *first)))
{
*result = *first;
++result;
}
return {std::move(first), std::move(result)};
}
template<ranges::input_range R, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_unary_predicate<
std::projected<ranges::iterator_t<R>, Proj>> Pred>
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr ranges::remove_copy_if_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result, Pred pred, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result),
std::move(pred), std::move(proj));
}
};
inline constexpr remove_copy_if_fn remove_copy_if {};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <complex>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <string_view>
#include <vector>

void println(const auto rem, const auto& v)
{
    std::cout << rem << ' ';
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    // Filter out the hash symbol from the given string.
    const std::string_view str{"#Small #Buffer #Optimization"};
    std::cout << "before: " << std::quoted(str) << '\n';

    std::cout << "after:  \"";
    std::ranges::remove_copy(str.begin(), str.end(),
                             std::ostream_iterator<char>(std::cout), '#');
    std::cout << "\"\n";

    // Copy only the complex numbers with positive imaginary part.
    using Ci = std::complex<int>;
    constexpr std::array<Ci, 5> source
    {
        Ci{1, 0}, Ci{0, 1}, Ci{2, -1}, Ci{3, 2}, Ci{4, -3}
    };
    std::vector<std::complex<int>> target;

    std::ranges::remove_copy_if
    (
        source,
        std::back_inserter(target),
        [](int imag) { return imag <= 0; },
        [](Ci z) { return z.imag(); }
    );

    println("source:", source);
    println("target:", target);

    std::vector<std::complex<float>> nums{<!---->{2, 2}, {1, 3}, {4, 8}, {1, 3}<!---->};
    std::vector<std::complex<double>> outs;
    #ifdef __cpp_lib_algorithm_default_value_type
        std::remove_copy(nums.cbegin(), nums.cend(), std::back_inserter(outs),
                         {1, 3}); // T gets deduced to std::complex<float>
    #else
        std::remove_copy(nums.cbegin(), nums.cend(), std::back_inserter(outs),
                         std::complex<float>{1, 3});
    #endif
    println("nums:  ", nums);
    println("outs:  ", outs);
}
```


**Output:**
```
before: "#Small #Buffer #Optimization"
after:  "Small Buffer Optimization"
source: (1,0) (0,1) (2,-1) (3,2) (4,-3)
target: (0,1) (3,2)
nums:   (2,2) (1,3) (4,8) (1,3)
outs:   (2,2) (4,8)
```


## See also


| cpp/algorithm/ranges/dsc remove | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/dsc remove_copy | (see dedicated page) |

