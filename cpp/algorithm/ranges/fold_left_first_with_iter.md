---
title: std::ranges::fold_left_first_with_iter
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_left_first_with_iter
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::input_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-left-foldable*/<std::iter_value_t<I>, I> F >
requires std::constructible_from<
std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr /* see description */
fold_left_first_with_iter( I first, S last, F f );
dcl|num=2|since=c++23|1=
template< ranges::input_range R,
/*indirectly-binary-left-foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F >
requires std::constructible_from<
ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr /* see description */
fold_left_first_with_iter( R&& r, F f );
|1=
template< class F, class T, class I >
concept /*indirectly-binary-left-foldable*/ = /* see description */;
dcl|num=4|since=c++23|1=
template< class I, class T >
using fold_left_first_with_iter_result = ranges::in_value_result<I, T>;
```

Left-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(f(f(f(x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_left_first_with_iter` behaves like `std::accumulate`'s overload that accepts a binary predicate, except that the `*first` is used internally as an initial element.
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last).
2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
4. The return type alias. See "" section for details.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `f` - the binary function object

## Return value

Let `U` be `decltype(ranges::fold_left(std::move(first), last, std::iter_value_t<I>(*first), f))`.
1. An object of type `ranges::fold_left_first_with_iter_result<I, std::optional<U>>`.
* The member `ranges::in_value_result::in` holds an iterator to the end of the range.
* The member `ranges::in_value_result::value` holds the result of the left-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of given range over `f`.
If the range is empty, the return value is }.
2. Same as  except that the return type is `ranges::fold_left_first_with_iter_result<ranges::borrowed_iterator_t<R>, std::optional<U>>`.

## Possible implementations

eq fun
|1=
class fold_left_first_with_iter_fn
{
template<class O, class I, class S, class F>
constexpr auto impl(I&& first, S&& last, F f) const
{
using U = decltype(
ranges::fold_left(std::move(first), last, std::iter_value_t<I>(*first), f)
);
using Ret = ranges::fold_left_first_with_iter_result<O, std::optional<U>>;
if (first == last)
return Ret{std::move(first), std::optional<U>()};
std::optional<U> init(std::in_place, *first);
for (++first; first != last; ++first)
*init = std::invoke(f, std::move(*init), *first);
return Ret{std::move(first), std::move(init)};
}
public:
template<std::input_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-left-foldable*/<std::iter_value_t<I>, I> F>
requires std::constructible_from<std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr auto operator()(I first, S last, F f) const
{
return impl<I>(std::move(first), std::move(last), std::ref(f));
}
template<ranges::input_range R, /*indirectly-binary-left-foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F>
requires
std::constructible_from<ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr auto operator()(R&& r, F f) const
{
return impl<ranges::borrowed_iterator_t<R>>(
ranges::begin(r), ranges::end(r), std::ref(f)
);
}
};
inline constexpr fold_left_first_with_iter_fn fold_left_first_with_iter;

## Complexity

Exactly `ranges::distance(first, last) - 1` (assuming the range is not empty) applications of the function object `f`.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <ranges>
#include <utility>
#include <vector>

int main()
{
    std::vector v{1, 2, 3, 4, 5, 6, 7, 8};

    auto sum = std::ranges::fold_left_first_with_iter
    (
        v.begin(), v.end(), std::plus<int>()
    );
    std::cout << "sum: " << sum.value.value() << '\n';
    assert(sum.in == v.end());

    auto mul = std::ranges::fold_left_first_with_iter(v, std::multiplies<int>());
    std::cout << "mul: " << mul.value.value() << '\n';
    assert(mul.in == v.end());

    // get the product of the std::pair::second of all pairs in the vector:
    std::vector<std::pair<char, float>> data {{'A', 2.f}, {'B', 3.f}, {'C', 7.f
```

auto sec = std::ranges::fold_left_first_with_iter
(
data | std::ranges::views::values, std::multiplies<>()
);
std::cout << "sec: " << sec.value.value() << '\n';
// use a program defined function object (lambda-expression):
auto lambda = [](int x, int y) { return x + y + 2; };
auto val = std::ranges::fold_left_first_with_iter(v, lambda);
std::cout << "val: " << val.value.value() << '\n';
assert(val.in == v.end());
}
|output=
sum: 36
mul: 40320
sec: 42
val: 50

## References


## See also


| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

