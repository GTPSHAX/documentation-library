---
title: std::ranges::fold_left_with_iter
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_left_with_iter
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=1|since1=c++23|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S, class T,
/* indirectly-binary-left-foldable */<T, I> F >
constexpr /* see description */
fold_left_with_iter( I first, S last, T init, F f );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class T = std::iter_value_t<I>,
/* indirectly-binary-left-foldable */<T, I> F >
constexpr /* see description */
fold_left_with_iter( I first, S last, T init, F f );
dcl rev multi|num=2|since1=c++23|until1=c++26
|dcl1=
template< ranges::input_range R, class T,
/* indirectly-binary-left-foldable */
<T, ranges::iterator_t<R>> F >
constexpr /* see description */
fold_left_with_iter( R&& r, T init, F f );
|dcl2=
template< ranges::input_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-left-foldable */
<T, ranges::iterator_t<R>> F >
constexpr /* see description */
fold_left_with_iter( R&& r, T init, F f );
|1=
template< class F, class T, class I >
concept /* indirectly-binary-left-foldable */ = /* see description */;
dcl|num=4|since=c++23|1=
template< class I, class T >
using fold_left_with_iter_result = ranges::in_value_result<I, T>;
```

Left-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(f(f(f(init, x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_left_with_iter` behaves like `std::accumulate`'s overload that accepts a binary predicate.
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last).
2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.
4. The return type alias. See "" section for details.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `init` - the initial value of the fold
- `f` - the binary function object

## Return value

Let `U` be `std::decay_t<std::invoke_result_t<F&, T, std::iter_reference_t<I>>>`.
1. An object of type `ranges::fold_left_with_iter_result<I, U>`.
* The member `ranges::in_value_result::in` holds an iterator to the end of the range.
* The member `ranges::in_value_result::value` holds the result of the left-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of given range over `f`.
If the range is empty, the return value is obtained via the expression equivalent to }.
2. Same as  except that the return type is `ranges::fold_left_with_iter_result<ranges::borrowed_iterator_t<R>, U>`.

## Possible implementations

eq fun|1=
class fold_left_with_iter_fn
{
template<class O, class I, class S, class T, class F>
constexpr auto impl(I&& first, S&& last, T&& init, F f) const
{
using U = std::decay_t<std::invoke_result_t<F&, T, std::iter_reference_t<I>>>;
using Ret = ranges::fold_left_with_iter_result<O, U>;
if (first == last)
return Ret{std::move(first), U(std::move(init))};
U accum = std::invoke(f, std::move(init), *first);
for (++first; first != last; ++first)
accum = std::invoke(f, std::move(accum), *first);
return Ret{std::move(first), std::move(accum)};
}
public:
template<std::input_iterator I, std::sentinel_for<I> S, class T = std::iter_value_t<I>,
/* indirectly-binary-left-foldable */<T, I> F>
constexpr auto operator()(I first, S last, T init, F f) const
{
return impl<I>(std::move(first), std::move(last), std::move(init), std::ref(f));
}
template<ranges::input_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-left-foldable */<T, ranges::iterator_t<R>> F>
constexpr auto operator()(R&& r, T init, F f) const
{
return impl<ranges::borrowed_iterator_t<R>>
(
ranges::begin(r), ranges::end(r), std::move(init), std::ref(f)
);
}
};
inline constexpr fold_left_with_iter_fn fold_left_with_iter;

## Complexity

Exactly `ranges::distance(first, last)` applications of the function object `f`.

## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_algorithm_default_value_type` | 202403L | C++26 | List-initialization for algorithms |


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <complex>
#include <functional>
#include <ranges>
#include <utility>
#include <vector>

int main()
{
    namespace ranges = std::ranges;

    std::vector v{1, 2, 3, 4, 5, 6, 7, 8};

    auto sum = ranges::fold_left_with_iter(v.begin(), v.end(), 6, std::plus<int>());
    assert(sum.value == 42);
    assert(sum.in == v.end());

    auto mul = ranges::fold_left_with_iter(v, 0X69, std::multiplies<int>());
    assert(mul.value == 4233600);
    assert(mul.in == v.end());

    // Get the product of the std::pair::second of all pairs in the vector:
    std::vector<std::pair<char, float>> data {<!---->{'A', 2.f}, {'B', 3.f}, {'C', 3.5f}<!---->};
    auto sec = ranges::fold_left_with_iter
    (
        data {{!
```

);
assert(sec.value == 42);
// Use a program defined function object (lambda-expression):
auto lambda = [](int x, int y){ return x + 0B110 + y; };
auto val = ranges::fold_left_with_iter(v, -42, lambda);
assert(val.value == 42);
assert(val.in == v.end());
using CD = std::complex<double>;
std::vector<CD> nums1, 1}, {2, 0}, {3, 0;
#ifdef __cpp_lib_algorithm_default_value_type
auto res = ranges::fold_left_with_iter(nums, {7, 0}, std::multiplies{});
#else
auto res = ranges::fold_left_with_iter(nums, CD{7, 0}, std::multiplies{});
#endif
assert((res.value == CD{42, 42}));
}

## References


## See also


| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

