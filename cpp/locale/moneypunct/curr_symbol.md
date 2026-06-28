---
title: std::moneypunct::curr_symbol
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/curr_symbol
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|
public:
string_type curr_symbol() const;
dcl|num=2|
protected:
virtual string_type do_curr_symbol() const;
```

1. Public member function, calls the member function `do_curr_symbol` of the most derived class.
2. Returns the string used as the currency identifier by this locale. If `International` (the second template parameter of `std::moneypunct`) is `false`, the identifier is usually a single (wide) character, such as `"￥"` or `"$"`. If `International` is `true`, the identifier is usually a four-character string holding the three-character [ISO 4217](https://en.wikipedia.org/wiki/ISO 4217) currency code followed by a space (`"JPY "` or `"USD "`).

## Return value

The object of type `string_type` holding the currency symbol or code.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

void show_ccy(const char* locname)
{
    std::locale loc(locname);
    std::cout << locname << " currency symbol is "
              << std::use_facet<std::moneypunct<char, true>>(loc).curr_symbol()
              << "or " << std::use_facet<std::moneypunct<char>>(loc).curr_symbol()
              << " for short\n";
}

int main()
{
    show_ccy("en_US.utf8");
    show_ccy("ja_JP.utf8");
    show_ccy("sv_SE.utf8");
    show_ccy("ru_RU.utf8");
    show_ccy("vi_VN.utf8");
}
```


**Output:**
```
en_US.utf8 currency symbol is USD or $ for short
ja_JP.utf8 currency symbol is JPY or ￥ for short
sv_SE.utf8 currency symbol is SEK or kr for short
ru_RU.utf8 currency symbol is RUB or руб for short
vi_VN.utf8 currency symbol is VND or ₫ for short
```


## Defect reports


## See also


| cpp/locale/moneypunct/dsc do_pos_format | (see dedicated page) |

