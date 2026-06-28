---
title: std::ranges::elements_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/iterator
---

ddcl|notes=|
template< bool Const >
class /*iterator*/;
The return type of `elements_view::begin`, and of `elements_view::end` when the underlying view is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`|Denotes: | |
| * `std::random_access_iterator_tag`, if  models . Otherwise, | |
| * `std::bidirectional_iterator_tag`, if  models . Otherwise, | |
| * `std::forward_iterator_tag`, if  models . Otherwise, | |
| * `std::input_iterator_tag`. | |
| dsc|`iterator_category`<br>|Not defined, if  does not model . Otherwise, | |
| * `std::input_iterator_tag`, if `std::get<N>(*current_)` is an rvalue. Otherwise, let  be the type `std::iterator_traits<std::iterator_t<Base>>::iterator_category`. | |
| * `std::random_access_iterator_tag`, if  models `std::derived_from<std::random_access_iterator_tag>`. Otherwise, | |
| * . | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|elements_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/elements_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/elements_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |


## Defect reports


## See also


| cpp/ranges/transform_view/dsc iterator | (see dedicated page) |

