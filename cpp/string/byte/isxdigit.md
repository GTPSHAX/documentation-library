---
title: std::isxdigit
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isxdigit
---

ddcl|header=cctype|
int isxdigit( int ch );
Checks if the given character is a hexadecimal numeric character (`0123456789ABCDEFabcdef`).
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a hexadecimal numeric character, zero otherwise.

## Notes

`std::isdigit` and `std::isxdigit` are the only standard narrow character classification functions that are not affected by the currently installed C locale. although some implementations (e.g. Microsoft in 1252 codepage) may classify additional single-byte characters as digits.

## Example


### Example

```cpp
#include <cctype>
#include <climits>
#include <iostream>

int main()
{
    for (int c = 0; UCHAR_MAX >= c; ++c)
        if (isxdigit(c))
            std::cout << static_cast<char>(c);
    std::cout << '\n';
}
```


**Output:**
```
0123456789ABCDEFabcdef
```


## See also


| cpp/locale/dsc isxdigit | (see dedicated page) |
| cpp/string/wide/dsc iswxdigit | (see dedicated page) |

