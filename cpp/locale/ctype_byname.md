---
title: std::ctype_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype_byname
---

ddcl|header=locale|
template< class CharT >
class ctype_byname : public std::ctype<CharT>;
`std::ctype_byname` is a `std::ctype` facet which encapsulates character classification rules of the locale specified at its construction.

## Specializations

The standard library is guaranteed to provide the following specializations:


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/byname/dsc constructor|ctype_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|ctype_byname | (see dedicated page) |


## Notes

`std::ctype_byname<char>` was incorrectly declared as an explicit specialization in the synopsis of , and the declaration was removed by the resolution of , but it remains a required specialization, just like `std::ctype_byname<wchar_t>`.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    wchar_t c = L'\u00de'; // capital letter thorn

    std::locale loc("C");

    std::cout << "isupper('Þ', C locale) returned "
              << std::boolalpha << std::isupper(c, loc) << '\n';

    loc = std::locale(loc, new std::ctype_byname<wchar_t>("en_US.utf8"));

    std::cout << "isupper('Þ', C locale with Unicode ctype) returned "
              << std::boolalpha << std::isupper(c, loc) << '\n';
}
```


**Output:**
```
isupper('Þ', C locale) returned false
isupper('Þ', C locale with Unicode ctype) returned true
```


## Defect reports


## See also


| cpp/locale/dsc ctype | (see dedicated page) |
| cpp/locale/dsc ctype_char | (see dedicated page) |

