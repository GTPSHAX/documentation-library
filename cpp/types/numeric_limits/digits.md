---
title: std::numeric_limits::digits
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/digits
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const int digits;
|dcl2=
static constexpr int digits;
```

The value of `std::numeric_limits<T>::digits` is the number of digits in base-`radix` that can be represented by the type `T` without change. For integer types, this is the number of bits not counting the sign bit and the padding bits (if any). For floating-point types, this is the digits of the mantissa (for `IEC 559/IEEE 754` implementations, this is the number of digits stored for the mantissa plus one, because the mantissa has an implicit leading 1 and binary point).

## Standard specializations


| Item | Description |
|------|-------------|
| **{{tt** | T |


```cpp
CHAR_BIT * sizeof(wchar_t)
    - std::numeric_limits<wchar_t>::is_signed
```


## Example


### Example

```cpp
#include <concepts>
#include <iomanip>
#include <iostream>
#include <limits>
#include <meta>
#include <string_view>
#include <type_traits>
using namespace std::literals;

template<typename T>
    requires std::integral<T> or std::floating_point<T>
constexpr void digit()
{
    constexpr int w{(int)"unsigned long long"sv.size()};
    std::cout << std::right << std::setw(w)
              << std::meta::display_string_of(^^T) << " : "
              << std::numeric_limits<T>::digits << '\n';
}

template<typename... T>
constexpr void digits()
{
    (digit<T>(), ...);
}

int main()
{
    digits<
        bool, char, signed char, unsigned char, wchar_t, char8_t, char16_t,
        char32_t, short, unsigned short, int, unsigned int, long, unsigned long,
        long long, unsigned long long, float, double, long double
    >();
}
```


**Output:**
```
<nowiki>
              bool : 1
              char : 7
       signed char : 7
     unsigned char : 8
           wchar_t : 31
           char8_t : 8
          char16_t : 16
          char32_t : 32
             short : 15
    unsigned short : 16
               int : 31
      unsigned int : 32
              long : 63
     unsigned long : 64
         long long : 63
unsigned long long : 64
             float : 24
            double : 53
       long double : 64
</nowiki>
```


## See also


| cpp/types/numeric_limits/dsc radix | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |

