---
title: std::ranges::views::stride
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::input_range V >
requires ranges::view<V>
class stride_view
: public ranges::view_interface<stride_view<V>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ stride = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
constexpr ranges::view auto stride( R&& r, ranges::range_difference_t<R> n );
dcl|since=c++23|1=
template< class DifferenceType >
constexpr /*range adaptor closure*/ stride( DifferenceType&& n );
```

1. `stride_view` is a range adaptor that takes a  and a number  and produces a view, that consists of elements of the original view by advancing over ''n'' elements at a time. This means that each  element of the produced view is  element of the original view, for some non-negative index .
The elements of the original view, whose “index” is not a multiple of , are not present in the produced view.
@@ Let  be the size of the original view. Then the size of produced view is:
* `(S / n) + (S % n ? 1 : 0)`, if `1=S >= n`; otherwise,
* `1`, if `S > 0`; otherwise,
* `0`, and the resulting view is empty.
2. The name `views::stride` denotes a *RangeAdaptorObject*. Given subexpressions `e` and `n`, the expression `views::stride(e, n)` is expression-equivalent to `stride_view(e, n)`.
@@ The `n` must be greater than `0`, otherwise the behavior is undefined.
`stride_view` always models , and models , , , and/or , if adapted  type `V` models the corresponding concept.
`stride_view<V>` models  whenever the underlying view `V` does.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|stride_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|stride_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|stride_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|stride_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|stride_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|stride_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class V >
constexpr bool ranges::enable_borrowed_range<stride_view<V>> =
ranges::enable_borrowed_range<V>;
This specialization of `ranges::enable_borrowed_range` makes `stride_view` satisfy  when the underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string_view>
using namespace std::literals;

void print(std::ranges::viewable_range auto&& v, std::string_view separator = " ")
{
    for (auto const& x : v)
        std::cout << x << separator;
    std::cout << '\n';
}

int main()
{
    print(std::views::iota(1, 13) {{!
```

print(std::views::iota(1, 13) | std::views::stride(3) | std::views::reverse);
print(std::views::iota(1, 13) | std::views::reverse | std::views::stride(3));
print("0x0!133713337*x//42/A$@"sv | std::views::stride(0B11) |
std::views::transform([](char O) -> char { return 0100 | O; }),
"");
}
|output=
1 4 7 10
10 7 4 1
12 9 6 3
password

## References


## See also


| cpp/ranges/dsc slide_view | (see dedicated page) |
| cpp/ranges/dsc chunk_view | (see dedicated page) |
| cpp/ranges/dsc adjacent_view | (see dedicated page) |
| cpp/ranges/dsc filter_view | (see dedicated page) |

