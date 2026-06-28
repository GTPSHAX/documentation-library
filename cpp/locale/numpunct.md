---
title: std::numpunct
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/numpunct
---

ddcl|header=locale|
template< class CharT >
class numpunct;
The facet `std::numpunct` encapsulates numeric punctuation preferences. Stream I/O operations use `std::numpunct` through `std::num_get` and `std::num_put` for parsing numeric input and formatting numeric output.
The numbers that are supported by `std::numpunct` have the format described below. Here `digit` represents the radix set specified by the `fmtflags` argument value, `thousands-sep` and `decimal-point` are the results of `thousands_sep()` and `decimal_point()` functions respectively.
The format of integer values is as follows:

```cpp
lang=text|1=
integer     ::= [sign] units
sign        ::= plusminus
plusminus   ::= '+' {{!
```

units       ::= digits [thousands-sep units]
digits      ::= digit [digits]
The number of digits between the `thousand-sep`s (maximum size of `digits`) is specified by the result of `grouping()`.
The format of floating-point values is as follows:

```cpp
lang=text|1=
floatval    ::= [sign] units [decimal-point [digits]] [e [sign] digits] {{!
```

[sign]        decimal-point  digits   [e [sign] digits]
e           ::= 'e' | 'E'

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/numpunct/dsc numpunct | (see dedicated page) |
| cpp/locale/numpunct/dsc ~numpunct | (see dedicated page) |
| cpp/locale/numpunct/dsc decimal_point | (see dedicated page) |
| cpp/locale/numpunct/dsc thousands_sep | (see dedicated page) |
| cpp/locale/numpunct/dsc grouping | (see dedicated page) |
| cpp/locale/numpunct/dsc truefalsename | (see dedicated page) |


## Protected member functions


| cpp/locale/numpunct/dsc do_decimal_point | (see dedicated page) |
| cpp/locale/numpunct/dsc do_thousands_sep | (see dedicated page) |
| cpp/locale/numpunct/dsc do_grouping | (see dedicated page) |
| cpp/locale/numpunct/dsc do_truefalsename | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <locale>

struct french_bool : std::numpunct<char>
{
    string_type do_truename() const override { return "vrai"; }
    string_type do_falsename() const override { return "faux"; }
};

int main()
{
    std::cout << "default locale: "
              << std::boolalpha << true << ", " << false << '\n';
    std::cout.imbue(std::locale(std::cout.getloc(), new french_bool));
    std::cout << "locale with modified numpunct: "
              << std::boolalpha << true << ", " << false << '\n';
}
```


**Output:**
```
default locale: true, false
locale with modified numpunct: vrai, faux
```


## Defect reports


## See also


| cpp/locale/numpunct_byname|creates a numpunct facet for the named locale | |

