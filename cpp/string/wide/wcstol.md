---
title: std::wcstol
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcstol
---


```cpp
**Header:** `<`cwchar`>`
dcl|
long      wcstol ( const wchar_t* str, wchar_t** str_end, int base );
dcl|since=c++11|
long long wcstoll( const wchar_t* str, wchar_t** str_end, int base );
```

Interprets an integer value in a wide string pointed to by `str`.
The functions sets the pointer pointed to by `str_end` to point to the wide character past the last character interpreted. If `str_end` is a null pointer, it is ignored.

## Parameters


### Parameters

- `str` - pointer to the null-terminated wide string to be interpreted
- `str_end` - pointer to a pointer to wide character
- `base` - ''base'' of the interpreted integer value

## Return value

Integer value corresponding to the contents of `str` on success. If the converted value falls out of range of corresponding return type, range error occurs and `LONG_MAX`, `LONG_MIN`, `LLONG_MAX` or `LLONG_MIN` is returned. If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cwchar>
#include <errno.h>
#include <iostream>
#include <string>

int main()
{
    const wchar_t* p = L"10 200000000000000000000000000000 30 -40";
    wchar_t* end;
    std::wcout << "Parsing L'" << p << "':\n";
    for (long i = std::wcstol(p, &end, 10); p != end; i = std::wcstol(p, &end, 10))
    {
        std::wcout << '\'' << std::wstring(p, end-p) << "' -> ";
        p = end;
        if (errno == ERANGE)
        {
            std::wcout << "range error, got ";
            errno = 0;
        }
        std::wcout << i << '\n';
    }
}
```


**Output:**
```
Parsing L'10 200000000000000000000000000000 30 -40':
'10' -> 10
' 200000000000000000000000000000' -> range error, got 9223372036854775807
' 30' -> 30
' -40' -> -40
```


## See also


| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/wide/dsc wcstoul | (see dedicated page) |

