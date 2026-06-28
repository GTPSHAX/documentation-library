---
title: std::numeric_limits::digits10
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/digits10
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const int digits10;
|dcl2=
static constexpr int digits10;
```

The value of `std::numeric_limits<T>::digits10` is the number of base-10 digits that can be represented by the type `T` without change, that is, any number with this many significant decimal digits can be converted to a value of type `T` and back to decimal form, without change due to rounding or overflow. For base-`radix` types, it is the value of  (`digits - 1` for floating-point types) multiplied by mathjax-or|\(\small \log_{10}{radix}\)|log(radix) and rounded down.

## Standard specializations


| Item | Description |
|------|-------------|
| **{{tt** | T |


## Example

An 8-bit binary type can represent any two-digit decimal number exactly, but 3-digit decimal numbers 256..999 cannot be represented. The value of `digits10` for an 8-bit type is 2 (`std::log10(2)` &approx; 0.30103, so `1=8 * std::log10(2)` is &approx; 2.41).
The standard 32-bit IEEE 754 floating-point type has a 24 bit fractional part (23 bits written, one implied), which may suggest that it can represent 7 digit decimals (`1=24 * std::log10(2)` is &approx; 7.22), but relative rounding errors are non-uniform and some floating-point values with 7 decimal digits do not survive conversion to 32-bit float and back: the smallest positive example is `8.589973e9`, which becomes `8.589974e9` after the roundtrip. These rounding errors cannot exceed one bit in the representation, and `digits10` is calculated as `1=(24 - 1) * std::log10(2)`, which is &approx; 6.92. Rounding down results in the value 6.
Likewise, the 16-digit string `9007199254740993` does not survive text &rarr; double &rarr; text roundtrip, becoming `9007199254740992`: the 64-bit IEEE 754 type double guarantees this roundtrip only for 15 decimal digits.

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
constexpr void digit10()
{
    constexpr int w{(int)"unsigned long long"sv.size()};
    std::cout << std::right << std::setw(w)
              << std::meta::display_string_of(^^T) << " : "
              << std::numeric_limits<T>::digits10 << '\n';
}

template<typename... T>
constexpr void digits10()
{
    (digit10<T>(), ...);
}

int main()
{
    digits10<
        bool, char, signed char, unsigned char, wchar_t, char8_t, char16_t,
        char32_t, short, unsigned short, int, unsigned int, long, unsigned long,
        long long, unsigned long long, float, double, long double
    >();
}
```


**Output:**
```
<nowiki>
              bool : 0
              char : 2
       signed char : 2
     unsigned char : 2
           wchar_t : 9
           char8_t : 2
          char16_t : 4
          char32_t : 9
             short : 4
    unsigned short : 4
               int : 9
      unsigned int : 9
              long : 18
     unsigned long : 19
         long long : 18
unsigned long long : 19
             float : 6
            double : 15
       long double : 18
</nowiki>
```


## See also


| cpp/types/numeric_limits/dsc max_digits10 | (see dedicated page) |
| cpp/types/numeric_limits/dsc radix | (see dedicated page) |
| cpp/types/numeric_limits/dsc digits | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |

