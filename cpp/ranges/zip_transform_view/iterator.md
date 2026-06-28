---
title: std::ranges::zip_transform_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/iterator
---

ddcla|since=c++23|expos=yes|
template< bool Const >
class /*iterator*/;
The iterator type of a possibly const-qualified `zip_transform_view`, returned by `zip_transform_view::begin` and in certain cases by `zip_transform_view::end`.
The type `/*iterator*/<true>` or `/*iterator*/<false>` treats the underlying views as const-qualified or non-const-qualified respectively.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`iterator_category`<br>| | |
| Let `/*POT*/` denote the pack of types | |


```cpp
std::iterator_traits<std::iterator_t<
    /*maybe-const*/<Const, Views>>>::iterator_category...
```

If `/*Base*/` models , then `iterator_category` denotes:

```cpp
std::invoke_result_t</*maybe-const*/<Const, F>&,
    ranges::range_reference_t</*maybe-const*/<Const, Views>>...>
```

: is not a reference.
* Otherwise,
:* `std::random_access_iterator_tag`, if<br />
:: `(std::derived_from</*POT*/, std::random_access_iterator_tag> && ...)` is `true`.<br />
:* Otherwise, `std::bidirectional_iterator_tag`, if<br />
:: `(std::derived_from</*POT*/, std::bidirectional_iterator_tag> && ...)` is `true`.<br />
:* Otherwise, `std::forward_iterator_tag`, if<br />
:: `(std::derived_from</*POT*/, std::forward_iterator_tag> && ...)` is `true`.<br />
:* Otherwise, `std::input_iterator_tag`.
Not present if `/*Base*/` does not model .
dsc|`value_type`|
Let `/*RREF*/` be `ranges::range_reference_t<Views>...`,<br />
and `/*CRREF*/` be `ranges::range_reference_t<const Views>...`. Then:
* `std::remove_cvref_t<std::invoke_result_t<F&, /*RREF*/>>` if `Const` is `false`,
* `std::remove_cvref_t<std::invoke_result_t<const F&, /*CRREF*/>>` otherwise.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|zip_transform_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/zip_transform_view/iterator/operator_cmp|title=operator==<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/zip_transform_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic on underlying iterators|notes= | |


## Example

