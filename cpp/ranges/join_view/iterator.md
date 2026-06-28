---
title: std::ranges::join_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator
---

ddcl|since=c++20|notes=|
template< bool Const >
class /*iterator*/
The return type of `join_view::begin`, and of `join_view::end` when both the outer range `V` and the inner range `ranges::range_reference_t<V>` satisfy  and the parent `join_view` is a .
If `V` is not a simple view (e.g. if `ranges::iterator_t<const V>` is invalid or different from `ranges::iterator_t<V>`), `Const` is true for iterators returned from the const overloads, and false otherwise. If `V` is a simple view, `Const` is true if and only if `ranges::range_reference_t<V>` is a reference.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::bidirectional_iterator_tag`, if `ranges::range_reference_t<Base>` is a reference type, and  and `ranges::range_reference_t<Base>` each model ;<br> | |
| * `std::forward_iterator_tag`, if `ranges::range_reference_t<Base>` is a reference type, and  and `ranges::range_reference_t<Base>` each model ;<br> | |
| * `std::input_iterator_tag` otherwise. | |
| dsc|`iterator_category`<br>|Defined only if `iterator::iterator_concept` (see above) denotes `std::forward_iterator_tag`.<br> | |
| Let  be `std::iterator_traits<ranges::iterator_t<Base>>::iterator_category`, and let  be c multi | |
| |std::iterator_traits<ranges::iterator_t<ranges::range_reference_t<Base>>>:: | |
| |    iterator_category.<br> | |
| * `std::bidirectional_iterator_tag`, if  and  each model `std::derived_from<std::bidirectional_iterator_tag>`;<br> | |
| * `std::forward_iterator_tag`, if  and  each model `std::derived_from<std::forward_iterator_tag>`;<br> | |
| * `std::input_iterator_tag` otherwise. | |
| dsc|`difference_type`|c multi | |
| |std::common_type_t<ranges::range_difference_t<Base>, | |
| |                   ranges::range_difference_t<ranges::range_reference_t<Base>>> | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions


## Non-member functions


| cpp/ranges/join_view/iterator/operator_cmp|title=operator==|compares the underlying iterators|notes= | |
| cpp/ranges/join_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/join_view/iterator/iter_swap|swaps the objects pointed to by two underlying iterators|notes= | |

<!--

## Defect reports

-->
