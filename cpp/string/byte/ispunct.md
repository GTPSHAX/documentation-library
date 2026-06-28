---
title: std::ispunct
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/ispunct
---

ddcl|header=cctype|
int ispunct( int ch );
Checks if the given character is a punctuation character as classified by the current C locale. The default C locale classifies the characters (`1=!"#$%&'()*+,-./:;<=>?@[\]^_`}) as punctuation.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a punctuation character, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <clocale>
#include <iostream>

int main()
{
    unsigned char c = '\xd7'; // the character × (multiplication sign) in ISO-8859-1

    std::cout << "ispunct(\'\\xd7\', default C locale) returned "
              << std::boolalpha << (bool)std::ispunct(c) << '\n';

    std::setlocale(LC_ALL, "en_GB.iso88591");
    std::cout << "ispunct(\'\\xd7\', ISO-8859-1 locale) returned "
              << std::boolalpha << (bool)std::ispunct(c) << '\n';
}
```


**Output:**
```
ispunct('\xd7', default C locale) returned false
ispunct('\xd7', ISO-8859-1 locale) returned true
```


## See also


| cpp/locale/dsc ispunct | (see dedicated page) |
| cpp/string/wide/dsc iswpunct | (see dedicated page) |

