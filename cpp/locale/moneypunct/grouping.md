---
title: std::moneypunct::grouping
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/grouping
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
std::string grouping() const;
dcl|num=2|1=
protected:
virtual std::string do_grouping() const;
```

1. Public member function, calls the member function `do_grouping` of the most derived class.
2. Returns the pattern that determines the grouping of the digits in the monetary output, with the same exact meaning as `std::numpunct::do_grouping`.

## Return value

The object of type `std::string` holding the groups. The standard specializations of `std::moneypunct` return an empty string, indicating no grouping. Typical groupings (e.g. the `en_US` locale) return `"\003"`.

## Example


## See also


| cpp/locale/moneypunct/dsc do_thousands_sep | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_decimal_point | (see dedicated page) |

