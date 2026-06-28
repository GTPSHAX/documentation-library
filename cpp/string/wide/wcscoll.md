---
title: std::wcscoll
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcscoll
---

ddcl|header=cwchar|
int wcscoll( const wchar_t* lhs, const wchar_t* rhs );
Compares two null-terminated wide strings according to the locale most recently installed by `std::setlocale`, as defined by the `LC_COLLATE` category.

## Parameters


### Parameters

- `lhs, rhs` - pointers to the null-terminated wide strings to compare

## Return value

Negative value if `lhs` is ''less than'' (precedes) `rhs`.
`0` if `lhs` is ''equal to'' `rhs`.
Positive value if `lhs` is ''greater than'' (follows) `rhs`.

## Notes


## Example


### Example

```cpp
#include <clocale>
#include <iostream>

void try_compare(const wchar_t* p1, const wchar_t* p2)
{
    if (std::wcscoll(p1, p2) < 0)
        std::wcout << p1 << " before " << p2 << '\n';
    else
        std::wcout << p2 << " before " << p1 << '\n';
}

int main()
{
    std::setlocale(LC_ALL, "en_US.utf8");
    std::wcout << "In the American locale: ";
    try_compare(L"hrnec", L"chrt");

    std::setlocale(LC_COLLATE, "cs_CZ.utf8");
    std::wcout << "In the Czech locale: ";
    try_compare(L"hrnec", L"chrt");

    std::setlocale(LC_COLLATE, "en_US.utf8");
    std::wcout << "In the American locale: ";
    try_compare(L"år", L"ängel");

    std::setlocale(LC_COLLATE, "sv_SE.utf8");
    std::wcout << "In the Swedish locale: ";
    try_compare(L"år", L"ängel");
}
```


**Output:**
```
In the American locale: chrt before hrnec
In the Czech locale: hrnec before chrt
In the American locale: ängel before år
In the Swedish locale: år before ängel
```


## See also


| cpp/string/byte/dsc strcoll | (see dedicated page) |
| cpp/locale/collate/dsc do_compare | (see dedicated page) |
| cpp/string/wide/dsc wcsxfrm | (see dedicated page) |

