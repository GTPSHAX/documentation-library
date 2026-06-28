---
title: std::ranges::join_view::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/sentinel
---

ddcl|since=c++20|notes=|
template< bool Const >
class /*sentinel*/
The return type of `join_view::end` when either of the underlying ranges (`V` or `ranges::range_reference_t<V>`) is not a , or when the parent `join_view` is not a .
If `V` is not a simple view, `Const` is `true` for sentinels returned from the const overloads, and `false` otherwise. If `V` is a simple view, `Const` is `true`.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions


| cpp/ranges/adaptor/sentinel/dsc constructor|join_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/adaptor/sentinel/dsc operator cmp|join_view | (see dedicated page) |

