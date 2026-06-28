---
title: std::wcsncat
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcsncat
---

ddcl|header=cwchar|
wchar_t* wcsncat( wchar_t* dest, const wchar_t* src, std::size_t count );
Appends at most `count` wide characters from the wide string pointed to by `src` to the end of the character string pointed to by `dest`, stopping if the null terminator is copied. The wide character `src[0]` replaces the null terminator at the end of `dest`. The null terminator is always appended in the end (so the maximum number of wide characters the function may write is `count + 1`).
The behavior is undefined if the destination array is not large enough for the contents of both `src` and `dest` and the terminating null wide character.
The behavior is undefined if the strings overlap.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated wide string to append to
- `src` - pointer to the null-terminated wide string to copy from
- `count` - maximum number of wide characters to copy

## Return value

`dest`

## Example


### Example

```cpp
#include <clocale>
#include <cwchar> 
#include <iostream>

int main(void) 
{
    wchar_t str[50] = L"Земля, прощай.";
    std::wcsncat(str, L" ", 1);
    std::wcsncat(str, L"В добрый путь.", 8); // only append the first 8 wide chars

    std::setlocale(LC_ALL, "en_US.utf8");
    std::wcout.imbue(std::locale("en_US.utf8"));
    std::wcout << str << '\n';
}
```


**Output:**
```
Земля, прощай. В добрый
```


## See also


| cpp/string/wide/dsc wcscat | (see dedicated page) |
| cpp/string/byte/dsc strncat | (see dedicated page) |
| cpp/string/wide/dsc wcscpy | (see dedicated page) |

