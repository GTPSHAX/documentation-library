---
title: std::ranges::views::take
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V >
class take_view
: public ranges::view_interface<take_view<V>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ take = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto
take( R&& r, ranges::range_difference_t<R> count );
dcl|since=c++20|1=
template< class DifferenceType >
constexpr /* range adaptor closure */ take( DifferenceType&& count );
```

1. A range adaptor that represents  of the elements from an underlying sequence, starting at the beginning and ending at a given bound.
2. `views::take` is a *RangeAdaptorObject*. The expression `views::take(e, f)` results in a view that represents the first `f` elements from `e`. The result is not necessarily a `take_view`.
`views::take(e, f)` is expression-equivalent to (where `T` is `std::remove_cvref_t<decltype((e))>` and `D` is `ranges::range_difference_t<decltype((e))>`):
* , if `T` is a `ranges::empty_view`, except that the evaluations of `e` and `f` are indeterminately sequenced;
* `U(ranges::begin(e), ranges::begin(e) + std::min<D>(ranges::distance(e), f))`, if `T` is a specialization of `std::span`, `std::basic_string_view`, or `ranges::subrange` that models both  and , where `U` is
:* `std::span<typename T::element_type>`, if `T` is a specialization of `std::span`;
:* `T`, if `T` is a specialization of `std::basic_string_view`;
:* `ranges::subrange<ranges::iterator_t<T>>`, if `T` is a specialization of `ranges::subrange`;
* , if `T` is a specialization of `ranges::iota_view` that models both  and ;
rrev|since=c++23|
* otherwise, if `T` is a specialization of :
:* `views::repeat(*e.value_, std::min<D>(ranges::distance(e), f))`, if `T` models ; is such case `e` is evaluated only once;
:* `views::repeat(*e.value_, static_cast<D>(e))` otherwise;
* otherwise, `take_view(e, f)`.
In all cases, `decltype((f))` must model `std::convertible_to<D>`.
`take_view` models the concepts , , , ,  , and  when the underlying view `V` models respective concepts. It models  when the underlying view `V` models both  and .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|take_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|take_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|take_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|take_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|take_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|take_view | (see dedicated page) |


## 


## Nested classes


## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::take_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `take_view` satisfy  when the underlying view satisfies it.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>

int main()
{
    namespace views = std::views;
    auto print = [](char x){ std::cout << x; };

    for (const char nums[]{'1', '2', '3'};
         int n : views::iota(0, 5))
    {
        std::cout << "take(" << n << "): ";
        // safely takes only upto min(n, nums.size()) elements:
        std::ranges::for_each(nums {{!
```

std::cout << '\n';
}
}
|output=
take(0):
take(1): 1
take(2): 12
take(3): 123
take(4): 123

## Defect reports


## See also


| cpp/ranges/dsc view_counted | (see dedicated page) |
| cpp/ranges/dsc take_while_view | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |

