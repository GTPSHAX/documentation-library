---
title: std::wcstoimax
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcstoimax
---


```cpp
**Header:** `<`cinttypes`>`
dcl|since=c++11|
std::intmax_t wcstoimax( const wchar_t* nptr, wchar_t** endptr, int base );
dcl|since=c++11|
std::uintmax_t wcstoumax( const wchar_t* nptr, wchar_t** endptr, int base );
```

Interprets an unsigned integer value in a wide string pointed to by `nptr`.
The functions sets the pointer pointed to by `endptr` to point to the wide character past the last character interpreted. If `endptr` is a null pointer, it is ignored.

## Parameters


### Parameters

- `nptr` - pointer to the null-terminated wide string to be interpreted
- `endptr` - pointer to a pointer to a wide character
- `base` - ''base'' of the interpreted integer value

## Return value

Integer value corresponding to the contents of `str` on success. If the converted value falls out of range of corresponding return type, range error occurs and `INTMAX_MAX`, `INTMAX_MIN`, `UINTMAX_MAX`, or `0` is returned, as appropriate. If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cinttypes>
#include <iostream>
#include <string>

int main()
{
    std::wstring str = L"helloworld";
    std::intmax_t val = std::wcstoimax(str.c_str(), nullptr, 36);
    std::wcout << str << " in base 36 is " << val << " in base 10\n";

    wchar_t* nptr;
    val = std::wcstoimax(str.c_str(), &nptr, 30);
    if (nptr != &str[0] + str.size())
        std::wcout << str << " in base 30 is invalid."
                   << " The first invalid digit is " << *nptr << '\n';
}
```


**Output:**
```
helloworld in base 36 is 1767707668033969 in base 10
helloworld in base 30 is invalid. The first invalid digit is w
```


## See also


| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/string/wide/dsc wcstol | (see dedicated page) |
| cpp/string/wide/dsc wcstoul | (see dedicated page) |

