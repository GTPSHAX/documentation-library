---
title: std::isxdigit(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isxdigit
---


# isxdigitsmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isxdigit( CharT ch, const locale& loc );
Checks if the given character is classified as a hexadecimal digit by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as a hexadecimal digit, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isxdigit(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::xdigit, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <string>
#include <unordered_set>

struct gxdigit_ctype : std::ctype<wchar_t>
{
    std::unordered_set<wchar_t> greek_digits{L'α', L'β', L'γ', L'δ', L'ε', L'ζ'};

    bool do_is(mask m, char_type c) const override
    {
        return (m & xdigit) && greek_digits.contains(c)
            ? true // 6 first Greek small letters will be classified as digits
            : ctype::do_is(m, c); // leave the rest to the parent class
    }
};

int main()
{
    std::wstring text = L"0123456789abcdefABCDEFαβγδεζηθικλμ";
    std::locale loc(std::locale(""), new gxdigit_ctype);

    std::locale::global(std::locale("en_US.utf8"));
    std::wcout.imbue(std::locale());

    std::wcout << "Hexadecimal digits in text: ";
    for (const wchar_t c : text)
        if (std::isxdigit(c, loc))
            std::wcout << c << L' ';
    std::wcout << L'\n';

    std::wcout << "Not hexadecimal digits in text: ";
    for (const wchar_t c : text)
        if (not std::isxdigit(c, loc))
            std::wcout << c << L' ';
    std::wcout << L'\n';
}
```


**Output:**
```
Hexadecimal digits in text: 0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F α β γ δ ε ζ
Not hexadecimal digits in text: η θ ι κ λ μ
```


## See also


| cpp/string/byte/dsc isxdigit | (see dedicated page) |
| cpp/string/wide/dsc iswxdigit | (see dedicated page) |

