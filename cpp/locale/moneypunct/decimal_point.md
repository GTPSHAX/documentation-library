---
title: std::moneypunct::decimal_point
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/decimal_point
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
CharT decimal_point() const;
dcl|num=2|1=
protected:
virtual CharT do_decimal_point() const;
```

1. Public member function, calls the member function `do_decimal_point` of the most derived class.
2. Returns the character to use as the decimal point separator in monetary I/O if the format uses fractions (that is, if `do_frac_digits()` is greater than zero). For typical U.S. locales, it is the character `'.'` (or `L'.'`).

## Return value

The object of type `CharT` holding the decimal point character.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>

void show_dpt(const char* locname)
{
    std::locale loc(locname);
    std::cout.imbue(loc);
    std::cout << locname << " decimal point is '"
              << std::use_facet<std::moneypunct<char>>(loc).decimal_point()
              << "' for example: " << std::showbase << std::put_money(123);
    if (std::use_facet<std::moneypunct<char>>(loc).frac_digits() == 0)
        std::cout << " (does not use frac digits)";

    std::cout << '\n';
}

int main()
{
    show_dpt("en_US.utf8");
    show_dpt("ja_JP.utf8");
    show_dpt("sv_SE.utf8");
    show_dpt("de_DE.utf8");
}
```


**Output:**
```
en_US.utf8 decimal point is '.' for example: $1.23
ja_JP.utf8 decimal point is '.' for example: ￥123 (does not use frac digits)
sv_SE.utf8 decimal point is ',' for example: 1,23 kr
de_DE.utf8 decimal point is ',' for example: 1,23 €
```


## See also


| cpp/locale/moneypunct/dsc do_frac_digits | (see dedicated page) |

