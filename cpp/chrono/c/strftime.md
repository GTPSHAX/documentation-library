---
title: std::strftime
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/c/strftime
---

ddcl|header=ctime|
std::size_t strftime( char* str, std::size_t count, const char* format, const std::tm* tp );
Converts the date and time information from a given calendar time `tp` to a null-terminated multibyte character string `str` according to format string `format`. Up to `count` bytes are written.

## Parameters


### Parameters

- `str` - pointer to the first element of the char array for output
- `count` - maximum number of bytes to write
- `format` - pointer to a null-terminated multibyte character string specifying the format of conversion
- `tp` - pointer to the object containing date and time information to be converted

## Format string


## Return value

The number of bytes written into the character array pointed to by `str` not including the terminating `'\0'` on success. If `count` was reached before the entire string could be stored, `0` is returned and the contents are indeterminate.

## Example


### Example

```cpp
#include <ctime>
#include <iostream>
#include <iterator>
#include <locale>

void utcExample()
{
    // Example of the very popular RFC 3339 format UTC time
    std::time_t time = std::time({});
    char timeString[std::size("yyyy-mm-ddThh:mm:ssZ")];
    std::strftime(std::data(timeString), std::size(timeString),
                  "%FT%TZ", std::gmtime(&time));
    std::cout << timeString << '\n';
}

int main()
{
    std::time_t t = std::time(nullptr);
    char mbstr[100];

    if (std::strftime(mbstr, sizeof(mbstr), "%A %c", std::localtime(&t)))
        std::cout << mbstr << '\n';

    std::locale::global(std::locale("ja_JP.utf8"));
    if (std::strftime(mbstr, sizeof(mbstr), "%A %c", std::localtime(&t)))
        std::cout << mbstr << '\n';

    utcExample();
}
```


**Output:**
```
Tuesday Tue Sep  7 19:40:35 2021
火曜日 2021年09月07日 19時40分35秒
2021-09-07T19:40:35Z
```


## See also


| cpp/chrono/c/dsc asctime | (see dedicated page) |
| cpp/chrono/c/dsc ctime | (see dedicated page) |
| cpp/chrono/c/dsc wcsftime | (see dedicated page) |
| cpp/io/manip/dsc put_time | (see dedicated page) |
| cpp/chrono/dsc formatter|hh_mm_ss | (see dedicated page) |

