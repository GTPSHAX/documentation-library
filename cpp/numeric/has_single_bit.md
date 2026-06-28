---
title: std::has_single_bit
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/has_single_bit
---

ddcl|since=c++20|header=bit|
template< class T >
constexpr bool has_single_bit( T x ) noexcept;
Checks if `x` is an integral power of two.
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

`true` if `x` is an integral power of two; otherwise `false`.

## Notes


## Possible implementation

eq fun|1=
template<typename T, typename ... U>
concept neither = (!std::same_as<T, U> && ...);
template<typename T>
concept unsigned_integer = std::unsigned_integral<T> &&
neither<T, bool, char, char8_t, char16_t, char32_t, wchar_t>;
// First version
constexpr bool has_single_bit(unsigned_integer auto x) noexcept
{
return x && !(x & (x - 1));
}
// Second version
constexpr bool has_single_bit(unsigned_integer auto x) noexcept
{
return std::popcount(x) == 1;
}

## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <cmath>
#include <iostream>

int main()
{
    for (auto u{0u}; u != 0B1010; ++u)
    {
        std::cout << "u = " << u << " = " << std::bitset<4>(u);
        if (std::has_single_bit(u))
            std::cout << " = 2^" << std::log2(u) << " (is power of two)";
        std::cout << '\n';
    }
}
```


**Output:**
```
u = 0 = 0000
u = 1 = 0001 = 2^0 (is power of two)
u = 2 = 0010 = 2^1 (is power of two)
u = 3 = 0011
u = 4 = 0100 = 2^2 (is power of two)
u = 5 = 0101
u = 6 = 0110
u = 7 = 0111
u = 8 = 1000 = 2^3 (is power of two)
u = 9 = 1001
```


## See also


| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/utility/bitset/dsc count | (see dedicated page) |
| cpp/utility/bitset/dsc test | (see dedicated page) |

