---
title: std::isalpha
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isalpha
---

ddcl|header=cctype|
int isalpha( int ch );
Checks if the given character is an alphabetic character as classified by the currently installed C locale. In the default locale, the following characters are alphabetic:
* uppercase letters `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
* lowercase letters `abcdefghijklmnopqrstuvwxyz`
In locales other than `"C"`, an alphabetic character is a character for which `std::isupper()` or `std::islower()` returns non-zero or any other character considered alphabetic by the locale. In any case, `std::iscntrl()`, `std::isdigit()`, `std::ispunct()` and `std::isspace()` will return zero for this character.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is an alphabetic character, zero otherwise.

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

    std::cout << "isalpha(\'\\xdf\', default C locale) returned "
              << std::boolalpha << !!std::isalpha(c) << '\n';

    std::setlocale(LC_ALL, "de_DE.iso88591");
    std::cout << "isalpha(\'\\xdf\', ISO-8859-1 locale) returned "
              << static_cast<bool>(std::isalpha(c)) << '\n';

}
```


**Output:**
```
isalpha('\xdf', default C locale) returned false
isalpha('\xdf', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc isalpha | (see dedicated page) |
| cpp/string/wide/dsc iswalpha | (see dedicated page) |

