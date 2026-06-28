---
title: std::codecvt_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_byname
---

ddcl|header=locale|
template< class InternT, class ExternT, class State >
class codecvt_byname : public std::codecvt<InternT, ExternT, State>;
`std::codecvt_byname` is a `std::codecvt` facet which encapsulates multibyte/wide character conversion rules of a locale specified at its construction.

## Specializations

The standard library is guaranteed to provide the following specializations:


| locale | |


## Member functions


| cpp/locale/byname/dsc constructor|codecvt_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|codecvt_byname | (see dedicated page) |


## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <locale>
#include <string>

int main()
{
    // GB18030 narrow multibyte encoding
    std::ofstream("text.txt") << "\x7a"              // letter 'z', U+007a
                                 "\x81\x30\x89\x38"  // letter 'ß', U+00df
                                 "\xcb\xae"          // CJK ideogram '水' (water), U+6c34
                                 "\x94\x32\xbc\x35"; // musical sign '𝄋' (segno), U+1d10b

    std::wifstream fin("text.txt");
    fin.imbue(std::locale(fin.getloc(),
              new std::codecvt_byname<wchar_t, char, std::mbstate_t>("zh_CN.gb18030")));

    for (wchar_t c; fin.get(c);)
        std::cout << std::hex << std::showbase << static_cast<unsigned>(c) << '\n';
}
```


**Output:**
```
0x7a
0xdf
0x6c34
0x1d10b
```


## Defect reports


## See also


| cpp/locale/dsc codecvt | (see dedicated page) |

