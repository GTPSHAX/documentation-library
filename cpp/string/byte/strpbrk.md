---
title: std::strpbrk
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strpbrk
---


```cpp
**Header:** `<`cstring`>`
dcl|
const char* strpbrk( const char* dest, const char* breakset );
dcl|
char* strpbrk(       char* dest, const char* breakset );
```

Scans the null-terminated byte string pointed to by `dest` for any character from the null-terminated byte string pointed to by `breakset`, and returns a pointer to that character.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated byte string to be analyzed
- `breakset` - pointer to the null-terminated byte string that contains the characters to search for

## Return value

Pointer to the first character in `dest`, that is also in `breakset`, or null pointer if no such character exists.

## Notes

The name stands for "string pointer break", because it returns a pointer to the first of the separator ("break") characters.

## Example


### Example

```cpp
#include <cstring>
#include <iomanip>
#include <iostream>

int main()
{
    const char* str = "hello world, friend of mine!";
    const char* sep = " ,!";

    unsigned int cnt = 0;
    do
    {
        str = std::strpbrk(str, sep); // find separator
        std::cout << std::quoted(str) << '\n';
        if (str)
            str += std::strspn(str, sep); // skip separator
        ++cnt; // increment word count
    } while (str && *str);

    std::cout << "There are " << cnt << " words\n";
}
```


**Output:**
```
" world, friend of mine!"
", friend of mine!"
" of mine!"
" mine!"
"!"
There are 5 words
```


## See also


| cpp/string/byte/dsc strcspn | (see dedicated page) |
| cpp/string/byte/dsc strtok | (see dedicated page) |
| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/wide/dsc wcspbrk | (see dedicated page) |

