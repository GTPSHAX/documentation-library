---
title: std::tolower
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/tolower
---

ddcl|header=cctype|
int tolower( int ch );
Converts the given character to lowercase according to the character conversion rules defined by the currently installed C locale.
In the default `"C"` locale, the following uppercase letters `ABCDEFGHIJKLMNOPQRSTUVWXYZ` are replaced with respective lowercase letters `abcdefghijklmnopqrstuvwxyz`.

## Parameters


### Parameters

- `ch` - character to be converted. If the value of `ch` is not representable as `unsigned char` and does not equal `EOF`, the behavior is undefined

## Return value

Lowercase version of `ch` or unmodified `ch` if no lowercase version is listed in the current C locale.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xb4'; // the character Ž in ISO-8859-15
                              // but ´ (acute accent) in ISO-8859-1

    std::setlocale(LC_ALL, "en_US.iso88591");
    std::cout << std::hex << std::showbase;
    std::cout << "in iso8859-1, tolower('0xb4') gives " << std::tolower(c) << '\n';
    std::setlocale(LC_ALL, "en_US.iso885915");
    std::cout << "in iso8859-15, tolower('0xb4') gives " << std::tolower(c) << '\n';
}
```


**Output:**
```
in iso8859-1, tolower('0xb4') gives 0xb4
in iso8859-15, tolower('0xb4') gives 0xb8
```


## See also


| cpp/string/byte/dsc toupper | (see dedicated page) |
| cpp/locale/dsc tolower | (see dedicated page) |
| cpp/string/wide/dsc towlower | (see dedicated page) |


## External links

