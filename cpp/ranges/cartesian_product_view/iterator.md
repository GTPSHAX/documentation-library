---
title: Vs...>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator
---

ddcla|since=c++23|expos=yes|
template< bool Const >
class /*iterator*/
The return type of `cartesian_product_view::begin`, and of `cartesian_product_view::end` when the underlying view `V` is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::random_access_iterator_tag`, if `/*cartesian-product-is-random-access*/<Const, First, Vs...>` is modeled, | |
| * `std::bidirectional_iterator_tag`, if `/*cartesian-product-is-bidirectional*/<Const, First, Vs...>` is modeled, | |
| * `std::forward_iterator_tag`, if  models , | |
| * `std::input_iterator_tag`, otherwise | |


```cpp
std::tuple<ranges::range_value_t</*maybe-const*/<Const, First>>,
           ranges::range_value_t</*maybe-const*/<Const, Vs>>...>;
```


```cpp
std::tuple<ranges::range_reference_t</*maybe-const*/<Const, First>>,
           ranges::range_reference_t</*maybe-const*/<Const, Vs>>...>;
```


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|current_|private=yes|a tuple of iterators to the current underlying elements|spec=`std::tuple<ranges::iterator_t</*maybe-const*/<Const, First>>,`<br> | |
| `ranges::iterator_t</*maybe-const*/<Const, Vs>>...>`<br> | |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|cartesian_product_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/cartesian_product_view/iterator/operator_cmp|title=operator==<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/cartesian_product_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |
| cpp/ranges/cartesian_product_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/cartesian_product_view/iterator/iter_swap|swaps underlying pointed-to elements|notes= | |


## Example


## See also

