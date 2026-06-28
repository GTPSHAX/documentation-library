---
title: std::strtoul
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strtoul
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|
unsigned long      strtoul ( const char* str, char** str_end, int base );
dcl|since=c++11|num=2|
unsigned long long strtoull( const char* str, char** str_end, int base );
```

Interprets an unsigned integer value in a byte string pointed to by `str`.
The functions sets the pointer pointed to by `str_end` to point to the character past the last character interpreted. If `str_end` is a null pointer, it is ignored.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be interpreted
- `str_end` - pointer to a pointer to character, might be set to a position past the last character interpreted
- `base` - ''base'' of the interpreted integer value

## Return value

Integer value corresponding to the contents of `str` on success. If the converted value falls out of range of corresponding return type, range error occurs (`errno` is set to `ERANGE`) and `ULONG_MAX` or `ULLONG_MAX` is returned. If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cstdlib>
#include <errno.h>
#include <iostream>
#include <string>

int main()
{
    const char* p = "10 200000000000000000000000000000 30 -40 - 42";
    char* end = nullptr;
    std::cout << "Parsing '" << p << "':\n";
    for (unsigned long i = std::strtoul(p, &end, 10);
        p != end;
        i = std::strtoul(p, &end, 10))
    {
        std::cout << "'" << std::string(p, end - p) << "' -> ";
        p = end;
        if (errno == ERANGE)
        {
            errno = 0;
            std::cout << "range error, got ";
        }
        std::cout << i << '\n';
    }
    std::cout << "After the loop p points to '" << p << "'\n";
}
```


**Output:**
```
Parsing '10 200000000000000000000000000000 30 -40 - 42':
'10' -> 10
' 200000000000000000000000000000' -> range error, got 18446744073709551615
' 30' -> 30
' -40' -> 18446744073709551576
After the loop p points to ' - 42'
```


## See also


| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/string/wide/dsc wcstoul | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |

