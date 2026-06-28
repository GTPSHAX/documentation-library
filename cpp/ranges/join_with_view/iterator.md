---
title: std::ranges::join_with_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/iterator
---


```cpp
dcla|expos=yes|
template< bool Const >
class /*iterator*/
```

`ranges::join_with_view<V, Pattern>::` is the type of the iterators returned by  and  of `ranges::join_with_view<V, Pattern>`.
The state of an iterator of this class is managed as if there are two nested iterators:
* an ''outer iterator'' into the parent range
:* If  models , it is .
:* Otherwise, it is .
* an ''inner iterator''  into the pattern range  or into a child range of the parent range
This iterator class has the invariant that the inner iterator is always dereferenceable unless the outer iterator is not dereferenceable. When an iterator is constructed, incremented or decremented, its outer iterator might be adjusted to hold the invariant.

## Template parameters


### Parameters

- `Const` - whether the iterator is a constant iterator

## Nested types


| Item | Description |
|------|-------------|

#### Exposition-only types

| **Type** | Definition |

#### Iterator property types

| **Type** | Definition |
| dsc|`value_type`| | |
| `std::common_type_t<ranges::range_value_t<``>,`<br> | |
| `ranges::range_value_t<``>>` | |
| dsc|`difference_type`| | |
| `std::common_type_t<ranges::range_difference_t<``>,`<br> | |
| `ranges::range_difference_t<``>,`<br> | |
| `ranges::range_difference_t<``>>` | |


### Determining the iterator concept

`iterator_concept` is defined as follows:
* If all following conditions are satisfied, `iterator_concept` denotes `std::bidirectional_iterator_tag`:
**  is `true`.
**  models .
**  and  each model .
* Otherwise, if all following conditions are satisfied, `iterator_concept` denotes `std::forward_iterator_tag`:
**  is `true`.
**  and  each model .
* Otherwise, `iterator_concept` denotes `std::input_iterator_tag`.

### Determining the iterator category

Given the following types:
* Let `OuterC` be `std::iterator_traits<``>::iterator_category`.
* Let `InnerC` be `std::iterator_traits<``>::iterator_category`.
* Let `PatternC` be `std::iterator_traits<``>::iterator_category`.
`iterator_category` is defined if and only if  is `true`, and  and  each model . In this case, it is defined as follows:
* If  is `false`, `iterator_category` denotes `std::input_iterator_tag`.
* Otherwise, if all following conditions are satisfied, `iterator_category` denotes `std::bidirectional_iterator_tag`:
** `OuterC`, `InnerC`, and `PatternC` each model `std::derived_from<std::bidirectional_iterator_tag>`.
**  and  each model .
* Otherwise, if `OuterC`, `InnerC`, and `PatternC` each model `std::derived_from<std::forward_iterator_tag>`, `iterator_category` denotes `std::forward_iterator_tag`.
* Otherwise, `iterator_category` denotes `std::input_iterator_tag`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|join_with_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/join_with_view/iterator/operator cmp|title=operator==|compares the underlying iterators|notes= | |
| cpp/ranges/join_with_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/join_with_view/iterator/iter_swap|swaps the objects pointed to by two underlying iterators|notes= | |

