---
title: std::ctype
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/ctype
---

ddcl|header=locale|
template< class CharT >
class ctype;
Class `ctype` encapsulates character classification features. All stream input operations performed through `std::basic_istream<CharT>` use the `std::ctype<CharT>` of the locale imbued in the stream to identify whitespace characters for input tokenization. Stream output operations apply `std::ctype<CharT>::widen()` to narrow-character arguments prior to output.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/ctype/dsc is | (see dedicated page) |
| cpp/locale/ctype/dsc scan_is | (see dedicated page) |
| cpp/locale/ctype/dsc scan_not | (see dedicated page) |
| cpp/locale/ctype/dsc toupper | (see dedicated page) |
| cpp/locale/ctype/dsc tolower | (see dedicated page) |
| cpp/locale/ctype/dsc widen | (see dedicated page) |
| cpp/locale/ctype/dsc narrow | (see dedicated page) |


## Protected member functions


| cpp/locale/ctype/dsc do_is | (see dedicated page) |
| cpp/locale/ctype/dsc do_scan_is | (see dedicated page) |
| cpp/locale/ctype/dsc do_scan_not | (see dedicated page) |
| cpp/locale/ctype/dsc do_toupper | (see dedicated page) |
| cpp/locale/ctype/dsc do_tolower | (see dedicated page) |
| cpp/locale/ctype/dsc do_widen | (see dedicated page) |
| cpp/locale/ctype/dsc do_narrow | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <sstream>

struct csv_whitespace : std::ctype<wchar_t>
{
    bool do_is(mask m, char_type c) const
    {
        if ((m & space) && c == L' ')
            return false; // space will NOT be classified as whitespace

        if ((m & space) && c == L',')
            return true; // comma will be classified as whitespace

        return ctype::do_is(m, c); // leave the rest to the base class
    }
};

int main()
{
    std::wstring in = L"Column 1,Column 2,Column 3\n123,456,789";
    std::wstring token;

    std::wcout << "default locale:\n";
    std::wistringstream s1(in);
    while (s1 >> token)
        std::wcout << "  " << token << '\n';

    std::wcout << "locale with modified ctype:\n";
    std::wistringstream s2(in);
    csv_whitespace* my_ws = new csv_whitespace;
    s2.imbue(std::locale(s2.getloc(), my_ws));
    while (s2 >> token)
        std::wcout << "  " << token << '\n';
}
```


**Output:**
```
default locale:
  Column
  1,Column
  2,Column
  3
  123,456,789
locale with modified ctype:
  Column 1
  Column 2
  Column 3
  123
  456
  789
```


## See also


| cpp/locale/dsc ctype_char | (see dedicated page) |
| cpp/locale/dsc ctype_base | (see dedicated page) |
| cpp/locale/dsc ctype_byname | (see dedicated page) |

