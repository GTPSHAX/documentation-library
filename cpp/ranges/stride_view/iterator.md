---
title: std::ranges::stride_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator
---

ddcl|since=c++23|notes=|
template< bool Const >
class /*iterator*/
The return type of `stride_view::begin`, and of `stride_view::end` when the underlying view `V` is a .
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
| dsc|`iterator_category`<br>|Let  denote the type `iterator_traits<iterator_t<Base>>::iterator_category`. | |
| * `std::random_access_iterator_tag`, if  models `std::derived_from<std::random_access_iterator_tag>`. | |
| *  otherwise. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|stride_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/stride_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/stride_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |
| cpp/ranges/stride_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/stride_view/iterator/iter_swap|swaps underlying pointed-to elements|notes= | |


## Example


## See also


| cpp/ranges/slide_view/dsc iterator | (see dedicated page) |

