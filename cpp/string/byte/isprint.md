---
title: std::isprint
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isprint
---

ddcl|header=cctype|
int isprint( int ch );
Checks if `ch` is a printable character as classified by the currently installed C locale. In the default, `"C"` locale, the following characters are printable:
* digits (`0123456789`)
* uppercase letters (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
* lowercase letters (`abcdefghijklmnopqrstuvwxyz`)
* punctuation characters (`1=!"#$%&'()*+,-./:;<=>?@[\]^_`})
* space (` `)
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character can be printed, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xa0'; // the non-breaking space in ISO-8859-1

    std::cout << "isprint(\'\\xa0\', default C locale) returned "
              << std::boolalpha << (bool)std::isprint(c) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "isprint(\'\\xa0\', ISO-8859-1 locale) returned "
              << std::boolalpha << (bool)std::isprint(c) << '\n';
}
```


**Output:**
```
isprint('\xa0', default C locale) returned false
isprint('\xa0', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc isprint | (see dedicated page) |
| cpp/string/wide/dsc iswprint | (see dedicated page) |

