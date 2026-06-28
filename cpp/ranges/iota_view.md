---
title: std::ranges::views::iota
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/iota_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< std::weakly_incrementable W,
std::semiregular Bound = std::unreachable_sentinel_t >
requires /*weakly-equality-comparable-with*/<W, Bound> && std::copyable<W>
class iota_view
: public ranges::view_interface<iota_view<W, Bound>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ iota = /* unspecified */;
}
dcla|num=3|since=c++26|1=
namespace views {
inline constexpr /* unspecified */ indices = /* unspecified */;
}
dcl|since=c++20|1=
template< class W >
requires /* see below */
constexpr /* see below */ iota( W&& value );
dcl|since=c++20|1=
template< class W, class Bound >
requires /* see below */
constexpr /* see below */ iota( W&& value, Bound&& bound );
dcl|since=c++26|1=
template< class T >
requires /*is-integer-like*/<T>
constexpr /* see below */ indices( T bound );
```

1. A range factory that generates a sequence of elements by repeatedly incrementing an initial value. Can be either bounded or unbounded (infinite).
2. `views::iota(e)` and `views::iota(e, f)` are expression-equivalent to `iota_view<std::decay_t<decltype((e))>>(e)` and `iota_view(e, f)` respectively for any suitable subexpressions `e` and `f`.
3. Let `T` be `std::remove_cvref_t<decltype((e))>`. Then `views::indices(e)` is expression-equivalent to `views::iota(T(0), e)` for any suitable subexpression `e` if `/*is-integer-like*/<T>` is `true`.
rrev|since=c++26|

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## 


## Nested classes


## Helper templates

ddcl|since=c++20|1=
template< std::weakly_incrementable W, std::semiregular Bound >
constexpr bool ranges::enable_borrowed_range<ranges::iota_view<W, Bound>> = true;
This specialization of `ranges::enable_borrowed_range` makes `iota_view` satisfy .

## Possible implementation

See also the implementation in [https://github.com/gcc-mirror/gcc/blob/6f3c04e20625dee7c32b1ec43cb0812e38f4394b/libstdc%2B%2B-v3/include/std/ranges#L919 libstdc++].
eq impl
|title1=views::indices (3)|ver1=3|1=
namespace views {
inline constexpr auto indices = []</*is-integer-like*/ I>(I n)
{
return views::iota(I{}, n);
};
}

## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_ranges_indices` | 202506L | C++26 | `ranges::views::indices` |


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>

struct Bound
{
    int bound;
    bool operator==(int x) const { return x == bound; }
};

int main()
{
    for (int i : std::ranges::iota_view{1, 10})
        std::cout << i << ' ';
    std::cout << '\n';

    for (int i : std::views::iota(1, 10))
        std::cout << i << ' ';
    std::cout << '\n';

    for (int i : std::views::iota(1, Bound{10}))
        std::cout << i << ' ';
    std::cout << '\n';

    for (int i : std::views::iota(1) {{!
```

std::cout << i << ' ';
std::cout << '\n';
std::ranges::for_each(std::views::iota(1, 10),
[](int i){ std::cout << i << ' '; });
std::cout << '\n';
#if __cpp_lib_ranges_indices
constexpr int v[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
// auto broken_indices = views::iota(0, std::ranges::size(v));
//     does not compile due to types (int VS size_t) mismatch
auto good_indices = std::views::indices(std::ranges::size(v));
for (auto i : good_indices)
std::cout << v[i] << ' ';
std::cout << '\n';
#endif
}
|output=
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9

## Defect reports


## References


## See also


| cpp/algorithm/dsc iota | (see dedicated page) |
| cpp/algorithm/ranges/dsc iota | (see dedicated page) |
| cpp/ranges/dsc repeat_view | (see dedicated page) |
| cpp/ranges/dsc enumerate_view | (see dedicated page) |

