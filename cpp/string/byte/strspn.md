---
title: std::strspn
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strspn
---

ddcl|header=cstring|
size_t strspn( const char* dest, const char* src );
Returns the length of the maximum initial segment (span) of the byte string pointed to by `dest`, that consists of only the characters found in byte string pointed to by `src`.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated byte string to be analyzed
- `src` - pointer to the null-terminated byte string that contains the characters to search for

## Return value

The length of the maximum initial segment that contains only characters from byte string pointed to by `src`.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <string>

const char* low_alpha = "qwertyuiopasdfghjklzxcvbnm";

int main()
{
    std::string s = "abcde312$#@";

    std::size_t spnsz = std::strspn(s.c_str(), low_alpha);
    std::cout << "After skipping initial lowercase letters from '" << s
              << "'\nThe remainder is '" << s.substr(spnsz) << "'\n";
}
```


**Output:**
```
After skipping initial lowercase letters from 'abcde312$#@'
The remainder is '312$#@'
```


## See also


| cpp/string/byte/dsc strcspn | (see dedicated page) |
| cpp/string/wide/dsc wcsspn | (see dedicated page) |
| cpp/string/byte/dsc strpbrk | (see dedicated page) |

