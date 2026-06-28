---
title: std::wcstod
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcstof
---


```cpp
**Header:** `<`cwchar`>`
dcl|since=c++11|
float       wcstof( const wchar_t* str, wchar_t** str_end );
dcl|
double      wcstod( const wchar_t* str, wchar_t** str_end );
dcl|since=c++11|
long double wcstold( const wchar_t* str, wchar_t** str_end );
```

Interprets a floating point value in a wide string pointed to by `str`.
The functions sets the pointer pointed to by `str_end` to point to the wide character past the last character interpreted. If `str_end` is a null pointer, it is ignored.

## Parameters


### Parameters

- `str` - pointer to the null-terminated wide string to be interpreted
- `str_end` - pointer to a pointer to a wide character

## Return value

Floating point value corresponding to the contents of `str` on success. If the converted value falls out of range of corresponding return type, range error occurs and `HUGE_VAL`, `HUGE_VALF` or `HUGE_VALL` is returned. If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cerrno>
#include <clocale>
#include <cwchar>
#include <iostream>
#include <string>

int main()
{
    const wchar_t* p = L"111.11 -2.22 0X1.BC70A3D70A3D7P+6 -Inf 1.18973e+4932zzz";
    wchar_t* end;
    std::wcout << "Parsing L\"" << p << "\":\n";
    for (double f = std::wcstod(p, &end); p != end; f = std::wcstod(p, &end))
    {
        std::wcout << "  '" << std::wstring(p, end-p) << "' -> ";
        p = end;
        if (errno == ERANGE)
        {
            std::wcout << "range error, got ";
            errno = 0;
        }
        std::wcout << f << '\n';
    }

    if (std::setlocale(LC_NUMERIC, "de_DE.utf8"))
    {
        std::wcout << L"With de_DE.utf8 locale:\n";
        std::wcout << L"  '123.45' -> " << std::wcstod(L"123.45", 0) << L'\n';
        std::wcout << L"  '123,45' -> " << std::wcstod(L"123,45", 0) << L'\n';
    }
}
```


**Output:**
```
Parsing L"111.11 -2.22 0X1.BC70A3D70A3D7P+6 -Inf 1.18973e+4932zzz":
  '111.11' -> 111.11
  ' -2.22' -> -2.22
  ' 0X1.BC70A3D70A3D7P+6' -> 111.11
  ' -Inf' -> -inf
  ' 1.18973e+4932' -> range error, got inf
With de_DE.utf8 locale:
  '123.45' -> 123
  '123,45' -> 123.45
```


## See also


| cpp/string/byte/dsc strtof | (see dedicated page) |

