---
title: std::strtoimax
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strtoimax
---


```cpp
**Header:** `<`cinttypes`>`
dcl|since=c++11|num=1|
std::intmax_t strtoimax( const char* nptr, char** endptr, int base );
dcl|since=c++11|num=2|
std::uintmax_t strtoumax( const char* nptr, char** endptr, int base );
```

Interprets an integer value in a byte string pointed to by `nptr`.
The functions sets the pointer pointed to by `endptr` to point to the character past the last character interpreted. If `endptr` is a null pointer, it is ignored.
If the `nptr` is empty or does not have the expected form, no conversion is performed, and (if `enptr` is not a null pointer) the value of `nptr` is stored in the object pointed to by `endptr`.

## Parameters


### Parameters

- `nptr` - pointer to the null-terminated byte string to be interpreted
- `endptr` - pointer to a pointer to character.
- `base` - ''base'' of the interpreted integer value

## Return value

* If successful, an integer value corresponding to the contents of `str` is returned.
* If the converted value falls out of range of corresponding return type, a range error occurs (setting `errno` to `ERANGE`) and `INTMAX_MAX`, `INTMAX_MIN`, `UINTMAX_MAX` or `0` is returned, as appropriate.
* If no conversion can be performed, `0` is returned.

## Example


### Example

```cpp
#include <cinttypes>
#include <iostream>
#include <string>

int main()
{
    std::string str = "helloworld";
    std::intmax_t val = std::strtoimax(str.c_str(), nullptr, 36);
    std::cout << str << " in base 36 is " << val << " in base 10\n";

    char* nptr;
    val = std::strtoimax(str.c_str(), &nptr, 30);
    if (nptr != &str[0] + str.size())
        std::cout << str << " in base 30 is invalid."
                  << " The first invalid digit is '" << *nptr << "'\n";
}
```


**Output:**
```
helloworld in base 36 is 1767707668033969 in base 10
helloworld in base 30 is invalid. The first invalid digit is 'w'
```


## See also


| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtoul | (see dedicated page) |
| cpp/string/wide/dsc wcstoimax | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |

