---
title: std::iswxdigit
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswxdigit
---

ddcl|header=cwctype|
int iswxdigit( wint_t ch );
Checks if the given wide character corresponds (if narrowed) to a hexadecimal numeric character, i.e. one of `0123456789abcdefABCDEF`.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a hexadecimal numeric character, zero otherwise.

## Notes

`std::iswdigit` and `std::iswxdigit` are the only standard wide character classification functions that are not affected by the currently installed C locale.

## Example


### Example

```cpp
#include <cwctype>
#include <iostream>

int main()
{
    std::cout << std::boolalpha
              << (std::iswxdigit(L'a') != 0) << ' '
              << (std::iswxdigit(L'ä') != 0) << '\n';
}
```


**Output:**
```
true false
```


## See also


| cpp/locale/dsc isxdigit | (see dedicated page) |
| cpp/string/byte/dsc isxdigit | (see dedicated page) |

