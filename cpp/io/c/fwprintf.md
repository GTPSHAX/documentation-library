---
title: std::wprintf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fwprintf
---


```cpp
**Header:** `<`cwchar`>`
dcl|num=1|
int wprintf( const wchar_t* format, ... );
dcl|num=2|
int fwprintf( std::FILE* stream, const wchar_t* format, ... );
dcl|num=3|
int swprintf( wchar_t* buffer, std::size_t size, const wchar_t* format, ... );
```

Loads the data from the given locations, converts them to wide string equivalents and writes the results to a variety of sinks.
1. Writes the results to `stdout`.
2. Writes the results to a file stream `stream`.
3. Writes the results to a wide string `buffer`. At most `size - 1` wide characters are written followed by null wide character.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `buffer` - pointer to a wide character string to write to
- `size` - up to `size - 1` characters may be written, plus the null terminator
- `format` - pointer to a null-terminated wide string specifying how to interpret the data
- `...` - arguments specifying data to print. If any argument after default conversions is not the type expected by the corresponding conversion specifier, or if there are fewer arguments than required by `format`, the behavior is undefined. If there are more arguments than required by `format`, the extraneous arguments are evaluated and ignored

## Return value

@1,2@ Number of wide characters written if successful or negative value if an error occurred.
3. Number of wide characters written (not counting the terminating null wide character) if successful or negative value if an encoding error occurred or if the number of characters to be generated was equal or greater than `size` (including when `size` is zero).

## Notes

While narrow strings provide `std::snprintf`, which makes it possible to determine the required output buffer size, there is no equivalent for wide strings, and in order to determine the buffer size, the program may need to call `std::swprintf`, check the result value, and reallocate a larger buffer, trying again until successful.

## Example


### Example

```cpp
#include <clocale>
#include <cwchar>
#include <iostream>
#include <locale>

int main()
{
    char narrow_str[] = "z\u00df\u6c34\U0001f34c";
                  // or "zß水🍌";
                  // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9f\x8d\x8c";
    wchar_t warr[29]; // the expected string is 28 characters plus 1 null terminator
    std::setlocale(LC_ALL, "en_US.utf8");

    std::swprintf(warr, sizeof warr/sizeof *warr,
                  L"Converted from UTF-8: '%s'", narrow_str);

    std::wcout.imbue(std::locale("en_US.utf8"));
    std::wcout << warr << '\n';
}
```


**Output:**
```
Converted from UTF-8: 'zß水🍌'
```


## See also


| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/c/dsc vfwprintf | (see dedicated page) |
| cpp/io/c/dsc fputws | (see dedicated page) |

