---
title: std::wcschr
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcschr
---


```cpp
**Header:** `<`cwchar`>`
dcl|
const wchar_t* wcschr( const wchar_t* str, wchar_t ch );
dcl|1=
wchar_t* wcschr(       wchar_t* str, wchar_t ch );
```

Finds the first occurrence of the wide character `ch` in the wide string pointed to by `str`.

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
    const wchar_t* cat = std::wcschr(arr, L'猫');
    const wchar_t* dog = std::wcschr(arr, L'犬');

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
The character 猫 found at position 1
The character 犬 not found
```


## See also


| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/wide/dsc wcsrchr | (see dedicated page) |
| cpp/string/wide/dsc wcspbrk | (see dedicated page) |

