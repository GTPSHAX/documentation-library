---
title: std::ranges::transform_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/iterator
---

ddcl|since=c++20|notes=|
template< bool Const >
class /*iterator*/
The return type of `transform_view::begin`, and of `transform_view::end` when the underlying view is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| *`std::random_access_iterator_tag`, if  models , | |
| *`std::bidirectional_iterator_tag`, if  models , | |
| *`std::forward_iterator_tag`, if  models , | |
| *`std::input_iterator_tag` otherwise. | |
| dsc|`iterator_category`<br>|Let `MCF` be . | |
| *`std::input_iterator_tag`, if `std::invoke_result_t<MCF&, ranges::range_reference_t<Base>>` is not a reference. | |
| Otherwise, let  be `std::iterator_traits<ranges::iterator_t<Base>>::iterator_category`. | |
| *`std::random_access_iterator_tag`, if  is `std::contiguous_iterator_tag`; | |
| *, otherwise. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Non-member functions


| cpp/ranges/transform_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/transform_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |
| cpp/ranges/transform_view/iterator/iter_move|obtains an rvalue reference to the transformed element|notes= | |


## Defect reports

