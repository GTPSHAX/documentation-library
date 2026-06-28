---
title: std::strncat
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strncat
---

ddcl|header=cstring|
char* strncat( char* dest, const char* src, std::size_t count );
Appends a byte string pointed to by `src` to a byte string pointed to by `dest`. At most `count` characters are copied. The resulting byte string is null-terminated.
The destination byte string must have enough space for the contents of both `dest` and `src` plus the terminating null character, except that the size of `src` is limited to `count`.
The behavior is undefined if the strings overlap.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated byte string to append to
- `src` - pointer to the null-terminated byte string to copy from
- `count` - maximum number of characters to copy

## Return value

`dest`

## Notes

Because `std::strncat` needs to seek to the end of `dest` on each call, it is inefficient to concatenate many strings into one using `std::strncat`.

## Example


### Example

```cpp
#include <cstdio>
#include <cstring>

int main() 
{
    char str[50] = "Hello ";
    const char str2[50] = "World!";
    std::strcat(str, str2);
    std::strncat(str, " Goodbye World!", 3); // may issue "truncated output" warning
    std::puts(str);
}
```


**Output:**
```
Hello World! Go
```


## See also


| cpp/string/byte/dsc strcat | (see dedicated page) |
| cpp/string/byte/dsc strcpy | (see dedicated page) |

