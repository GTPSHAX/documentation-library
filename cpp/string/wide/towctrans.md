---
title: std::towctrans
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/towctrans
---

ddcl|header=cwctype|
std::wint_t towctrans( std::wint_t ch, std::wctrans_t desc );
Maps the wide character `ch` using the current C locale's `LC_CTYPE` mapping category identified by `desc`.

## Parameters


### Parameters

- `ch` - the wide character to map
- `desc` - the `LC_CTYPE` mapping, obtained from a call to `std::wctrans`

## Return value

The mapped value of `ch` using the mapping identified by `desc` in `LC_CTYPE` facet of the current C locale.

## Example


### Example

```cpp
#include <algorithm>
#include <clocale>
#include <cwctype>
#include <iostream>

std::wstring tohira(std::wstring str)
{
    std::transform(str.begin(), str.end(), str.begin(), [](wchar_t c)
    {
         return std::towctrans(c, std::wctrans("tojhira"));
    });
    return str;
}

int main()
{
    std::setlocale(LC_ALL, "ja_JP.UTF-8");
    std::wstring kana = L"ヒラガナ";
    std::wcout << "katakana characters " << kana
               << " are " << tohira(kana) << " in hiragana\n";
}
```


**Output:**
```
katakana characters ヒラガナ are ひらがな in hiragana
```


## See also


| cpp/string/wide/dsc wctrans | (see dedicated page) |

