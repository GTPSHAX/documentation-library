---
title: std::collate
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/collate
---

ddcl|header=locale|
template< class CharT >
class collate;
Class `std::collate` encapsulates locale-specific collation (comparison) and hashing of strings. This facet is used by `std::basic_regex` and can be applied, by means of , directly to all standard algorithms that expect a string comparison predicate.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/collate/dsc compare | (see dedicated page) |
| cpp/locale/collate/dsc transform | (see dedicated page) |
| cpp/locale/collate/dsc hash | (see dedicated page) |


## Protected member functions


| cpp/locale/collate/dsc do_compare | (see dedicated page) |
| cpp/locale/collate/dsc do_transform | (see dedicated page) |
| cpp/locale/collate/dsc do_hash | (see dedicated page) |


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <locale>
#include <string>
#include <vector>

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    std::wcout.imbue(std::locale(""));
    std::vector<std::wstring> v
    {
        L"ar", L"zebra", L"\u00f6grupp", L"Zebra",
        L"\u00e4ngel",L"\u00e5r", L"f\u00f6rnamn"
    };

    std::wcout << "Default locale collation order: ";
    std::sort(v.begin(), v.end());
    for (auto s : v)
        std::wcout << s << ' ';
    std::wcout << '\n';

    std::wcout << "English locale collation order: ";
    std::sort(v.begin(), v.end(), std::locale("en_US.UTF-8"));
    for (auto s : v)
        std::wcout << s << ' ';
    std::wcout << '\n';

    std::wcout << "Swedish locale collation order: ";
    std::sort(v.begin(), v.end(), std::locale("sv_SE.UTF-8"));
    for (auto s : v)
        std::wcout << s << ' ';
    std::wcout << '\n';
}
```


**Output:**
```
Default locale collation order: Zebra ar förnamn zebra ängel år ögrupp
English locale collation order: ängel ar år förnamn ögrupp zebra Zebra
Swedish locale collation order: ar förnamn zebra Zebra år ängel ögrupp
```


## See also


| cpp/locale/locale/dsc operator() | (see dedicated page) |
| cpp/locale/dsc collate_byname | (see dedicated page) |

