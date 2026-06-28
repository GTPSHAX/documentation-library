---
title: std::strchr
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strchr
---


```cpp
**Header:** `<`cstring`>`
dcl|
const char* strchr( const char* str, int ch );
dcl|
char* strchr(       char* str, int ch );
```

Finds the first occurrence of the character `static_cast<char>(ch)` in the byte string pointed to by `str`.
The terminating null character is considered to be a part of the string and can be found if searching for `'\0'`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be analyzed
- `ch` - character to search for

## Return value

Pointer to the found character in `str`, or a null pointer if no such character is found.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>

int main()
{
    const char* str = "Try not. Do, or do not. There is no try.";
    char target = 'T';
    const char* result = str;

    while ((result = std::strchr(result, target)) != nullptr)
    {
        std::cout << "Found '" << target
                  << "' starting at '" << result << "'\n";

        // Increment result, otherwise we'll find target at the same location
        ++result;
    }
}
```


**Output:**
```
Found 'T' starting at 'Try not. Do, or do not. There is no try.'
Found 'T' starting at 'There is no try.'
```


## See also


| cpp/string/byte/dsc memchr | (see dedicated page) |
| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/wide/dsc wcschr | (see dedicated page) |
| cpp/string/byte/dsc strrchr | (see dedicated page) |
| cpp/string/byte/dsc strpbrk | (see dedicated page) |

