---
title: std::islower
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/islower
---

ddcl|header=cctype|
int islower( int ch );
Checks if the given character is classified as a lowercase character according to the current C locale. In the default `"C"` locale, `std::islower` returns a nonzero value only for the lowercase letters (`abcdefghijklmnopqrstuvwxyz`).
If `islower` returns a nonzero value, it is guaranteed that `std::iscntrl`, `std::isdigit`, `std::ispunct`, and `std::isspace` return zero for the same character in the same C locale.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a lowercase letter, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xe5'; // letter å in ISO-8859-1

    std::cout << "islower(\'\\xe5\', default C locale) returned "
              << std::boolalpha << (bool)std::islower(c) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "islower(\'\\xe5\', ISO-8859-1 locale) returned "
              << std::boolalpha << (bool)std::islower(c) << '\n';

}
```


**Output:**
```
islower('\xe5', default C locale) returned false
islower('\xe5', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc islower | (see dedicated page) |
| cpp/string/wide/dsc iswlower | (see dedicated page) |

