---
title: std::stoi
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/stol
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|1=
int       stoi ( const std::string& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=2|since=c++11|1=
int       stoi ( const std::wstring& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=3|since=c++11|1=
long      stol ( const std::string& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=4|since=c++11|1=
long      stol ( const std::wstring& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=5|since=c++11|1=
long long stoll( const std::string& str,
std::size_t* pos = nullptr, int base = 10 );
dcl|num=6|since=c++11|1=
long long stoll( const std::wstring& str,
std::size_t* pos = nullptr, int base = 10 );
```

Interprets a signed integer value in the string `str`.
Let `ptr` be an internal (to the conversion functions) pointer of type `char*`  or `wchar_t*` , accordingly.
1. Calls `std::strtol(str.c_str(), &ptr, base)`.
2. Calls `std::wcstol(str.c_str(), &ptr, base)`.
3. Calls `std::strtol(str.c_str(), &ptr, base)`.
4. Calls `std::wcstol(str.c_str(), &ptr, base)`.
5. Calls `std::strtoll(str.c_str(), &ptr, base)`.
6. Calls `std::wcstoll(str.c_str(), &ptr, base)`.
If `pos` is not a null pointer, then `ptr` will receive an address of the first unconverted character in `str.c_str()`, and the index of that character will be calculated and stored in `*pos`, giving the number of characters that were processed by the conversion.

## Parameters


### Parameters

- `str` - the string to convert
- `pos` - address of an integer to store the number of characters processed
- `base` - the number base

## Return value

Integer value corresponding to the content of `str`.

## Exceptions

* `std::invalid_argument` if no conversion could be performed.
* `std::out_of_range` if the converted value would fall out of the range of the result type or if the underlying function (`std::strtol` or `std::strtoll`) sets `errno` to `ERANGE`.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

int main()
{
    const auto data =
    {
        "45",
        "+45",
        " -45",
        "3.14159",
        "31337 with words",
        "words and 2",
        "12345678901",
    };

    for (const std::string s : data)
    {
        std::size_t pos{};
        try
        {
            std::cout << "std::stoi(" << std::quoted(s) << "): ";
            const int i{std::stoi(s, &pos)};
            std::cout << i << "; pos: " << pos << '\n';
        }
        catch (std::invalid_argument const& ex)
        {
            std::cout << "std::invalid_argument::what(): " << ex.what() << '\n';
        }
        catch (std::out_of_range const& ex)
        {
            std::cout << "std::out_of_range::what(): " << ex.what() << '\n';
            const long long ll{std::stoll(s, &pos)};
            std::cout << "std::stoll(" << std::quoted(s) << "): " << ll
                      << "; pos: " << pos << '\n';
        }
    }

    std::cout << "\nCalling with different radixes:\n";
    for (const auto& [s, base] : {std::pair<const char*, int>
        {"11",  2}, {"22",  3}, {"33",  4}, {"77",  8},
        {"99", 10}, {"FF", 16}, {"jJ", 20}, {"Zz", 36}<!---->})
    {
        const int i{std::stoi(s, nullptr, base)};
        std::cout << "std::stoi(" << std::quoted(s)
                  << ", nullptr, " << base << "): " << i << '\n';
    }
}
```


**Output:**
```
std::stoi("45"): 45; pos: 2
std::stoi("+45"): 45; pos: 3
std::stoi(" -45"): -45; pos: 4
std::stoi("3.14159"): 3; pos: 1
std::stoi("31337 with words"): 31337; pos: 5
std::stoi("words and 2"): std::invalid_argument::what(): stoi
std::stoi("12345678901"): std::out_of_range::what(): stoi
std::stoll("12345678901"): 12345678901; pos: 11

Calling with different radixes:
std::stoi("11", nullptr, 2): 3
std::stoi("22", nullptr, 3): 8
std::stoi("33", nullptr, 4): 15
std::stoi("77", nullptr, 8): 63
std::stoi("99", nullptr, 10): 99
std::stoi("FF", nullptr, 16): 255
std::stoi("jJ", nullptr, 20): 399
std::stoi("Zz", nullptr, 36): 1295
```


## Defect reports


## See also


| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/basic_string/dsc stof | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtoul | (see dedicated page) |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |

