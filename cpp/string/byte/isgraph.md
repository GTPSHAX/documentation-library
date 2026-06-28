---
title: std::isgraph
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isgraph
---

ddcl|header=cctype|
int isgraph( int ch );
Checks if the given character is graphic (has a graphical representation) as classified by the currently installed C locale. In the default C locale, the following characters are graphic:
* digits (`0123456789`)
* uppercase letters (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
* lowercase letters (`abcdefghijklmnopqrstuvwxyz`)
* punctuation characters (`1=!"#$%&'()*+,-./:;<=>?@[\]^_`})
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character has a graphical representation character, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xb6'; // the character ¶ in ISO-8859-1

    std::cout << "isgraph(\'\\xb6\', default C locale) returned "
              << std::boolalpha << (std::isgraph(c) != 0) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "isgraph(\'\\xb6\', ISO-8859-1 locale) returned "
              << std::boolalpha << (std::isgraph(c) != 0) << '\n';
}
```


**Output:**
```
isgraph('\xb6', default C locale) returned false
isgraph('\xb6', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc isgraph | (see dedicated page) |
| cpp/string/wide/dsc iswgraph | (see dedicated page) |

