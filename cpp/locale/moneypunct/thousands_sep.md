---
title: std::moneypunct::thousands_sep
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/thousands_sep
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
char_type thousands_sep() const;
dcl|num=2|1=
protected:
virtual char_type do_thousands_sep() const;
```

1. Public member function, calls the member function `do_thousands_sep` of the most derived class.
2. Returns the character to be used as the separator between digit groups when parsing or formatting the integral parts of monetary values.

## Return value

The object of type `char_type` to use as the thousands separator. In common U.S. locales, this is `','` or `L','`.

## Example


## See also


| cpp/locale/moneypunct/dsc do_grouping | (see dedicated page) |

