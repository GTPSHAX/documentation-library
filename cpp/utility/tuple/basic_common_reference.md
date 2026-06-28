---
title: std::basic_common_reference<tuple-like>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/basic_common_reference
---

ddcl|header=tuple|since=c++23|
template< tuple-like TTuple, tuple-like UTuple,
template<class> class TQual, template<class> class UQual >
requires /* see below */
struct basic_common_reference<TTuple, UTuple, TQual, UQual>;
The common reference type of two  types is a `std::tuple` consists of the common reference types of all corresponding element type pairs of both types, where the cv and reference qualifiers on the tuple-like types are applied to their element types.
Given
* `TTypes` as the pack formed by the sequence of `std::tuple_element_t<i, TTuple>` for every integer `i` in [0, std::tuple_size_v<TTuple>), and
* `UTypes` as the pack formed by the sequence of `std::tuple_element_t<i, UTuple>` for every integer `i` in [0, std::tuple_size_v<UTuple>),
the following constraints need to be satisfied:
* `TTuple` or `UTuple` is a `std::tuple` specialization.
* `std::is_same_v<TTuple, std::decay_t<TTuple>>` is `true`.
* `std::is_same_v<UTuple, std::decay_t<UTuple>>` is `true`.
* `std::tuple_size_v<TTuple>` equals `std::tuple_size_v<UTuple>` (`TTuple` and `UTuple` have the same number of elements).
* `std::tuple<std::common_reference_t<TQual<TTypes>..., UQual<UTypes>>...>` denotes a type.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Example

