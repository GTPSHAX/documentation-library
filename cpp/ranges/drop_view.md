---
title: std::ranges::views::drop
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V >
class drop_view
: public ranges::view_interface<drop_view<V>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ drop = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto
drop( R&& r, ranges::range_difference_t<R> count );
dcl|since=c++20|1=
template< class DifferenceType >
constexpr /* range adaptor closure */ drop( DifferenceType&& count );
```

1. A range adaptor consisting of elements of the underlying sequence, skipping the first ''N'' elements.
2. *RangeAdaptorObject*. Given `T` is `std::remove_cvref_t<decltype((e))>` and `D` is `ranges::range_difference_t<decltype((e))>`), the expression `views::drop(e, f)` is expression-equivalent to:
* , if `T` is a , except that the evaluations of `e` and `f` are indeterminately sequenced;
* otherwise, c multi|
T(ranges::begin(e) + inc, ranges::end(e),|
/*to-unsigned-like*/(ranges::distance(e) - inc))
, if `T` is a specialization of `ranges::subrange` that models both  and , and `T` needs to store the size (see  for details), where `inc` is `std::min<D>(ranges::distance(e), f)`;
* otherwise, `U(ranges::begin(e) + inc, ranges::end(e))`, if `T` is a specialization of `std::span`, `std::basic_string_view`, `ranges::iota_view`, or `ranges::subrange` that models both  and , where `U` is
:* `std::span<typename T::element_type>`, if `T` is a specialization of `std::span`;
:* `T` otherwise;
rrev|since=c++23|
* otherwise, if `T` is a specialization of :
:* `views::repeat(*e.value_, ranges::distance(e) - inc)`, if `T` models ; in such case `e` is evaluated only once;
:* `((void)e, auto(f))` otherwise, except that the evaluations of `e` and `f` are indeterminately sequenced;
* otherwise, `drop_view(e, f)`.
In all cases, `decltype((f))` must model `std::convertible_to<D>`.
`drop_view` models the concepts , , , , , , and  when the underlying view `V` models respective concepts.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|drop_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|drop_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|drop_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|drop_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|drop_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|drop_view | (see dedicated page) |


## 


## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::drop_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `drop_view` satisfy  when the underlying view satisfies it.

## Example


### Example

```cpp
#include <initializer_list>
#include <iostream>
#include <ranges>

int main()
{
    const auto nums = {1, 2, 3, 4, 5, 6, 7};

    std::cout << "drop " << 2 << ": ";
    for (int i : std::ranges::drop_view{nums, 2})
        std::cout << i << ' ';
    std::cout << '\n';

    std::cout << "drop " << 3 << ": ";
    for (int i : nums {{!
```

std::cout << i << ' ';
std::cout << '\n';
std::cout << "drop " << 4 << ": ";
for (int i : std::views::iota(1, 8) | std::views::drop(4))
std::cout << i << ' ';
std::cout << '\n';
// Note that dropping more than the number of elements is OK:
for (int dp : {5, 6, 7, 890, 100500})
{
std::cout << "drop " << dp << ": ";
for (int i : std::views::iota(1, 8) | std::views::drop(dp))
std::cout << i << ' ';
std::cout << '\n';
}
}
|output=
drop 2: 3 4 5 6 7
drop 3: 4 5 6 7
drop 4: 5 6 7
drop 5: 6 7
drop 6: 7
drop 7:
drop 890:
drop 100500:

## Defect reports


## See also


| cpp/ranges/dsc drop_while_view | (see dedicated page) |

