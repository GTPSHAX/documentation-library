---
title: std::collate::do_compare
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/collate/compare
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
int compare( const CharT* low1, const CharT* high1,
const CharT* low2, const CharT* high2 ) const;
dcl|num=2|1=
protected:
virtual int do_compare( const CharT* low1, const CharT* high1,
const CharT* low2, const CharT* high2 ) const;
```

1. Public member function, calls the protected virtual member function `do_compare` of the most derived class.
2. Compares the character sequence [low1, high1) to the character sequence [low2, high2), using this locale's collation rules, and returns `1` if the first string follows the second, `-1` if the first string precedes the second, zero if the two strings are equivalent.

## Parameters


### Parameters

- `low1` - pointer to the first character of the first string
- `high1` - one past the end pointer for the first string
- `low2` - pointer to the first character of the second string
- `high2` - one past the end pointer for the second string

## Return value

`1` if the first string is greater than the second (that is, follows the second in the collation order), `-1` if the first string is less than the second (precedes the second in the collation order), zero if the two strings are equivalent.

## Notes

When three-way comparison is not required (such as when providing a `Compare` argument to standard algorithms such as `std::sort`), `cpp/locale/locale/operator()|std::locale::operator()` may be more appropriate.

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <string>

template<typename CharT>
void try_compare(const std::locale& l, const CharT* p1, const CharT* p2)
{
    auto& f = std::use_facet<std::collate<CharT>>(l);

    std::basic_string<CharT> s1(p1), s2(p2);
    if (f.compare(&s1[0], &s1[0] + s1.size(),
                  &s2[0], &s2[0] + s2.size()) < 0)
        std::wcout << p1 << " before " << p2 << '\n';
    else
        std::wcout << p2 << " before " << p1 << '\n';
}

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    std::wcout.imbue(std::locale());

    std::wcout << "In the American locale: ";
    try_compare(std::locale(), "hrnec", "chrt");
    std::wcout << "In the Czech locale: ";
    try_compare(std::locale("cs_CZ.utf8"), "hrnec", "chrt");

    std::wcout << "In the American locale: ";
    try_compare(std::locale(), L"år", L"ängel");
    std::wcout << "In the Swedish locale: ";
    try_compare(std::locale("sv_SE.utf8"), L"år", L"ängel");
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
| cpp/string/wide/dsc wcscoll | (see dedicated page) |
| cpp/locale/locale/dsc operator() | (see dedicated page) |

