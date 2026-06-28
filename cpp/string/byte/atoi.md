---
title: std::atoi
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/atoi
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|
int       atoi( const char* str );
dcl|num=2|
long      atol( const char* str );
dcl|num=3|since=c++11|
long long atoll( const char* str );
```

Interprets an integer value in a byte string pointed to by `str`. The implied radix is always 10.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be interpreted

## Return value

Integer value corresponding to the contents of `str` on success.
If no conversion can be performed, `0` is returned.

## Possible implementation

eq fun|1=
template<typename T>
T atoi_impl(const char* str)
{
while (std::isspace(static_cast<unsigned char>(*str)))
++str;
bool negative = false;
if (*str == '+')
++str;
else if (*str == '-')
{
++str;
negative = true;
}
T result = 0;
for (; std::isdigit(static_cast<unsigned char>(*str)); ++str)
{
int digit = *str - '0';
result *= 10;
result -= digit; // calculate in negatives to support INT_MIN, LONG_MIN,..
}
return negative ? result : -result;
}
int atoi(const char* str)
{
return atoi_impl<int>(str);
}
long atol(const char* str)
{
return atoi_impl<long>(str);
}
long long atoll(const char* str)
{
return atoi_impl<long long>(str);
}
Actual C++ library implementations fall back to C library implementations of `atoi`, `atoil`, and `atoll`, which either implement it directly (as in [https://github.com/bminor/musl/blob/master/src/stdlib/atoi.c MUSL libc]) or delegate to `std::strtol|strtol`/`std::strtoll|strtoll` (as in [https://github.com/bminor/glibc/blob/master/stdlib/atoi.c GNU libc]).

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

int main()
{
    const auto data =
    {
        "42",
        "0x2A", // treated as "0" and junk "x2A", not as hexadecimal
        "3.14159",
        "31337 with words",
        "words and 2",
        "-012345",
        "10000000000" // note: out of int32_t range
    };

    for (const char* s : data)
    {
        const int i{std::atoi(s)};
        std::cout << "std::atoi('" << s << "') is " << i << '\n';
        if (const long long ll{std::atoll(s)}; i != ll)
            std::cout << "std::atoll('" << s << "') is " << ll << '\n';
    }
}
```


**Output:**
```
std::atoi('42') is 42
std::atoi('0x2A') is 0
std::atoi('3.14159') is 3
std::atoi('31337 with words') is 31337
std::atoi('words and 2') is 0
std::atoi('-012345') is -12345
std::atoi('10000000000') is 1410065408
std::atoll('10000000000') is 10000000000
```


## See also


| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtoul | (see dedicated page) |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |

