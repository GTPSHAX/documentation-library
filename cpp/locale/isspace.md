---
title: std::isspace(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isspace
---


# isspacesmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isspace( CharT ch, const locale& loc );
Checks if the given character is classified as a whitespace character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as a whitespace character, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isspace(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::space, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

void try_with(wchar_t c, const char* loc)
{
    std::wcout << "isspace('" << c << "', locale(\"" << loc << "\")) returned "
               << std::boolalpha << std::isspace(c, std::locale(loc)) << '\n';
}

int main()
{
    const wchar_t EM_SPACE = L'\u2003'; // Unicode character 'EM SPACE'
    try_with(EM_SPACE, "C");
    try_with(EM_SPACE, "en_US.UTF8");
}
```


**Output:**
```
isspace(' ', locale("C")) returned false
isspace(' ', locale("en_US.UTF8")) returned true
```


## See also


| cpp/string/byte/dsc isspace | (see dedicated page) |
| cpp/string/wide/dsc iswspace | (see dedicated page) |

