---
title: std::toupper
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/toupper
---

ddcl|header=cctype|
int toupper( int ch );
Converts the given character to uppercase according to the character conversion rules defined by the currently installed C locale.
In the default `"C"` locale, the following lowercase letters `abcdefghijklmnopqrstuvwxyz` are replaced with respective uppercase letters `ABCDEFGHIJKLMNOPQRSTUVWXYZ`.

## Parameters


### Parameters

- `ch` - character to be converted. If the value of `ch` is not representable as `unsigned char` and does not equal `EOF`, the behavior is undefined.

## Return value

Converted character or `ch` if no uppercase version is defined by the current C locale.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <climits>
#include <clocale>
#include <iostream>
#include <ranges>

int main()
{
    for (auto bd{0}; unsigned char lc : std::views::iota(0, UCHAR_MAX))
        if (unsigned char uc = std::toupper(lc); uc != lc)
            std::cout << lc << uc << (13 == ++bd ? '\n' : ' ');
    std::cout << "\n\n";

    unsigned char c = '\xb8'; // the character ž in ISO-8859-15
                              // but ¸ (cedilla) in ISO-8859-1

    std::setlocale(LC_ALL, "en_US.iso88591");
    std::cout << std::hex << std::showbase;
    std::cout << "in iso8859-1, toupper('0xb8') gives " << std::toupper(c) << '\n';
    std::setlocale(LC_ALL, "en_US.iso885915");
    std::cout << "in iso8859-15, toupper('0xb8') gives " << std::toupper(c) << '\n';
}
```


**Output:**
```
aA bB cC dD eE fF gG hH iI jJ kK lL mM
nN oO pP qQ rR sS tT uU vV wW xX yY zZ

in iso8859-1, toupper('0xb8') gives 0xb8
in iso8859-15, toupper('0xb8') gives 0xb4
```


## See also


| cpp/string/byte/dsc tolower | (see dedicated page) |
| cpp/locale/dsc toupper | (see dedicated page) |
| cpp/string/wide/dsc towupper | (see dedicated page) |


## External links

