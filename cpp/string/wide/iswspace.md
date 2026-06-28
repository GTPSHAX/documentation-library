---
title: std::iswspace
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswspace
---

ddcl|header=cwctype|
int iswspace( wint_t ch );
Checks if the given wide character is a wide whitespace character as classified by the currently installed C locale. In the default locale, the whitespace characters are the following:
* Space (`0x20`, `' '`)
* Form feed (`0x0c`, `'\f'`)
* Line feed (`0x0a`, `'\n'`)
* Carriage return (`0x0d`, `'\r'`)
* Horizontal tab (`0x09`, `'\t'`)
* Vertical tab (`0x0b`, `'\v'`).

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a whitespace character, zero otherwise.

## Notes

ISO 30112 defines POSIX space characters as Unicode characters U+0009..U+000D, U+0020, U+1680, U+180E, U+2000..U+2006, U+2008..U+200A, U+2028, U+2029, U+205F, and U+3000.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

void try_with(wchar_t c, const char* loc)
{
    std::setlocale(LC_ALL, loc);
    std::wcout << "isspace('" << c << "') in " << loc << " locale returned "
               << std::boolalpha << static_cast<bool>(std::iswspace(c)) << '\n';
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
isspace(' ') in C locale returned false
isspace(' ') in en_US.UTF8 locale returned true
```


## See also


| cpp/locale/dsc isspace | (see dedicated page) |
| cpp/string/byte/dsc isspace | (see dedicated page) |

