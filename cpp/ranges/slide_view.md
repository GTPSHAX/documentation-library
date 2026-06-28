---
title: std::ranges::views::slide
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::forward_range V >
requires ranges::view<V>
class slide_view
: public ranges::view_interface<slide_view<V>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ slide = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
constexpr ranges::view auto slide( R&& r, ranges::range_difference_t<R> n );
dcl|since=c++23|1=
template< class DifferenceType >
constexpr /* range adaptor object */ slide( DifferenceType&& n );
dcla|anchor=slide-caches-nothing|num=3|notes=|1=
template< class V >
concept /*slide-caches-nothing*/ =
ranges::random_access_range<V> && ranges::sized_range<V>;
dcla|anchor=slide-caches-last|num=4|notes=|1=
template< class V >
concept /*slide-caches-last*/ =
!/*slide-caches-nothing*/<V> &&
ranges::bidirectional_range<V> && ranges::common_range<V>;
dcla|anchor=slide-caches-first|num=5|notes=|1=
template< class V >
concept /*slide-caches-first*/ =
!/*slide-caches-nothing*/<V> && !/*slide-caches-last*/<V>;
```

1. `slide_view` is a range adaptor that takes a  and a number `n` and produces a view whose `''m'' element (a “window”) is a view over  elements of the original view.
@@ Let `s` be the size of the original view. Then the size of produced view is:
* `s - n + 1`, if `1=s >= n`,
* `0` otherwise, and the resulting view is empty.
2. The name `views::slide` denotes a *RangeAdaptorObject*. Given subexpressions `e` and `n`, the expression `views::slide(e, n)` is expression-equivalent to `slide_view(e, n)`.
If `n` is not greater than `0`, the behavior is undefined.
`slide_view` always models , and models , , or  if adapted  type models the corresponding concept.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|slide_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|slide_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|slide_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|slide_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|slide_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class V >
constexpr bool ranges::enable_borrowed_range<slide_view<V>> =
ranges::enable_borrowed_range<V>;
This specialization of `ranges::enable_borrowed_range` makes `slide_view` satisfy  when the underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <ranges>

auto print_subrange = [](std::ranges::viewable_range auto&& r)
{
    std::cout << '[';
    for (char space[]{0,0}; auto elem : r)
        std::cout << space << elem, *space = ' ';
    std::cout << "] ";
};

int main()
{
    const auto v = {1, 2, 3, 4, 5, 6};

    std::cout << "All sliding windows of width:\n";
    for (const unsigned width : std::views::iota(1U, 1U + v.size()))
    {
        auto const windows = v {{!
```

std::cout << "W = " << width << ": ";
std::ranges::for_each(windows, print_subrange);
std::cout << '\n';
}
}
|output=
All sliding windows of width W:
W = 1: [1] [2] [3] [4] [5] [6]
W = 2: [1 2] [2 3] [3 4] [4 5] [5 6]
W = 3: [1 2 3] [2 3 4] [3 4 5] [4 5 6]
W = 4: [1 2 3 4] [2 3 4 5] [3 4 5 6]
W = 5: [1 2 3 4 5] [2 3 4 5 6]
W = 6: [1 2 3 4 5 6]

## References


## See also


| cpp/ranges/dsc adjacent_view | (see dedicated page) |
| cpp/ranges/dsc chunk_view | (see dedicated page) |

