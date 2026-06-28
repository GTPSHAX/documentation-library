---
title: std::wcsncpy
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcsncpy
---

ddcl|header=cwchar|
wchar_t* wcsncpy( wchar_t* dest, const wchar_t* src, std::size_t count );
Copies at most `count` characters of the wide string pointed to by `src` (including the terminating null wide character) to wide character array pointed to by `dest`.
If `count` is reached before the entire string `src` was copied, the resulting wide character array is not null-terminated.
If, after copying the terminating null wide character from `src`, `count` is not reached, additional null wide characters are written to `dest` until the total of `count` characters have been written.
If the strings overlap, the behavior is undefined.

## Parameters


### Parameters

- `dest` - pointer to the wide character array to copy to
- `src` - pointer to the wide string to copy from
- `count` - maximum number of wide characters to copy

## Return value

`dest`

## Notes

In typical usage, `count` is the size of the destination array.

## Example


### Example

```cpp
#include <cwchar>
#include <iostream>

int main()
{
    const wchar_t src[] = L"hi";
    wchar_t dest[6] = {L'a', L'b', L'c', L'd', L'e', L'f'};

    std::wcsncpy(dest, src, 5); // this will copy 'hi' and repeat \0 three times

    std::wcout << "The contents of dest are: ";
    for (const wchar_t c : dest)
    {
        if (c)
            std::wcout << c << ' ';
        else
            std::wcout << "\\0" << ' ';
    }
    std::wcout << '\n';
}
```


**Output:**
```
The contents of dest are: h i \0 \0 \0 f
```


## See also


| cpp/string/wide/dsc wcscpy | (see dedicated page) |
| cpp/string/wide/dsc wmemcpy | (see dedicated page) |
| cpp/string/byte/dsc strncpy | (see dedicated page) |

