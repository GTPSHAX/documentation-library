---
title: std::ranges::slide_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/iterator
---

ddcla|since=c++23|expos=yes|
template< bool Const >
class /*iterator*/
The return type of `slide_view::begin`, and of `slide_view::end` when the underlying view `V` is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::random_access_iterator_tag`, if  models . Otherwise, | |
| * `std::bidirectional_iterator_tag`, if  models . Otherwise, | |
| * `std::forward_iterator_tag`. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|slide_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/slide_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/slide_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |


## Example


## See also


| <!-- | |
| cpp/ranges/slide_view/dsc sentinel | (see dedicated page) |
| --> | |

