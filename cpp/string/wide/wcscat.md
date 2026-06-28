---
title: std::wcscat
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcscat
---

ddcl|header=cwchar|
wchar_t* wcscat( wchar_t* dest, const wchar_t* src );
Appends a copy of the wide string pointed to by `src` to the end of the wide string pointed to by `dest`. The wide character `src[0]` replaces the null terminator at the end of `dest`. The resulting wide string is null-terminated.
The behavior is undefined if the destination array is not large enough for the contents of both `src` and `dest` and the terminating null wide character.
The behavior is undefined if the strings overlap.

## Parameters


### Parameters

- `dest` - pointer to the null-terminated wide string to append to
- `src` - pointer to the null-terminated wide string to copy from

## Return value

Returns a copy of `dest`.

## Example


### Example

```cpp
#include <clocale>
#include <cwchar> 
#include <iostream>

int main(void) 
{
    wchar_t str[50] = L"Земля, прощай.";
    std::wcscat(str, L" ");
    std::wcscat(str, L"В добрый путь.");

    std::setlocale(LC_ALL, "en_US.utf8");
    std::wcout.imbue(std::locale("en_US.utf8"));
    std::wcout << str << '\n';
}
```


**Output:**
```
Земля, прощай. В добрый путь.
```


## See also


| cpp/string/wide/dsc wcsncat | (see dedicated page) |
| cpp/string/byte/dsc strcat | (see dedicated page) |
| cpp/string/wide/dsc wcscpy | (see dedicated page) |

