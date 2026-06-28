---
title: std::messages_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/messages_byname
---

ddcl|header=locale|
template< class CharT >
class messages_byname : public std::messages<CharT>;
`std::messages_byname` is a `std::messages` facet which encapsulates retrieval of strings from message catalogs of the locale specified at its construction.

## Specializations

The standard library is guaranteed to provide the following specializations:


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|messages_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|messages_byname | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <locale>

void try_with(const std::locale& loc)
{
    const std::messages<char>& facet = std::use_facet<std::messages<char>>(loc);

    std::messages<char>::catalog cat = facet.open("sed", std::cout.getloc());
    if (cat < 0)
        std::cout << "Could not open \"sed\" message catalog\n";
    else
        std::cout << "\"No match\" "
                  << facet.get(cat, 0, 0, "No match") << '\n'
                  << "\"Memory exhausted\" " 
                  << facet.get(cat, 0, 0, "Memory exhausted") << '\n';

    facet.close(cat);
}

int main()
{
    std::locale loc("en_US.utf8");
    std::cout.imbue(loc);

    try_with(std::locale(loc, new std::messages_byname<char>("de_DE.utf8")));
    try_with(std::locale(loc, new std::messages_byname<char>("fr_FR.utf8")));
    try_with(std::locale(loc, new std::messages_byname<char>("ja_JP.utf8")));
}
```


**Output:**
```
"No match" Keine Übereinstimmung
"Memory exhausted" Speicher erschöpft
"No match" Pas de concordance
"Memory exhausted" Mémoire épuisée
"No match" 照合しません
"Memory exhausted" メモリーが足りません
```


## See also


| cpp/locale/dsc messages | (see dedicated page) |

