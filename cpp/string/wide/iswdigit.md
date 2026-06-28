---
title: std::iswdigit
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswdigit
---

ddcl|header=cwctype|
int iswdigit( wint_t ch );
Checks if the given wide character corresponds (if narrowed) to one of the ten decimal digit characters `0123456789`.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a numeric character, zero otherwise.

## Notes

`std::iswdigit` and `std::iswxdigit` are the only standard wide character classification functions that are not affected by the currently installed C locale.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

void test(wchar_t a3, wchar_t u3, wchar_t j3)
{
    std::wcout << std::boolalpha
               << "\t   '" << a3 << "'   '" << u3 << "'  '" << j3  << "'\n"
               << "iswdigit: "
               << (bool)std::iswdigit(a3) << "  "
               << (bool)std::iswdigit(u3) << " "
               << (bool)std::iswdigit(j3) << '\n'
               << "jdigit:   "
               << (bool)std::iswctype(a3, std::wctype("jdigit")) << ' '
               << (bool)std::iswctype(u3, std::wctype("jdigit")) << ' '
               << (bool)std::iswctype(j3, std::wctype("jdigit")) << '\n';
}

int main()
{
    wchar_t a3 = L'3';  // the ASCII digit 3
    wchar_t u3 = L'三'; // the CJK numeral 3
    wchar_t j3 = L'３'; // the full-width digit 3

    std::setlocale(LC_ALL, "en_US.utf8");
    std::wcout << "In American locale:\n";
    test(a3, u3, j3);

    std::wcout << "\nIn Japanese locale:\n";
    std::setlocale(LC_ALL, "ja_JP.utf8");
    test(a3, u3, j3);
}
```


**Output:**
```
In American locale:
           '3'   '三'  '３'
iswdigit: true  false false
jdigit:   false false false

In Japanese locale:
           '3'   '三'  '３'
iswdigit: true  false false
jdigit:   false false true
```


## See also


| cpp/locale/dsc isdigit | (see dedicated page) |
| cpp/string/byte/dsc isdigit | (see dedicated page) |

