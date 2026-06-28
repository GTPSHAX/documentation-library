---
title: std::ranges::enumerate_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator
---

ddcl|since=c++23|notes=|
template< bool Const >
class /*iterator*/
The return type of `enumerate_view::begin`, and of `enumerate_view::end` when the underlying view `V` is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::random_access_iterator_tag`, if  models . Otherwise, | |
| * `std::bidirectional_iterator_tag`, if  models . Otherwise, | |
| * `std::forward_iterator_tag`, if  models . Otherwise, | |
| * `std::input_iterator_tag`. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|enumerate_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/enumerate_view/iterator/operator cmp|title=operator==<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/enumerate_view/iterator/operator arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |
| cpp/ranges/enumerate_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |


## Example

<!--===See also===


| cpp/ranges/elements_view/dsc iterator | (see dedicated page) |

