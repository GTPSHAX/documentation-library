---
title: std::ranges::views::pairwise
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::forward_range V, std::size_t N >
requires ranges::view<V> && (N > 0)
class adjacent_view
: public ranges::view_interface<adjacent_view<V, N>>
dcl|num=2|since=c++23|1=
namespace views {
template< std::size_t N >
constexpr /* unspecified */ adjacent = /* unspecified */ ;
}
dcl|num=3|since=c++23|1=
namespace views {
inline constexpr auto pairwise = adjacent<2>;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto adjacent<N>( R&& r );
```

1. `adjacent_view` is a range adaptor that takes a , and produces a  whose  element (a “window”) is a `std::tuple` that holds  references to the elements  of the original view.
@@ Let  be the size of the original view. Then the size of produced view is:
* `S - N + 1`, if `1=S >= N`,
* `0` otherwise, and the resulting view is empty.
2. The name `views::adjacent<N>` denotes a *RangeAdaptorObject*. Given a subexpression `e` and a constant expression `N`, the expression `views::adjacent<N>(e)` is expression-equivalent to
* `((void)e, auto(views::empty<tuple<>>))` if `N` is equal to `0` and `decltype((e))` models ,
* `adjacent_view<views::all_t<decltype((e))>, N>(e)` otherwise.
3. The name `views::pairwise` denotes a *RangeAdaptorObject* that behaves exactly as `views::adjacent<2>`.
`adjacent_view` always models , and models , , or  if adapted  type models the corresponding concept.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|adjacent_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|adjacent_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|adjacent_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|adjacent_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|adjacent_view | (see dedicated page) |


## Deduction guides

(none)

## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class V, size_t N >
constexpr bool ranges::enable_borrowed_range<adjacent_view<V, N>> =
ranges::enable_borrowed_range<V>;
This specialization of `ranges::enable_borrowed_range` makes `adjacent_view` satisfy  when the underlying view satisfies it.

## Notes

`views::adjacent` only accepts forward ranges even when `N` is `0`.

## Example


### Example

```cpp
#include <array>
#include <format>
#include <iostream>
#include <ranges>
#include <tuple>

int main()
{
    constexpr std::array v{1, 2, 3, 4, 5, 6};
    std::cout << "v = [1 2 3 4 5 6]\n";

    for (int i{}; std::tuple t : v {{!
```

{
auto [t0, t1, t2] = t;
std::cout << std::format("e = {:<{[{} {} {}]\n", "", 2 * i++, t0, t1, t2);
}
}
|output=
v = [1 2 3 4 5 6]
e = [1 2 3]
e =   [2 3 4]
e =     [3 4 5]
e =       [4 5 6]

## Defect reports


## References


## See also


| cpp/ranges/dsc adjacent_transform_view | (see dedicated page) |
| cpp/ranges/dsc views pairwise_transform | (see dedicated page) |
| cpp/ranges/dsc slide_view | (see dedicated page) |
| cpp/ranges/dsc chunk_view | (see dedicated page) |
| cpp/ranges/dsc stride_view | (see dedicated page) |

