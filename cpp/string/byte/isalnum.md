---
title: std::isalnum
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isalnum
---

ddcl|header=cctype|
int isalnum( int ch );
Checks if the given character is an alphanumeric character as classified by the current C locale. In the default locale, the following characters are alphanumeric:
* digits (`0123456789`)
* uppercase letters (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
* lowercase letters (`abcdefghijklmnopqrstuvwxyz`)
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is an alphanumeric character, `0` otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xdf'; // German letter ß in ISO-8859-1

    std::cout << "isalnum(\'\\xdf\', default C locale) returned "
              << std::boolalpha << static_cast<bool>(std::isalnum(c)) << '\n';

    if (std::setlocale(LC_ALL, "de_DE.iso88591"))
        std::cout << "isalnum(\'\\xdf\', ISO-8859-1 locale) returned "
                  << static_cast<bool>(std::isalnum(c)) << '\n';

}
```


**Output:**
```
isalnum('\xdf', default C locale) returned false
isalnum('\xdf', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc isalnum | (see dedicated page) |
| cpp/string/wide/dsc iswalnum | (see dedicated page) |

de:cpp/string/byte/isalnum
es:cpp/string/byte/isalnum
fr:cpp/string/byte/isalnum
it:cpp/string/byte/isalnum
ja:cpp/string/byte/isalnum
pt:cpp/string/byte/isalnum
ru:cpp/string/byte/isalnum
zh:cpp/string/byte/isalnum
