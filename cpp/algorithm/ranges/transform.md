---
title: std::ranges::binary_transform_result
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/transform
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O,
std::copy_constructible F, class Proj = std::identity >
requires std::indirectly_writable<O,
std::indirect_result_t<F&, std::projected<I, Proj>>>
constexpr unary_transform_result<I, O>
transform( I first1, S last1, O result, F op, Proj proj = {} );
dcl|since=c++20|num=2|1=
template< ranges::input_range R, std::weakly_incrementable O,
std::copy_constructible F, class Proj = std::identity >
requires std::indirectly_writable<O,
std::indirect_result_t<F&, std::projected<ranges::iterator_t<R>, Proj>>>
constexpr unary_transform_result<ranges::borrowed_iterator_t<R>, O>
transform( R&& r, O result, F op, Proj proj = {} );
dcl|since=c++20|num=3|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
std::weakly_incrementable O,
std::copy_constructible F,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_writable<O,
std::indirect_result_t<F&,
std::projected<I1, Proj1>,
std::projected<I2, Proj2>>>
constexpr binary_transform_result<I1, I2, O>
transform( I1 first1, S1 last1, I2 first2, S2 last2, O result,
F binary_op, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|since=c++20|num=4|1=
template< ranges::input_range R1,
ranges::input_range R2,
std::weakly_incrementable O,
std::copy_constructible F,
class Proj1 = std::identity, class Proj2 = std::identity >
requires std::indirectly_writable<O,
std::indirect_result_t<F&,
std::projected<ranges::iterator_t<R1>, Proj1>,
std::projected<ranges::iterator_t<R2>, Proj2>>>
constexpr binary_transform_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>, O>
transform( R1&& r1, R2&& r2, O result, F binary_op,
Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|since=c++20|num=5|1=
template< class I, class O >
using unary_transform_result = ranges::in_out_result<I, O>;
dcl|since=c++20|num=6|1=
template< class I1, class I2, class O >
using binary_transform_result = ranges::in_in_out_result<I1, I2, O>;
```

Applies the given function to a range and stores the result in another range, beginning at `result`.
1. The unary operation `op` is applied to the range defined by [first1, last1) (after projecting with the projection `proj`).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
3. The binary operation `binary_op` is applied to pairs of elements from two ranges: one defined by [first1, last1) and the other defined by [first2, last2) (after respectively projecting with the projections `proj1` and `proj2`).
4. Same as , but uses `r1` as the first source range, as if using `ranges::begin(r1)` as `first1` and `ranges::end(r1)` as `last1`, and similarly for `r2`.

## Parameters


### Parameters

- `[first1, last1)` - 
- `r, r1` - the first range of elements to transform
- `[first2, last2)` - 
- `r2` - the second range of elements to transform
- `result` - the beginning of the destination range, may be equal to `first1` or `first2`
- `op, binary_op` - operation to apply to the projected element(s)
- `proj1` - projection to apply to the elements in the first range
- `proj2` - projection to apply to the elements in the second range

## Return value

@1,2@ A `unary_transform_result` contains an input iterator equal to `last` and an output iterator to the element past the last element transformed.
@3,4@ A `binary_transform_result` contains input iterators to last transformed elements from ranges [first1, last1) and [first2, last2) as `in1` and `in2` respectively, and the output iterator to the element past the last element transformed as `out`.

## Complexity

@1,2@ Exactly `ranges::distance(first1, last1)` applications of `op` and `proj`.
@3,4@ Exactly `ranges::min(ranges::distance(first1, last1), ranges::distance(first2, last2))` applications of `binary_op` and projections.

## Possible implementation

eq fun|1=
struct transform_fn
{
// First version
template<std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O,
std::copy_constructible F, class Proj = std::identity>
requires std::indirectly_writable<O, std::indirect_result_t<F&,
std::projected<I, Proj>>>
constexpr ranges::unary_transform_result<I, O>
operator()(I first1, S last1, O result, F op, Proj proj = {}) const
{
for (; first1 != last1; ++first1, (void)++result)
*result = std::invoke(op, std::invoke(proj, *first1));
return {std::move(first1), std::move(result)};
}
// Second version
template<ranges::input_range R, std::weakly_incrementable O,
std::copy_constructible F, class Proj = std::identity>
requires std::indirectly_writable<O,
std::indirect_result_t<F&, std::projected<ranges::iterator_t<R>, Proj>>>
constexpr ranges::unary_transform_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result, F op, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result),
std::move(op), std::move(proj));
}
// Third version
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::input_iterator I2, std::sentinel_for<I2> S2,
std::weakly_incrementable O,
std::copy_constructible F,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_writable<O,
std::indirect_result_t<F&,
std::projected<I1, Proj1>,
std::projected<I2, Proj2>>>
constexpr ranges::binary_transform_result<I1, I2, O>
operator()(I1 first1, S1 last1, I2 first2, S2 last2, O result,
F binary_op, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
for (; first1 != last1 && first2 != last2;
++first1, (void)++first2, (void)++result)
*result = std::invoke(binary_op,
std::invoke(proj1, *first1),
std::invoke(proj2, *first2));
return {std::move(first1), std::move(first2), std::move(result)};
}
// Fourth version
template<ranges::input_range R1, ranges::input_range R2,
std::weakly_incrementable O, std::copy_constructible F,
class Proj1 = std::identity, class Proj2 = std::identity>
requires std::indirectly_writable<O,
std::indirect_result_t<F&,
std::projected<ranges::iterator_t<R1>, Proj1>,
std::projected<ranges::iterator_t<R2>, Proj2>>>
constexpr ranges::binary_transform_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>, O>
operator()(R1&& r1, R2&& r2, O result,
F binary_op, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r1), ranges::end(r1),
ranges::begin(r2), ranges::end(r2),
std::move(result), std::move(binary_op),
std::move(proj1), std::move(proj2));
}
};
inline constexpr transform_fn transform;

## Notes

`ranges::transform` does not guarantee in-order application of `op` or `binary_op`. To apply a function to a sequence in-order or to apply a function that modifies the elements of a sequence, use `ranges::for_each`.

## Example

|code=
#include <algorithm>
#include <cctype>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
int main()
{
std::string s{"hello"};
auto op = [](unsigned char c) -> unsigned char { return std::toupper(c); };
namespace ranges = std::ranges;
// uppercase the string in-place
ranges::transform(s.begin(), s.end(), s.begin(), op );
std::vector<std::size_t> ordinals;
// convert each char to size_t
ranges::transform(s, std::back_inserter(ordinals),
[](unsigned char c) -> std::size_t { return c; });
std::cout << s << ':';
for (auto ord : ordinals)
std::cout << ' ' << ord;
// double each ordinal
ranges::transform(ordinals, ordinals, ordinals.begin(), std::plus{});
std::cout << '\n';
for (auto ord : ordinals)
std::cout << ord << ' ';
std::cout << '\n';
struct Foo { char bar; };
const std::vector<Foo> f = 'h'},{'e'},{'l'},{'l'},{'o';
std::string result;
// project, then uppercase
ranges::transform(f, std::back_inserter(result), op, &Foo::bar);
std::cout << result << '\n';
}
|output=
HELLO: 72 69 76 76 79
144 138 152 152 158
HELLO

## See also


| cpp/algorithm/ranges/dsc for_each | (see dedicated page) |
| cpp/ranges/dsc transform_view | (see dedicated page) |
| cpp/algorithm/dsc transform | (see dedicated page) |

