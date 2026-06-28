---
title: std::iscntrl(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/iscntrl
---


# iscntrlsmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool iscntrl( CharT ch, const locale& loc );
Checks if the given character is classified as a control character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as a control character, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool iscntrl(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::cntrl, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t CCH = L'\u0094'; // Destructive Backspace in Unicode

    std::locale loc1("C");
    std::cout << "iscntrl(CCH, C locale) returned "
              << std::boolalpha << std::iscntrl(CCH, loc1) << '\n';

    std::locale loc2("en_US.UTF8");
    std::cout << "iscntrl(CCH, Unicode locale) returned "
              << std::boolalpha << std::iscntrl(CCH, loc2) << '\n';
}
```


**Output:**
```
iscntrl(CCH, C locale) returned false
iscntrl(CCH, Unicode locale) returned true
```


## See also


| cpp/string/byte/dsc iscntrl | (see dedicated page) |
| cpp/string/wide/dsc iswcntrl | (see dedicated page) |

