---
title: std::ranges::views::all_t
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/all_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
inline constexpr /* unspecified */ all = /* unspecified */;
dcl|num=2|since=c++20|1=
template< ranges::viewable_range R >
using all_t = decltype(views::all(std::declval<R>()));
```

1. A *RangeAdaptorObject* (also a *RangeAdaptorClosureObject*) that returns a  that includes all elements of its  argument.
@@ Given an expression `e` of type `R`, the expression `views::all(e)` is expression-equivalent to:
* Implicitly converting `e` to a `std::decay_t<R>` prvalue, if `std::decay_t<R>` models .
* Otherwise, } if that expression is well-formed.
* Otherwise, }.
2. Calculates the suitable  type of a  type.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <type_traits>
#include <vector>

int main()
{
    std::vector<int> v{0, 1, 2, 3, 4, 5};
    for (int n : std::views::all(v) {{!
```

std::cout << n << ' ';
std::cout << '\n';
static_assert(std::is_same<
decltype(std::views::single(42)),
std::ranges::single_view<int>
>{});
static_assert(std::is_same<
decltype(std::views::all(v)),
std::ranges::ref_view<std::vector<int, std::allocator<int>>>
>{});
int a[]{1, 2, 3, 4};
static_assert(std::is_same<
decltype(std::views::all(a)),
std::ranges::ref_view<int[4]>
>{});
static_assert(std::is_same<
decltype(std::ranges::subrange{std::begin(a) + 1, std::end(a) - 1}),
std::ranges::subrange<int*, int*, std::ranges::subrange_kind(1)>
>{});
}
|output=
0 1

## Defect reports


## See also


| cpp/ranges/dsc empty_view | (see dedicated page) |
| cpp/ranges/dsc single_view | (see dedicated page) |
| cpp/ranges/dsc owning_view | (see dedicated page) |

