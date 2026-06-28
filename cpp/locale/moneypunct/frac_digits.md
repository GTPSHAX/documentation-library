---
title: std::moneypunct::frac_digits
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/frac_digits
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
int frac_digits() const;
dcl|num=2|1=
protected:
virtual int do_frac_digits() const;
```

1. Public member function, calls the member function `do_frac_digits` of the most derived class.
2. Returns the number of digits to be displayed after the decimal point when printing monetary values.

## Return value

The number of digits to be displayed after the decimal point. In common U.S. locales, this is the value `2`.

## Example


## See also


| cpp/locale/moneypunct/dsc do_thousands_sep | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_decimal_point | (see dedicated page) |

