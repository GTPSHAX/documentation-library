---
title: std::money_base
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/money_base
---

ddcl|header=locale|
class money_base;
The class `std::money_base` provides constants which are inherited and used by the `std::moneypunct`, `std::money_get` and `std::money_put` facets.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|}|unscoped enumeration type | |
| dsc|}|the monetary format type | |


| Item | Description |
|------|-------------|
| **Enumeration constant** | Definition |


## Notes

The monetary format is an array of four `char`s convertible to `std::money_base::part`. In that sequence, each of `symbol`, `sign`, and `value` appears exactly once, and either `space` or `none` appears in the remaining position. The value `none`, if present, is not first; the value `space`, if present, is neither first nor last.
The default format, returned by the standard specializations of `std::moneypunct` is }.

## See also


| cpp/locale/dsc moneypunct | (see dedicated page) |
| cpp/locale/dsc money_get | (see dedicated page) |
| cpp/locale/dsc money_put | (see dedicated page) |

