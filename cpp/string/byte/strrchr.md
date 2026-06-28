---
title: std::strrchr
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strrchr
---


```cpp
**Header:** `<`cstring`>`
dcl|
const char* strrchr( const char* str, int ch );
dcl|1=
char* strrchr(       char* str, int ch );
```

Finds the last occurrence of `ch` (after conversion to `char`) in the byte string pointed to by `str`. The terminating null character is considered to be a part of the string and can be found if searching for `'\0'`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be analyzed
- `ch` - character to search for

## Return value

Pointer to the found character in `str`, or null pointer if no such character is found.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>

int main()
{
    char input[] = "/home/user/hello.c";
    char* output = std::strrchr(input, '/');
    if (output)
        std::cout << output + 1 << '\n';
}
```


**Output:**
```
hello.c
```


## See also


| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/wide/dsc wcsrchr | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |

