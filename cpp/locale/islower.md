---
title: std::islower(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/islower
---


# islowersmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool islower( CharT ch, const locale& loc );
Checks if the given character is classified as a lowercase alphabetic character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as lowercase, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool islower(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::lower, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t c = L'\u03c0'; // GREEK SMALL LETTER PI

    std::locale loc1("C");
    std::cout << std::boolalpha
              << "islower('π', C locale) returned "
              << std::islower(c, loc1) << '\n'
              << "isupper('π', C locale) returned "
              << std::isupper(c, loc1) << '\n';

    std::locale loc2("en_US.UTF8");
    std::cout << "islower('π', Unicode locale) returned "
              << std::islower(c, loc2) << '\n'
              << "isupper('π', Unicode locale) returned "
              << std::isupper(c, loc2) << '\n';
}
```


**Output:**
```
islower('π', C locale) returned false
isupper('π', C locale) returned false
islower('π', Unicode locale) returned true
isupper('π', Unicode locale) returned false
```


## See also


| cpp/string/byte/dsc islower | (see dedicated page) |
| cpp/string/wide/dsc iswlower | (see dedicated page) |

