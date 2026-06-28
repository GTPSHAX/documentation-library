---
title: std::tolower(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/tolower
---


# tolowersmall|(std::locale)

ddcl|header=locale|
template< class CharT >
CharT tolower( CharT ch, const locale& loc );
Converts the character `ch` to lowercase if possible, using the conversion rules specified by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns the lowercase form of `ch` if one is listed in the locale, otherwise return `ch` unchanged.

## Notes

Only 1:1 character mapping can be performed by this function, e.g. the Greek uppercase letter 'Σ' has two lowercase forms, depending on the position in a word: 'σ' and 'ς'. A call to `std::tolower` cannot be used to obtain the correct lowercase form in this case.

## Possible implementation

eq fun
|1=
template<class CharT>
CharT tolower(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).tolower(ch);
}

## Example


### Example

```cpp
#include <cwctype>
#include <iostream>
#include <locale>

int main()
{
    wchar_t c = L'\u0190'; // Latin capital open E ('Ɛ')

    std::cout << std::hex << std::showbase;

    std::cout << "in the default locale, tolower(" << (std::wint_t)c << ") = "
              << (std::wint_t)std::tolower(c, std::locale()) << '\n';

    std::cout << "in Unicode locale, tolower(" << (std::wint_t)c << ") = "
              << (std::wint_t)std::tolower(c, std::locale("en_US.utf8")) << '\n';
}
```


**Output:**
```
in the default locale, tolower(0x190) = 0x190
in Unicode locale, tolower(0x190) = 0x25b
```


## See also


| cpp/locale/dsc toupper | (see dedicated page) |
| cpp/string/byte/dsc tolower | (see dedicated page) |
| cpp/string/wide/dsc towlower | (see dedicated page) |

