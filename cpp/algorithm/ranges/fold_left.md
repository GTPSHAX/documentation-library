---
title: std::ranges::fold_left
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_left
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=1|since1=c++23|until1=c++26
|dcl1=
template< std::input_iterator I, std::sentinel_for<I> S, class T,
/* indirectly-binary-left-foldable */<T, I> F >
constexpr auto fold_left( I first, S last, T init, F f );
|dcl2=
template< std::input_iterator I, std::sentinel_for<I> S,
class T = std::iter_value_t<I>,
/* indirectly-binary-left-foldable */<T, I> F >
constexpr auto fold_left( I first, S last, T init, F f );
dcl rev multi|num=2|since1=c++23|until1=c++26
|dcl1=
template< ranges::input_range R, class T,
/* indirectly-binary-left-foldable */
<T, ranges::iterator_t<R>> F >
constexpr auto fold_left( R&& r, T init, F f );
|dcl2=
template< ranges::input_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-left-foldable */
<T, ranges::iterator_t<R>> F >
constexpr auto fold_left( R&& r, T init, F f );
|1=
template< class F, class T, class I >
concept /* indirectly-binary-left-foldable */ = /* see description */;
```

Left-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(f(f(f(init, x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_left` behaves like `std::accumulate`'s overload that accepts a binary predicate.
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last). Equivalent to
`return ranges::fold_left_with_iter(std::move(first), last, std::move(init), f).value`.
2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `init` - the initial value of the fold
- `f` - the binary function object

## Return value

An object of type `U` that contains the result of left-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of the given range over `f`, where `U` is equivalent to `std::decay_t<std::invoke_result_t<F&, T, std::iter_reference_t<I>>>`.
If the range is empty, `U(std::move(init))` is returned.

## Possible implementations

eq fun|1=
struct fold_left_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, class T = std::iter_value_t<I>,
/* indirectly-binary-left-foldable */<T, I> F>
constexpr auto operator()(I first, S last, T init, F f) const
{
using U = std::decay_t<std::invoke_result_t<F&, T, std::iter_reference_t<I>>>;
if (first == last)
return U(std::move(init));
U accum = std::invoke(f, std::move(init), *first);
for (++first; first != last; ++first)
accum = std::invoke(f, std::move(accum), *first);
return std::move(accum);
}
template<ranges::input_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-left-foldable */<T, ranges::iterator_t<R>> F>
constexpr auto operator()(R&& r, T init, F f) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(init), std::ref(f));
}
};
inline constexpr fold_left_fn fold_left;

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
#include <complex>
#include <functional>
#include <iostream>
#include <ranges>
#include <string>
#include <utility>
#include <vector>

int main()
{
    namespace ranges = std::ranges;

    std::vector v{1, 2, 3, 4, 5, 6, 7, 8};

    int sum = ranges::fold_left(v.begin(), v.end(), 0, std::plus<int>()); // (1)
    std::cout << "sum: " << sum << '\n';

    int mul = ranges::fold_left(v, 1, std::multiplies<int>()); // (2)
    std::cout << "mul: " << mul << '\n';

    // get the product of the std::pair::second of all pairs in the vector:
    std::vector<std::pair<char, float>> data {<!---->{'A', 2.f}, {'B', 3.f}, {'C', 3.5f}<!---->};
    float sec = ranges::fold_left
    (
        data {{!
```

);
std::cout << "sec: " << sec << '\n';
// use a program defined function object (lambda-expression):
std::string str = ranges::fold_left
(
v, "A", [](std::string s, int x) { return s + ':' + std::to_string(x); }
);
std::cout << "str: " << str << '\n';
using CD = std::complex<double>;
std::vector<CD> nums1, 1}, {2, 0}, {3, 0;
#ifdef __cpp_lib_algorithm_default_value_type
auto res = ranges::fold_left(nums, {7, 0}, std::multiplies{}); // (2)
#else
auto res = ranges::fold_left(nums, CD{7, 0}, std::multiplies{}); // (2)
#endif
std::cout << "res: " << res << '\n';
}
|output=
sum: 36
mul: 40320
sec: 42
str: A:1:2:3:4:5:6:7:8
res: (42,42)

## References


## See also


| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

