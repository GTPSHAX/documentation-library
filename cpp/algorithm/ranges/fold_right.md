---
title: std::ranges::fold_right
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fold_right
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=1|since1=c++23|until1=c++26
|dcl1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S, class T,
/* indirectly-binary-right-foldable */<T, I> F >
constexpr auto fold_right( I first, S last, T init, F f );
|dcl2=
template< std::bidirectional_iterator I, std::sentinel_for<I> S,
class T = std::iter_value_t<I>,
/* indirectly-binary-right-foldable */<T, I> F >
constexpr auto fold_right( I first, S last, T init, F f );
dcl rev multi|num=2|since1=c++23|until1=c++26
|dcl1=
template< ranges::bidirectional_range R, class T,
/* indirectly-binary-right-foldable */
<T, ranges::iterator_t<R>> F >
constexpr auto fold_right( R&& r, T init, F f );
|dcl2=
template< ranges::bidirectional_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-right-foldable */
<T, ranges::iterator_t<R>> F >
constexpr auto fold_right( R&& r, T init, F f );
|1=
template< class F, class T, class I >
concept /* indirectly-binary-left-foldable */ = /* see description */;
|1=
template< class F, class T, class I >
concept /* indirectly-binary-right-foldable */ = /* see description */;
```

Right-[Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds) the elements of given range, that is, returns the result of evaluation of the chain expression:<br>`f(x, where `x, `x, ..., `x are elements of the range.
Informally, `ranges::fold_right` behaves like `ranges::fold_left(views::reverse(r), init, /*flipped*/(f))`.
The behavior is undefined if [first, last) is not a valid range.
1. The range is [first, last).
2. Same as , except that uses `r` as the range, as if by using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to fold, sentinel=yes}})` - 
- `r` - the range of elements to fold
- `init` - the initial value of the fold
- `f` - the binary function object

## Return value

An object of type `U` that contains the result of right-[Fold (higher-order function)|fold](https://en.wikipedia.org/wiki/Fold (higher-order function)|fold) of the given range over `f`, where `U` is equivalent to `std::decay_t<std::invoke_result_t<F&, std::iter_reference_t<I>, T>>;`.
If the range is empty, `U(std::move(init))` is returned.

## Possible implementations

eq fun|1=
struct fold_right_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S,
class T = std::iter_value_t<I>,
/* indirectly-binary-right-foldable */<T, I> F>
constexpr auto operator()(I first, S last, T init, F f) const
{
using U = std::decay_t<std::invoke_result_t<F&, std::iter_reference_t<I>, T>>;
if (first == last)
return U(std::move(init));
I tail = ranges::next(first, last);
U accum = std::invoke(f, *--tail, std::move(init));
while (first != tail)
accum = std::invoke(f, *--tail, std::move(accum));
return accum;
}
template<ranges::bidirectional_range R, class T = ranges::range_value_t<R>,
/* indirectly-binary-right-foldable */<T, ranges::iterator_t<R>> F>
constexpr auto operator()(R&& r, T init, F f) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(init), std::ref(f));
}
};
inline constexpr fold_right_fn fold_right;

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

using namespace std::literals;
namespace ranges = std::ranges;

int main()
{
    auto v = {1, 2, 3, 4, 5, 6, 7, 8};
    std::vector<std::string> vs{"A", "B", "C", "D"};

    auto r1 = ranges::fold_right(v.begin(), v.end(), 6, std::plus<>()); // (1)
    std::cout << "r1: " << r1 << '\n';

    auto r2 = ranges::fold_right(vs, "!"s, std::plus<>()); // (2)
    std::cout << "r2: " << r2 << '\n';

    // Use a program defined function object (lambda-expression):
    std::string r3 = ranges::fold_right
    (
        v, "A", [](int x, std::string s) { return s + ':' + std::to_string(x); }
    );
    std::cout << "r3: " << r3 << '\n';

    // Get the product of the std::pair::second of all pairs in the vector:
    std::vector<std::pair<char, float>> data{<!---->{'A', 2.f}, {'B', 3.f}, {'C', 3.5f}<!---->};
    float r4 = ranges::fold_right
    (
        data {{!
```

);
std::cout << "r4: " << r4 << '\n';
using CD = std::complex<double>;
std::vector<CD> nums1, 1}, {2, 0}, {3, 0;
#ifdef __cpp_lib_algorithm_default_value_type
auto r5 = ranges::fold_right(nums, {7, 0}, std::multiplies{});
#else
auto r5 = ranges::fold_right(nums, CD{7, 0}, std::multiplies{});
#endif
std::cout << "r5: " << r5 << '\n';
}
|output=
r1: 42
r2: ABCD!
r3: A:8:7:6:5:4:3:2:1
r4: 42
r5: (42,42)

## References


## See also


| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |

