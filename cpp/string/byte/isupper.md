---
title: std::isupper
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isupper
---

ddcl|header=cctype|
int isupper( int ch );
Checks if the given character is an uppercase character as classified by the currently installed C locale. In the default `"C"` locale, `std::isupper` returns a nonzero value only for the uppercase letters (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`).
If `std::isupper` returns a nonzero value, it is guaranteed that `std::iscntrl`, `std::isdigit`, `std::ispunct`, and `std::isspace` return zero for the same character in the same C locale.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is an uppercase letter, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xc6'; // letter Æ in ISO-8859-1

    std::cout << "isupper(\'\\xc6\', default C locale) returned "
              << std::boolalpha << (bool)std::isupper(c) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "isupper(\'\\xc6\', ISO-8859-1 locale) returned "
              << std::boolalpha << (bool)std::isupper(c) << '\n';

}
```


**Output:**
```
isupper('\xc6', default C locale) returned false
isupper('\xc6', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc isupper | (see dedicated page) |
| cpp/string/wide/dsc iswupper | (see dedicated page) |

