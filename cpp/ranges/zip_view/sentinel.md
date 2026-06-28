---
title: std::ranges::zip_view::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/sentinel
---

ddcla|since=c++23|expos=yes|
template< bool Const >
class /*sentinel*/;
The return type of `zip_view::end` when the underlying view is not a .
The type `/*sentinel*/<true>` or `/*sentinel*/<false>` treats the underlying view as const-qualified or non-const-qualified respectively.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc expos mem obj|end_|private=yes| | |
| * `std::tuple<ranges::sentinel_t<Views>...>` if `Const` is `false`, or | |
| * `std::tuple<ranges::sentinel_t<const Views>...>` if `Const` is `true`. | |


## Member functions


| cpp/ranges/adaptor/sentinel/dsc constructor|zip_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/adaptor/sentinel/dsc operator cmp|zip_view | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator-|zip_view | (see dedicated page) |

