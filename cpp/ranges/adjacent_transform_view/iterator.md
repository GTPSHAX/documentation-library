---
title: std::ranges::adjacent_transform_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/iterator
---

ddcl|since=c++23|notes=|
template< bool Const >
class /*iterator*/
The return type of `adjacent_transform_view::begin`, and of `adjacent_transform_view::end` when the underlying view `V` is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`iterator_category`| | |
| * `std::input_iterator_tag`, if | |


```cpp
std::invoke_result_t</*maybe-const*/<Const, F>&,
                     /*REPEAT*/(ranges::range_reference_t<Base>, N)...>
```

: is not a reference. Otherwise,
* let  denote the type `std::iterator_traits<iterator_t<Base>>::iterator_category`.
** `std::random_access_iterator_tag`, if <br>`std::derived_from<C, std::random_access_iterator_tag>` is `true`. Otherwise,
** `std::bidirectional_iterator_tag`, if <br>`std::derived_from<C, std::bidirectional_iterator_tag>` is `true`. Otherwise,
** `std::forward_iterator_tag`, if <br>`std::derived_from<C, std::forward_iterator_tag>` is `true`. Otherwise,
** `std::input_iterator_tag`.
dsc|`value_type`|

```cpp
std::remove_cvref_t<std::invoke_result_t</*maybe-const*/<Const, F>&,
                    /*REPEAT*/(ranges::range_reference_t<Base>, N)...>>;
```


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|adjacent_transform_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/adjacent_transform_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/adjacent_transform_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |


## Example


## See also


| cpp/ranges/zip_transform_view/dsc iterator | (see dedicated page) |

