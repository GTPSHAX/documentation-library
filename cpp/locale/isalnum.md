---
title: std::isalnum(std::locale)
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/isalnum
---


# isalnumsmall|(std::locale)

ddcl|header=locale|
template< class CharT >
bool isalnum( CharT ch, const locale& loc );
Checks if the given character is classified as an alphanumeric character by the given locale's `std::ctype` facet.

## Parameters


### Parameters

- `ch` - character
- `loc` - locale

## Return value

Returns `true` if the character is classified as alphanumeric, `false` otherwise.

## Possible implementation

eq fun
|1=
template<class CharT>
bool isalnum(CharT ch, const std::locale& loc)
{
return std::use_facet<std::ctype<CharT>>(loc).is(std::ctype_base::alnum, ch);
}

## Example


### Example

```cpp
#include <iostream>
#include <locale>

int main()
{
    const wchar_t c = L'\u2135'; // mathematical symbol aleph

    std::locale loc1("C");
    std::cout << "isalnum('ℵ', C locale) returned "
              << std::boolalpha << std::isalnum(c, loc1) << '\n';

    std::locale loc2("en_US.UTF-8");
    std::cout << "isalnum('ℵ', Unicode locale) returned "
              << std::boolalpha << std::isalnum(c, loc2) << '\n';
}
```


**Output:**
```
isalnum('ℵ', C locale) returned false
isalnum('ℵ', Unicode locale) returned true
```


## See also


| cpp/string/byte/dsc isalnum | (see dedicated page) |
| cpp/string/wide/dsc iswalnum | (see dedicated page) |

