---
title: std::stoul
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/stoul
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|1=
unsigned long      stoul ( const std::string& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=2|since=c++11|1=
unsigned long      stoul ( const std::wstring& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=3|since=c++11|1=
unsigned long long stoull( const std::string& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=4|since=c++11|1=
unsigned long long stoull( const std::wstring& str,
std::size_t* pos = nullptr, int base = 10 );
```

Interprets an unsigned integer value in the string `str`.
Let `ptr` be an internal (to the conversion functions) pointer of type `char*`  or `wchar_t*` , accordingly.
1. Calls `std::strtoul(str.c_str(), &ptr, base)`.
2. Calls `std::wcstoul(str.c_str(), &ptr, base)`.
3. Calls `std::strtoull(str.c_str(), &ptr, base)`.
4. Calls `std::wcstoull(str.c_str(), &ptr, base)`.
If `pos` is not a null pointer, then `ptr` will receive the address of the first unconverted character in `str.c_str()`, and the index of that character will be calculated and stored in `*pos`, giving the number of characters that were processed by the conversion.

## Parameters


### Parameters

- `str` - the string to convert
- `pos` - address of an integer to store the number of characters processed
- `base` - the number base

## Return value

The string converted to the specified unsigned integer type.

## Exceptions

* `std::invalid_argument` if no conversion could be performed.
* `std::out_of_range` if the converted value would fall out of the range of the result type or if the underlying function (`std::strtoul` or `std::strtoull`) sets `errno` to `ERANGE`.

## Example


## See also


| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stof | (see dedicated page) |

