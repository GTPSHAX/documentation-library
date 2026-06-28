---
title: std::ranges::views::pairwise_transform
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::forward_range V, std::move_constructible F, std::size_t N >
requires ranges::view<V> && (N > 0) && std::is_object_v<F> &&
std::regular_invocable<F&,
/*REPEAT*/(ranges::range_reference_t<V>, N)...> &&
/*can-reference*/<std::invoke_result_t<F&,
/*REPEAT*/(ranges::range_reference_t<V>, N)...>>
class adjacent_transform_view
: public ranges::view_interface<adjacent_transform_view<V, F, N>>
dcl|num=2|since=c++23|1=
namespace views {
template< std::size_t N >
constexpr /* unspecified */ adjacent_transform = /* unspecified */;
}
dcl|num=3|since=c++23|1=
namespace views {
inline constexpr auto pairwise_transform = adjacent_transform<2>;
}
dcl|since=c++23|
template< ranges::viewable_range R, class F >
requires /* see below */
constexpr ranges::view auto adjacent_transform<N>( R&& r, F&& fun );
dcl|since=c++23|
template< class F >
constexpr /*range adaptor closure*/ adjacent_transform<N>( F&& fun );
```

1. `adjacent_transform_view` is a range adaptor that takes a  and an invocable object `fun`, and produces a  whose  element is a value that is the result of applying `fun` to each element in [i, i + N) of the original view. `F` always has [arity](https://en.wikipedia.org/wiki/arity) `N`.
@@ Let  be the size of the original view. Then the size of produced view is:
* `S - N + 1`, if `1=S >= N`,
* `0` otherwise, and the resulting view is empty.
2. The name `views::adjacent_transform<N>` denotes a *RangeAdaptorObject*. Given subexpressions `e` and `f`, and a constant expression `N`, the expression `views::adjacent_transform<N>(e, f)` is expression-equivalent to:
* `((void)e, views::zip_transform(f))`, if `N` is equal to `0` and `decltype((e))` models  (except that the evaluations of `e` and `f` are indeterminately sequenced),
* `adjacent_transform_view<views::all_t<decltype((e))>, std::decay_t<decltype((f))>, N>(e, f)` otherwise.
3. The name `views::pairwise_transform` denotes a *RangeAdaptorObject* that behaves exactly as `views::adjacent_transform<2>`. In particular, the arity of `F` is also `2` and `fun` is a binary invocable object.
`adjacent_transform_view` always models , and models , , or , if adapted  type models the corresponding concept.

## Member functions


| cpp/ranges/adaptor/dsc constructor|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|adjacent_transform_view | (see dedicated page) |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc expos mem type|inner_iterator|private=yes| | |
| * `ranges::iterator_t<const InnerView>`, if `Const` is `true`. Otherwise, | |
| * `ranges::iterator_t<InnerView>` | |
| dsc expos mem type|inner_sentinel|private=yes| | |
| * `ranges::sentinel_t<const InnerView>`, if `Const` is `true`. Otherwise, | |
| * `ranges::sentinel_t<InnerView>` | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Nested classes


## Notes

`views::adjacent_transform` only accepts foward ranges even when `N` is `0`.

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <ranges>

int main()
{
    constexpr static std::array data{1, 2, 3, 4, 5, 6};
    constexpr int window{3};

    auto Fun = [](auto... ints) { return (... + ints); };
    // Alternatively, the Fun could be any ternary (if window == 3) callable, e.g.:
    // auto Fun = [](int x, int y, int z) { return x + y + z; };

    constexpr auto view = data {{!
```

static_assert(
view.size() == (data.size() - window + 1)
&& std::array{6, 9, 12, 15}
== std::array{view[0], view[1], view[2], view[3]}
&& view[0] == Fun(data[0], data[1], data[2])
&& view[1] == Fun(data[1], data[2], data[3])
&& view[2] == Fun(data[2], data[3], data[4])
&& view[3] == Fun(data[3], data[4], data[5])
);
for (int x : view)
std::cout << x << ' ';
std::cout << '\n';
}
|output=
6 9 12 15

## Defect reports


## References


## See also


| cpp/ranges/dsc adjacent_view | (see dedicated page) |
| cpp/ranges/dsc views pairwise | (see dedicated page) |
| cpp/ranges/dsc transform_view | (see dedicated page) |
| cpp/ranges/dsc zip_transform_view | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |

