---
title: std::wcscpy
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcscpy
---

ddcl|header=cwchar|
wchar_t* wcscpy( wchar_t* dest, const wchar_t* src );
Copies the wide string pointed to by `src` (including the terminating null wide character) to wide character array pointed to by `dest`.
If the strings overlap, the behavior is undefined.

## Parameters


### Parameters

- `dest` - pointer to the wide character array to copy to
- `src` - pointer to the null-terminated wide string to copy from

## Return value

`dest`

## Example


### Example

```cpp
#include <clocale>
#include <cwchar>
#include <iostream>
#include <memory>

int main()
{
    const wchar_t* src = L"犬 means dog";
//  src[0] = L'狗'; // can't modify string literal
    auto dst = std::make_unique<wchar_t[]>(std::wcslen(src) + 1); // +1 for the null
    std::wcscpy(dst.get(), src);
    dst[0] = L'狗';
    std::setlocale(LC_ALL, "en_US.utf8");
    std::wcout.imbue(std::locale(""));
    std::wcout << src << '\n' << dst.get() << '\n';
}
```


**Output:**
```
犬 means dog
狗 means dog
```


## See also


| cpp/string/wide/dsc wcsncpy | (see dedicated page) |
| cpp/string/wide/dsc wmemcpy | (see dedicated page) |
| cpp/string/byte/dsc strcpy | (see dedicated page) |

