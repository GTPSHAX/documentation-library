---
title: std::ranges::fold_right_last
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_right_last
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-right-foldable*/<std::iter_value_t<I>, I> F >
requires std::constructible_from<
std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr auto
fold_right_last( I first, S last, F f );
dcl|num=2|since=c++23|1=
template< ranges::bidirectional_range R,
/*indirectly-binary-right-foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F >
requires std::constructible_from<
ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr auto
fold_right_last( R&& r, F f );
|1=
template< class F, class T, class I >
concept /*indirectly-binary-left-foldable*/ = /* see description */;
|1=
template< class F, class T, class I >
concept /*indirectly-binary-right-foldable*/ = /* see description */;
```

Right-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_right_last` behaves like `ranges::fold_left(views::reverse(r), *--last, /*flipped*/(f))` (assuming the range is not empty).
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last). Given `U` as `decltype(ranges::fold_right(first, last, std::iter_value_t<I>(*first), f))`, equivalent to:

```cpp
if (first == last)
    return std::optional<U>();
I tail = ranges::prev(ranges::next(first, std::move(last)));
return std::optional<U>(std::in_place, ranges::fold_right(std::move(first), tail,
    std::iter_value_t<I>(*tail), std::move(f)));
```

2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `f` - the binary function object

## Return value

An object of type `std::optional<U>` that contains the result of right-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of the given range over `f`.
If the range is empty, `std::optional<U>()` is returned.

## Possible implementations

eq fun
|1=
struct fold_right_last_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-right-foldable*/<std::iter_value_t<I>, I> F>
requires
std::constructible_from<std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr auto operator()(I first, S last, F f) const
{
using U = decltype(
ranges::fold_right(first, last, std::iter_value_t<I>(*first), f));
if (first == last)
return std::optional<U>();
I tail = ranges::prev(ranges::next(first, std::move(last)));
return std::optional<U>(std::in_place,
ranges::fold_right(std::move(first), tail, std::iter_value_t<I>(*tail),
std::move(f)));
}
template<ranges::bidirectional_range R,
/*indirectly_binary_right_foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F>
requires
std::constructible_from<ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr auto operator()(R&& r, F f) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(f));
}
};
inline constexpr fold_right_last_fn fold_right_last;

## Complexity

Exactly `ranges::distance(first, last)` applications of the function object `f`.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <ranges>
#include <utility>
#include <vector>

int main()
{
    auto v = {1, 2, 3, 4, 5, 6, 7, 8};
    std::vector<std::string> vs {"A", "B", "C", "D"};

    auto r1 = std::ranges::fold_right_last(v.begin(), v.end(), std::plus<>()); // (1)
    std::cout << "*r1: " << *r1 << '\n';

    auto r2 = std::ranges::fold_right_last(vs, std::plus<>()); // (2)
    std::cout << "*r2: " << *r2 << '\n';

    // Use a program defined function object (lambda-expression):
    auto r3 = std::ranges::fold_right_last(v, [](int x, int y) { return x + y + 99; });
    std::cout << "*r3: " << *r3 << '\n';

    // Get the product of the std::pair::second of all pairs in the vector:
    std::vector<std::pair<char, float>> data {{'A', 3.f}, {'B', 3.5f}, {'C', 4.f
```

auto r4 = std::ranges::fold_right_last
(
data | std::ranges::views::values, std::multiplies<>()
);
std::cout << "*r4: " << *r4 << '\n';
}
|output=
*r1: 36
*r2: ABCD
*r3: 729
*r4: 42

## References


## See also


| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

