---
title: std::moneypunct
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct
---

ddcl|header=locale|1=
template< class CharT, bool International = false >
class moneypunct;
The facet `std::moneypunct` encapsulates monetary value format preferences. Stream I/O manipulators `std::get_money` and `std::put_money` use `std::moneypunct` through `std::money_get` and `std::money_put` for parsing monetary value input and formatting monetary value output.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/locale/moneypunct/dsc constructor | (see dedicated page) |
| cpp/locale/moneypunct/dsc decimal_point | (see dedicated page) |
| cpp/locale/moneypunct/dsc thousands_sep | (see dedicated page) |
| cpp/locale/moneypunct/dsc grouping | (see dedicated page) |
| cpp/locale/moneypunct/dsc curr_symbol | (see dedicated page) |
| cpp/locale/moneypunct/dsc positive_sign | (see dedicated page) |
| cpp/locale/moneypunct/dsc frac_digits | (see dedicated page) |
| cpp/locale/moneypunct/dsc pos_format | (see dedicated page) |


## Protected member functions


| cpp/locale/moneypunct/dsc destructor | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_decimal_point | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_thousands_sep | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_grouping | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_curr_symbol | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_positive_sign | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_frac_digits | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_pos_format | (see dedicated page) |


## See also


| cpp/locale/dsc money_base | (see dedicated page) |
| cpp/locale/dsc moneypunct_byname | (see dedicated page) |
| cpp/locale/dsc money_get | (see dedicated page) |
| cpp/locale/dsc money_put | (see dedicated page) |

