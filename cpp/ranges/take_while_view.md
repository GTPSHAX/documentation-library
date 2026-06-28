---
title: std::ranges::views::take_while
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V, class Pred >
requires ranges::input_range<V> &&
std::is_object_v<Pred> &&
std::indirect_unary_predicate<const Pred, ranges::iterator_t<V>>
class take_while_view
: public ranges::view_interface<take_while_view<V, Pred>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /*unspecified*/ take_while = /*unspecified*/;
}
dcl|since=c++20|1=
template< ranges::viewable_range R, class Pred >
requires /* see below */
constexpr ranges::view auto take_while( R&& r, Pred&& pred );
dcl|since=c++20|1=
template< class Pred >
constexpr /*range adaptor closure*/ take_while( Pred&& pred );
```

1. A range adaptor that represents  of the elements from an underlying sequence, starting at the beginning and ending at the first element for which the predicate returns `false`.
2. *RangeAdaptorObject*. The expression `views::take_while(e, f)` is expression-equivalent to `take_while_view(e, f)` for any suitable subexpressions `e` and `f`.
`take_while_view` models the concepts , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc pred|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|take_while_view | (see dedicated page) |


## 


## Nested classes


## Notes

For s, `views::take_while(v, pred)` is similar to }, but the latter invokes `pred` only during construction (while the former invokes `pred` each time a valid `take_while` iterator is compared to a sentinel).

## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    for (int year : std::views::iota(2020)
                  {{!
```

std::cout << year << ' ';
std::cout << '\n';
const char note[]{"Today is yesterday's tomorrow!..."};
auto not_dot = [](char c){ return c != '.'; };
for (char x : std::ranges::take_while_view(note, not_dot))
std::cout << x;
std::cout << '\n';
}
|output=
2020 2021 2022 2023 2024 2025
Today is yesterday's tomorrow!

## See also


| cpp/ranges/dsc take_view | (see dedicated page) |
| cpp/ranges/dsc drop_while_view | (see dedicated page) |

