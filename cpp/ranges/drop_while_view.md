---
title: std::ranges::views::drop_while
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_while_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V, class Pred >
requires ranges::input_range<V> &&
std::is_object_v<Pred> &&
std::indirect_unary_predicate<const Pred, ranges::iterator_t<V>>
class drop_while_view
: public ranges::view_interface<drop_while_view<V, Pred>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ drop_while = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R, class Pred >
requires /* see below */
constexpr ranges::view auto drop_while( R&& r, Pred&& pred );
dcl|since=c++20|1=
template< class Pred >
constexpr /*range adaptor closure*/ drop_while( Pred&& pred );
```

1. A range adaptor that represents  of elements from an underlying sequence, beginning at the first element for which the predicate returns `false`.
2. *RangeAdaptorObject*. The expression `views::drop_while(e, f)` is expression-equivalent to `drop_while_view(e, f)` for any suitable subexpressions `e` and `f`.
`drop_while_view` models the concepts , , , , , and  when the underlying view `V` models respective concepts. It also models  if `ranges::forward_range<V>` and `std::sized_sentinel_for<ranges::sentinel_t<V>, ranges::iterator_t<V>>` are modeled.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|drop_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|drop_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc pred|drop_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|drop_while_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|drop_while_view | (see dedicated page) |


## 


## Helper templates

ddcl|since=c++20|1=
template< class T, class Pred >
constexpr bool enable_borrowed_range<std::ranges::drop_while_view<T, Pred>> =
ranges::enable_borrowed_range<T>;
This specialization of `std::ranges::enable_borrowed_range` makes `drop_while_view` satisfy  when the underlying view satisfies it.

## Notes

In order to provide the amortized constant time complexity required by the  concept, the result of  is cached within the `drop_while_view` object. If the underlying range is modified after the first call to `begin()`, subsequent uses of the `drop_while_view` object might have unintuitive behavior.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string>
#include <string_view>

using std::operator""sv;

[[nodiscard]]
constexpr bool is_space(char p) noexcept
{
    auto ne = [p](auto q) { return p != q; };
    return !!(" \t\n\v\r\f" {{!
```

};
nodiscard("trims the output")
constexpr std::string_view trim_left(std::string_view const in) noexcept
{
auto view = in | std::views::drop_while(is_space);
return {view.begin(), view.end()};
}
nodiscard("trims the output")
constexpr std::string trim(std::string_view const in)
{
auto view = in
| std::views::drop_while(is_space)
| std::views::reverse
| std::views::drop_while(is_space)
| std::views::reverse
;
return {view.begin(), view.end()};
}
int main()
{
static_assert(trim_left(" \n C++23") == "C++23"sv);
constexpr auto src{" \f\n\t\r\vHello, C++20!\f\n\t\r\v "sv};
static_assert(trim(src) == "Hello, C++20!");
static constexpr auto v = {0, 1, 2, 3, 4, 5};
for (int n : v | std::views::drop_while([](int i) { return i < 3; }))
std::cout << n << ' ';
std::cout << '\n';
}
|output=
3 4 5

## Defect reports


## See also


| cpp/ranges/dsc drop_view | (see dedicated page) |

