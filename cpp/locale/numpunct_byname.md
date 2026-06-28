---
title: std::numpunct_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/numpunct_byname
---

ddcl|header=locale|
template< class CharT >
class numpunct_byname : public std::numpunct<CharT>;
`std::numpunct_byname` is a `std::numpunct` facet which encapsulates numeric punctuation preferences of a locale specified at its construction.

## Specializations

The standard library is guaranteed to provide the following specializations:


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|numpunct_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|numpunct_byname | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const double number = 1000.25;
    std::wcout << L"default locale: " << number << L'\n';
    std::wcout.imbue(std::locale(std::wcout.getloc(),
                                 new std::numpunct_byname<wchar_t>("ru_RU.UTF8")));
    std::wcout << L"default locale with russian numpunct: " << number << L'\n';
}
```


**Output:**
```
default locale: 1000.25
default locale with russian numpunct: 1 000,25
```


## See also


| cpp/locale/dsc numpunct | (see dedicated page) |

