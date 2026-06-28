---
title: std::isalpha(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isalpha
---


# isalphasmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isalpha( CharT ch, const locale& loc );
Checks if the given character is classified as an alphabetic character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as alphabetic, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isalpha(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::alpha, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t c = L'\u042f'; // cyrillic capital letter ya

    std::locale loc1("C");
    std::cout << "isalpha('Я', C locale) returned "
              << std::boolalpha << std::isalpha(c, loc1) << '\n';

    std::locale loc2("en_US.UTF8");
    std::cout << "isalpha('Я', Unicode locale) returned "
              << std::boolalpha << std::isalpha(c, loc2) << '\n';
}
```


**Output:**
```
isalpha('Я', C locale) returned false
isalpha('Я', Unicode locale) returned true
```


## See also


| cpp/string/byte/dsc isalpha | (see dedicated page) |
| cpp/string/wide/dsc iswalpha | (see dedicated page) |

