---
title: std::ranges::fold_left_first
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_left_first
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++23|1=
template< std::input_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-left-foldable*/<std::iter_value_t<I>, I> F >
requires std::constructible_from<std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr auto
fold_left_first( I first, S last, F f );
dcl|num=2|since=c++23|1=
template< ranges::input_range R,
/*indirectly-binary-left-foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F >
requires std::constructible_from<
ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr auto
fold_left_first( R&& r, F f );
|1=
template< class F, class T, class I >
concept /*indirectly-binary-left-foldable*/ = /* see description */;
```

Left-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(f(f(f(x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_left_first` behaves like `std::accumulate`'s overload that accepts a binary predicate, except that the `*first` is used internally as an initial element.
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last). Equivalent to
`return ranges::fold_left_first_with_iter(std::move(first), last, f).value`.
2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `f` - the binary function object

## Return value

An object of type `std::optional<U>` that contains the result of left-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of the given range over `f`, where `U` is equivalent to
`decltype(ranges::fold_left(std::move(first), last, std::iter_value_t<I>(*first), f))`.
If the range is empty, `std::optional<U>()` is returned.

## Possible implementations

eq fun
|1=
struct fold_left_first_fn
{
template<std::input_iterator I, std::sentinel_for<I> S,
/*indirectly-binary-left-foldable*/<std::iter_value_t<I>, I> F>
requires
std::constructible_from<std::iter_value_t<I>, std::iter_reference_t<I>>
constexpr auto operator()(I first, S last, F f) const
{
using U = decltype(
ranges::fold_left(std::move(first), last, std::iter_value_t<I>(*first), f)
);
if (first == last)
return std::optional<U>();
std::optional<U> init(std::in_place, *first);
for (++first; first != last; ++first)
*init = std::invoke(f, std::move(*init), *first);
return std::move(init);
}
template<ranges::input_range R,
/*indirectly-binary-left-foldable*/<
ranges::range_value_t<R>, ranges::iterator_t<R>> F>
requires
std::constructible_from<ranges::range_value_t<R>, ranges::range_reference_t<R>>
constexpr auto operator()(R&& r, F f) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::ref(f));
}
};
inline constexpr fold_left_first_fn fold_left_first;

## Complexity

Exactly `ranges::distance(first, last) - 1` (assuming the range is not empty) applications of the function object `f`.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <ranges>
#include <utility>

int main()
{
    constexpr std::array v{1, 2, 3, 4, 5, 6, 7, 8};
    static_assert
    (
        *std::ranges::fold_left_first(v.begin(), v.end(), std::plus{}) == 36
        && *std::ranges::fold_left_first(v, std::multiplies{}) == 40320
    );

    constexpr std::array w
    {
        1, 2, 3, 4, 13,
        1, 2, 3, 4, 13,
        1, 2, 3, 4, 13,
        1, 2, 3, 4,
    };
    static_assert
    (
        "Find the only value that (by precondition) occurs odd number of times:"
        && *std::ranges::fold_left_first(w, [](int p, int q){ return p ^ q; }) == 13
    );

    constexpr auto pairs = std::to_array<std::pair<char, float>>
    ({
        {'A', 3.0f},
        {'B', 3.5f},
        {'C', 4.0f}
    });
    static_assert
    (
        "Get the product of all pair::second in pairs:"
        && *std::ranges::fold_left_first
        (
            pairs {{!
```

) == 42
);
}

## References


## See also


| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

