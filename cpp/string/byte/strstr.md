---
title: std::strstr
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strstr
---


```cpp
**Header:** `<`cstring`>`
dcl|
const char* strstr( const char* haystack, const char* needle );
dcl|1=
char* strstr(       char* haystack, const char* needle );
```

Finds the first occurrence of the byte string `needle` in the byte string pointed to by `haystack`. The terminating null characters are not compared.

## Parameters


### Parameters

- `haystack` - pointer to the null-terminated byte string to examine
- `needle` - pointer to the null-terminated byte string to search for

## Return value

Pointer to the first character of the found substring in `haystack`, or a null pointer if no such character is found. If `needle` points to an empty string, `haystack` is returned.

## Example


### Example

```cpp
#include <cstring>
#include <iomanip>
#include <iostream>

int main()
{
    const char* str = "Try not. Do, or do not. There is no try.";
    const char* target = "not";

    for (const char* result = str; (result = std::strstr(result, target)); ++result)
        std::cout << "Found " << std::quoted(target)
                  << " starting at (" << result - str << "): "
                  << std::quoted(result) << '\n';
}
```


**Output:**
```
Found "not" starting at (4): "not. Do, or do not. There is no try."
Found "not" starting at (19): "not. There is no try."
```


## See also


| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/wide/dsc wcsstr | (see dedicated page) |
| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/byte/dsc strrchr | (see dedicated page) |

