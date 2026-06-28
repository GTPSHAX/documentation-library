---
title: std::wcsrchr
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcsrchr
---


```cpp
**Header:** `<`cwchar`>`
dcl|
const wchar_t* wcsrchr( const wchar_t* str, wchar_t ch );
dcl|1=
wchar_t* wcsrchr(       wchar_t* str, wchar_t ch );
```

Finds the last occurrence of the wide character `ch` in the wide string pointed to by `str`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated wide string to be analyzed
- `ch` - wide character to search for

## Return value

Pointer to the found character in `str`, or a null pointer if no such character is found.

## Example


### Example

```cpp
#include <cwchar>
#include <iostream>
#include <locale>

int main()
{
    const wchar_t arr[] = L"白猫 黒猫 кошки";
    const wchar_t* cat = std::wcsrchr(arr, L'猫');
    const wchar_t* dog = std::wcsrchr(arr, L'犬');

    std::cout.imbue(std::locale("en_US.utf8"));

    if (cat)
        std::cout << "The character 猫 found at position " << cat - arr << '\n';
    else
        std::cout << "The character 猫 not found\n";

    if (dog)
        std::cout << "The character 犬 found at position " << dog - arr << '\n';
    else
        std::cout << "The character 犬 not found\n";
}
```


**Output:**
```
The character 猫 found at position 4
The character 犬 not found
```


## See also


| cpp/string/wide/dsc wcschr | (see dedicated page) |
| cpp/string/byte/dsc strrchr | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |

