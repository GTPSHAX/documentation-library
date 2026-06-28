---
title: std::ranges::views::enumerate
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::view V >
requires /*range-with-movable-references*/<V>
class enumerate_view
: public ranges::view_interface<enumerate_view<V>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ enumerate = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr /* see below */ enumerate( R&& r );
|1=
template< class R >
concept /*range-with-movable-references*/ =
ranges::input_range<R> &&
std::move_constructible<ranges::range_reference_t<R>> &&
std::move_constructible<ranges::range_rvalue_reference_t<R>>;
```

1. `enumerate_view` is a range adaptor that takes a  and produces a view of `std::tuple|tuple`s. `i` element (the tuple) of the resulting sequence holds:
* the value equal to `i`, which is a zero-based index of the element of underlying sequence, and
* the reference to the underlying element.
2. The name `views::enumerate` denotes a *RangeAdaptorObject*. Given a subexpression `e`, the expression `views::enumerate(e)` is expression-equivalent to `enumerate_view<views::all_t<decltype((e))>>(e)` for any suitable subexpression `e`.
3. Ensures that the reference type of the underlying type can be moved.
`enumerate_view` models the concepts , , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|enumerate_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|enumerate_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|enumerate_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|enumerate_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|enumerate_view|notes | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|enumerate_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++23|1=
template< class View >
constexpr bool enable_borrowed_range<ranges::enumerate_view<View>> =
ranges::enable_borrowed_range<View>;
This specialization of `ranges::enable_borrowed_range` makes `enumerate_view` satisfy  when the underlying view satisfies it.

## Notes


## Example


### Example

```cpp
#include <initializer_list>
#include <iostream>
#include <map>
#include <ranges>
#include <vector>

int main()
{
    constexpr static auto v = {'A', 'B', 'C', 'D'};

    for (auto const [index, letter] : std::views::enumerate(v))
        std::cout << '(' << index << ':' << letter << ") ";
    std::cout << '\n';

#if __cpp_lib_ranges_to_container
    // create a map using the position of each element as key
    auto m = v {{!
```

for (auto const [key, value] : m)
std::cout << '[' << key << "]:" << value << ' ';
std::cout << '\n';
#endif
std::vector<int> numbers{1, 3, 5, 7};
// num is mutable even with const, which does not propagate to reference to
// make it const, use `std::views::enumerate(numbers) | std::views::as_const`
// or `std::views::enumerate(std::as_const(numbers))`
for (auto const [index, num] : std::views::enumerate(numbers))
{
++num; // the type is int&
std::cout << numbers[index] << ' ';
}
std::cout << '\n';
}
|p=true
|output=
(0:A) (1:B) (2:C) (3:D)
[0]:A [1]:B [2]:C [3]:D
2 4 6 8

## References


## See also


| cpp/ranges/dsc iota_view | (see dedicated page) |
| cpp/ranges/dsc views indices | (see dedicated page) |
| cpp/ranges/dsc zip_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |

