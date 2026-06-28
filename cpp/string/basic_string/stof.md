---
title: std::stod
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/stof
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|1=
float       stof ( const std::string& str, std::size_t* pos = nullptr );
dcl|num=2|since=c++11|1=
float       stof ( const std::wstring& str, std::size_t* pos = nullptr );
dcl|num=3|since=c++11|1=
double      stod ( const std::string& str, std::size_t* pos = nullptr );
dcl|num=4|since=c++11|1=
double      stod ( const std::wstring& str, std::size_t* pos = nullptr );
dcl|num=5|since=c++11|1=
long double stold( const std::string& str, std::size_t* pos = nullptr );
dcl|num=6|since=c++11|1=
long double stold( const std::wstring& str, std::size_t* pos = nullptr );
```

Interprets a floating point value in a string `str`.
Let `ptr` be an internal (to the conversion functions) pointer of type `char*`  or `wchar_t*` , accordingly.
1. Calls `std::strtof(str.c_str(), &ptr)`.
2. Calls `std::wcstof(str.c_str(), &ptr)`.
3. Calls `std::strtod(str.c_str(), &ptr)`.
4. Calls `std::wcstod(str.c_str(), &ptr)`.
5. Calls `std::strtold(str.c_str(), &ptr)`.
6. Calls `std::wcstold(str.c_str(), &ptr)`.
If `pos` is not a null pointer, then `ptr` will receive the address of the first unconverted character in `str.c_str()`, and the index of that character will be calculated and stored in `*pos`, giving the number of characters that were processed by the conversion.

## Parameters


### Parameters

- `str` - the string to convert
- `pos` - address of an integer to store the number of characters processed

## Return value

The string converted to the specified floating point type.

## Exceptions

`std::invalid_argument` if no conversion could be performed.
`std::out_of_range` if the converted value would fall out of the range of the result type or if the underlying function (`std::strtof`, `std::strtod` or `std::strtold`) sets `errno` to `ERANGE`.

## Example


## See also


| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |

