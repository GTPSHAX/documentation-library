---
title: std::strcat
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strcat
---

ddcl|header=cstring|
char* strcat( char* dest, const char* src );
Appends a copy of the character string pointed to by `src` to the end of the character string pointed to by `dest`. The character `src[0]` replaces the null terminator at the end of `dest`. The resulting byte string is null-terminated.
The behavior is undefined if the destination array is not large enough for the contents of both `src` and `dest` and the terminating null character.
The behavior is undefined if the strings overlap.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated byte string to append to
- `src` - pointer to the null-terminated byte string to copy from

## Return value

`dest`

## Notes

Because `strcat` needs to seek to the end of `dest` on each call, it is inefficient to concatenate many strings into one using `strcat`.

## Example


### Example

```cpp
#include <cstdio>
#include <cstring>

int main() 
{
    char str[50] = "Hello ";
    char str2[50] = "World!";
    std::strcat(str, str2);
    std::strcat(str, " Goodbye World!");
    std::puts(str);
}
```


**Output:**
```
Hello World! Goodbye World!
```


## See also


| cpp/string/byte/dsc strncat | (see dedicated page) |
| cpp/string/byte/dsc strcpy | (see dedicated page) |

