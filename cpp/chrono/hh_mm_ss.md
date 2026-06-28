---
title: std::chrono::hh_mm_ss
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/hh_mm_ss
---

ddcl|header=chrono|since=c++20|
template< class Duration >
class hh_mm_ss;
The class template `hh_mm_ss` splits a `std::chrono::duration` into a "broken down" time such as ''hours'':''minutes'':''seconds'', with the precision of the split determined by the `Duration` template parameter. It is primarily a formatting tool.
`Duration` must be a specialization of `std::chrono::duration`, otherwise the program is ill-formed.

## Member constants


| dsc mem sconst|nolink=true|constexpr unsigned fractional_width|the smallest possible integer in the range  such that `precision` (see below) will exactly represent the value of }, or `6` if there's no such integer | |


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| dsc|`precision`|box| | |
| `std::chrono::duration<std::common_type_t<Duration::rep, std::chrono::seconds::rep>,` | |
| `                      std::ratio<1, 10``>>` | |


## Member functions


| cpp/chrono/hh_mm_ss/dsc hh_mm_ss | (see dedicated page) |
| cpp/chrono/hh_mm_ss/dsc accessors | (see dedicated page) |
| cpp/chrono/hh_mm_ss/dsc duration | (see dedicated page) |


## Non-member functions


| cpp/chrono/hh_mm_ss/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|hh_mm_ss | (see dedicated page) |

