---
title: std::time_get_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get_byname
---

ddcl|header=locale|1=
template<
class CharT,
class InputIt = std::istreambuf_iterator<CharT>
> class time_get_byname : public std::time_get<CharT, InputIt>
`std::time_get_byname` is a `std::time_get` facet which encapsulates time and date parsing rules of the locale specified at its construction.

## Specializations

The standard library is guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of `char` and `wchar_t`, and
* `InputIt` must meet the requirements of *InputIterator*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|time_get_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|time_get_byname | (see dedicated page) |


## Example


## See also


| cpp/locale/dsc time_get | (see dedicated page) |
| cpp/io/manip/dsc get_time | (see dedicated page) |

