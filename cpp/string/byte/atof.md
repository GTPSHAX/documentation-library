---
title: std::atof
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/atof
---

ddcl|header=cstdlib|
double atof( const char* str );
Interprets a floating point value in a byte string pointed to by `str`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be interpreted

## Return value

`double` value corresponding to the contents of `str` on success. If the converted value falls out of range of the return type, the return value is undefined. If no conversion can be performed, `0.0` is returned.

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

int main()
{
    std::cout << std::atof("0.0000000123") << '\n'
              << std::atof("0.012") << '\n'
              << std::atof("15e16") << '\n'
              << std::atof("-0x1afp-2") << '\n'
              << std::atof("inF") << '\n'
              << std::atof("Nan") << '\n'
              << std::atof("invalid") << '\n';
}
```


**Output:**
```
1.23e-08
0.012
1.5e+17
-107.75
inf
nan
0
```


## See also


| cpp/string/basic_string/dsc stof | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |

