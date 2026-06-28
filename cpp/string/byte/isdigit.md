---
title: std::isdigit
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isdigit
---

ddcl|header=cctype|
int isdigit( int ch );
Checks if the given character is one of the 10 decimal digits: (`0123456789`).
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a numeric character, zero otherwise.

## Notes

`isdigit` and `isxdigit` are the only standard narrow character classification functions that are not affected by the currently installed C locale. although some implementations (e.g. Microsoft in [Windows-1252|1252 codepage](https://en.wikipedia.org/wiki/Windows-1252|1252 codepage)) may classify additional single-byte characters as digits.

## Example


### Example

```cpp
#include <cctype>
#include <climits>
#include <iostream>

int main(void)
{
    for (int i = 0; i <= UCHAR_MAX; ++i)
        if (std::isdigit(i))
            std::cout << static_cast<unsigned char>(i);
    std::cout << '\n';
}
```


**Output:**
```
0123456789
```


## See also


| cpp/locale/dsc isdigit | (see dedicated page) |
| cpp/string/wide/dsc iswdigit | (see dedicated page) |

