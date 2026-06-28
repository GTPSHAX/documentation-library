---
title: std::moneypunct_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct_byname
---

ddcl|header=locale|1=
template< class CharT, bool Intl = false >
class moneypunct_byname : public std::moneypunct<CharT, Intl>;
`std::moneypunct_byname` is a `std::moneypunct` facet which encapsulates monetary formatting preferences of a locale specified at its construction.

## Specializations

The standard library is guaranteed to provide every specialization that satisfies the following type requirements:
* `CharT` is one of `char` and `wchar_t`, and
* `Intl` is a possible specialization on a `bool` parameter.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|moneypunct_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|moneypunct_byname | (see dedicated page) |


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>

int main()
{
    long double mon = 1234567;
    std::locale::global(std::locale("en_US.utf8"));
    std::wcout.imbue(std::locale());
    std::wcout << L"american locale: " << std::showbase
               << std::put_money(mon) << '\n';
    std::wcout.imbue(std::locale(std::wcout.getloc(),
                                 new std::moneypunct_byname<wchar_t>("ru_RU.utf8")));
    std::wcout << L"american locale with russian moneypunct: "
               << std::put_money(mon) << '\n';
}
```


**Output:**
```
american locale: $12,345.67
american locale with russian moneypunct: 12 345.67 руб
```


## See also


| cpp/locale/dsc moneypunct | (see dedicated page) |

