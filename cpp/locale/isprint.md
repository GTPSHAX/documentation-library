---
title: std::isprint(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isprint
---


# isprintsmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isprint( CharT ch, const locale& loc );
Checks if the given character is classified as a printable character (including space) by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as printable, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isprint(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::print, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t c = L'\u2122'; // trademark sign

    std::locale loc1("C");
    std::cout << "isprint('™', C locale) returned "
              << std::boolalpha << std::isprint(c, loc1) << '\n';

    std::locale loc2("en_US.UTF-8");
    std::cout << "isprint('™', Unicode locale) returned "
              << std::boolalpha << std::isprint(c, loc2) << '\n';
}
```


**Output:**
```
isprint('™', C locale) returned false
isprint('™', Unicode locale) returned true
```


## See also


| cpp/string/byte/dsc isprint | (see dedicated page) |
| cpp/string/wide/dsc iswprint | (see dedicated page) |

