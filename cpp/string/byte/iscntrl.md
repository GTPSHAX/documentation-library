---
title: std::iscntrl
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/iscntrl
---

ddcl|header=cctype|
int iscntrl( int ch );
Checks if the given character is a control character as classified by the currently installed C locale. In the default, `"C"` locale, the control characters are the characters with the codes `0x00-0x1F` and `0x7F`.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a control character, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\x94'; // the control code CCH in ISO-8859-1

    std::cout << "iscntrl(\'\\x94\', default C locale) returned "
              << std::boolalpha << !!std::iscntrl(c) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "iscntrl(\'\\x94\', ISO-8859-1 locale) returned "
              << !!std::iscntrl(c) << '\n';

}
```


**Output:**
```
iscntrl('\x94', default C locale) returned false
iscntrl('\x94', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc iscntrl | (see dedicated page) |
| cpp/string/wide/dsc iswcntrl | (see dedicated page) |

