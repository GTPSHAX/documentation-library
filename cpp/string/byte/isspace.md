---
title: std::isspace
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isspace
---

ddcl|header=cctype|
int isspace( int ch );
Checks if the given character is whitespace character as classified by the currently installed C locale. In the default locale, the whitespace characters are the following:
* space (`0x20`, `' '`)
* form feed (`0x0c`, `'\f'`)
* line feed (`0x0a`, `'\n'`)
* carriage return (`0x0d`, `'\r'`)
* horizontal tab (`0x09`, `'\t'`)
* vertical tab (`0x0b`, `'\v'`)
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a whitespace character, zero otherwise.

## Notes


## Example


### Example

```cpp
#include <cctype>
#include <climits>
#include <iomanip>
#include <iostream>

int main(void)
{
    std::cout << std::hex << std::setfill('0') << std::uppercase;
    for (int ch{}; ch <= UCHAR_MAX; ++ch)
        if (std::isspace(ch))
            std::cout << std::setw(2) << ch << ' ';
    std::cout << '\n';
}
```


**Output:**
```
09 0A 0B 0C 0D 20
```


## See also


| cpp/locale/dsc isspace | (see dedicated page) |
| cpp/string/wide/dsc iswspace | (see dedicated page) |

