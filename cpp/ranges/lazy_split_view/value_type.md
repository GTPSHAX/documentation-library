---
title: std::ranges::lazy_split_view::outer_iterator<Const>::value_type
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/value_type
---

ddcl|since=c++20|
struct value_type : ranges::view_interface<value_type>
The value type of the iterator `ranges::lazy_split_view<V, Pattern>::``<Const>`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Member functions

member|value_type|2=
ddcl|since=c++20|
constexpr explicit value_type(/*outer_iterator*/ i); // exposition only
Initializes  with `std::move(i)`.
member|begin|2=
ddcl|since=c++20|
constexpr /*inner_iterator*/<Const> begin() const;
Equivalent to box|`return /*inner_iterator*/<Const>{`c/core|};.
member|end|2=
ddcl|since=c++20|
constexpr std::default_sentinel_t end() const noexcept;
Returns `std::default_sentinel`.

## Defect reports

