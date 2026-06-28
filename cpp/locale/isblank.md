---
title: std::isblank(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isblank
---


# isblanksmall|(std::locale)

ddcl|header=locale|since=c++11|
template< class CharT >
bool isblank( CharT ch, const locale& loc );
Checks if the given character is classified as a blank character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as a blank character, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isblank(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::blank, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

void try_with(wchar_t c, const char* loc)
{
    std::wcout << "isblank('" << c << "', locale(\"" << loc << "\")) returned "
               << std::boolalpha
               << std::isblank(c, std::locale(loc)) << '\n';
}

int main()
{
    const wchar_t IDEO_SPACE = L'\u3000'; // Unicode character 'IDEOGRAPHIC SPACE'
    try_with(IDEO_SPACE, "C");
    try_with(IDEO_SPACE, "en_US.UTF-8");
}
```


**Output:**
```
isblank(' ', locale("C")) returned false
isblank(' ', locale("en_US.UTF-8")) returned true
```


## See also


| cpp/string/byte/dsc isblank | (see dedicated page) |
| cpp/string/wide/dsc iswblank | (see dedicated page) |

