---
title: std::strtol
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strtol
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|
long      strtol( const char* str, char** str_end, int base );
dcl|num=2|since=c++11|
long long strtoll( const char* str, char** str_end, int base );
```

Interprets an integer value in a byte string pointed to by `str`.
The function sets the pointer pointed to by `str_end` to point to the character past the last character interpreted. If `str_end` is a null pointer, it is ignored.
If the `str` is empty or does not have the expected form, no conversion is performed, and (if `str_end` is not a null pointer) the value of `str` is stored in the object pointed to by `str_end`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be interpreted
- `str_end` - pointer to a pointer to character
- `base` - ''base'' of the interpreted integer value

## Return value

* If successful, an integer value corresponding to the contents of `str` is returned.
* If the converted value falls out of range of corresponding return type, a range error occurs (setting `errno` to `ERANGE`) and `LONG_MAX`, `LONG_MIN`, `LLONG_MAX` or `LLONG_MIN` is returned (according to sign of the value and the return type).
* If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cerrno>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>

int main()
{
    const char* p = "10 200000000000000000000000000000 30 -40";
    std::cout << "Parsing " << std::quoted(p) << ":\n";

    for (;;)
    {
        // errno can be set to any non-zero value by a library function call
        // regardless of whether there was an error, so it needs to be cleared
        // in order to check the error set by strtol
        errno = 0;
        char* p_end{};
        const long i = std::strtol(p, &p_end, 10);
        if (p == p_end)
            break;

        const bool range_error = errno == ERANGE;
        const std::string extracted(p, p_end - p);
        p = p_end;

        std::cout << "Extracted " << std::quoted(extracted)
                  << ", strtol returned " << i << '.';
        if (range_error)
            std::cout << "\n  Range error occurred.";

        std::cout << '\n';
    }
}
```


**Output:**
```
Parsing "10 200000000000000000000000000000 30 -40":
Extracted "10", strtol returned 10.
Extracted " 200000000000000000000000000000", strtol returned 9223372036854775807.
  Range error occurred.
Extracted " 30", strtol returned 30.
Extracted " -40", strtol returned -40.
```


## See also


| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/byte/dsc strtoul | (see dedicated page) |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/string/wide/dsc wcstol | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |

