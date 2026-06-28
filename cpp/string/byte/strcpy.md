---
title: std::strcpy
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strcpy
---

ddcl|header=cstring|
char* strcpy( char* dest, const char* src );
Copies the character string pointed to by `src`, including the null terminator, to the character array whose first element is pointed to by `dest`.
The behavior is undefined if the `dest` array is not large enough. The behavior is undefined if the strings overlap.

## Parameters


### Parameters

- `dest` - pointer to the character array to write to
- `src` - pointer to the null-terminated byte string to copy from

## Return value

`dest`

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <memory>

int main()
{
    const char* src = "Take the test.";
//  src[0] = 'M'; // can't modify string literal
    auto dst = std::make_unique<char[]>(std::strlen(src) + 1); // +1 for null terminator
    std::strcpy(dst.get(), src);
    dst[0] = 'M';
    std::cout << src << '\n' << dst.get() << '\n';
}
```


**Output:**
```
Take the test.
Make the test.
```


## See also


| cpp/string/byte/dsc strncpy | (see dedicated page) |
| cpp/string/byte/dsc memcpy | (see dedicated page) |

de:cpp/string/byte/strcpy
es:cpp/string/byte/strcpy
fr:cpp/string/byte/strcpy
it:cpp/string/byte/strcpy
ja:cpp/string/byte/strcpy
pt:cpp/string/byte/strcpy
ru:cpp/string/byte/strcpy
tr:cpp/string/byte/strcpy
zh:cpp/string/byte/strcpy
