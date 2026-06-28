---
title: std::ranges::zip_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator
---


```cpp
dcla|anchor=no|expos=yes|
template< bool Const >
class /*iterator*/;
```

The iterator type of a possibly const-qualified `zip_view`, returned by `zip_view::begin` and in certain cases by `zip_view::end`.
The type `/*iterator*/<true>` or `/*iterator*/<false>` treats the underlying views as const-qualified or non-const-qualified respectively.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::random_access_iterator_tag` if  is `true`, otherwise | |
| * `std::bidirectional_iterator_tag` if  is `true`, otherwise | |
| * `std::forward_iterator_tag` if  is `true`, otherwise | |
| * `std::input_iterator_tag`. | |
| dsc|`iterator_category`<br>| | |
| * `std::input_iterator_tag` if  is `true`, | |
| * not defined otherwise. | |
| dsc|`value_type`| | |
| * `std::tuple<ranges::range_value_t<Views>...>` if `Const` is `false`, | |
| * `std::tuple<ranges::range_value_t<const Views>...>` otherwise. | |
| dsc|`difference_type`| | |
| * `std::common_type_t<ranges::range_difference_t<Views>...>` if `Const` is `false`, | |
| * `std::common_type_t<ranges::range_difference_t<const Views>...>` otherwise. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc expos mem obj|current_|private=yes| | |
| * `std::tuple<ranges::iterator_t<Views>...>` if `Const` is `false`, or | |
| * `std::tuple<ranges::iterator_t<const Views>...>` otherwise. | |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|zip_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/zip_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/zip_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic on underlying iterators|notes= | |
| cpp/ranges/zip_view/iterator/iter_move|obtains a tuple-like value that denotes underlying pointed-to elements to be moved|notes= | |
| cpp/ranges/zip_view/iterator/iter_swap|swaps underlying pointed-to elements|notes= | |


## Example

