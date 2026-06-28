---
title: std::bit_floor
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/bit_floor
---

ddcl|since=c++20|header=bit|
template< class T >
constexpr T bit_floor( T x ) noexcept;
If `x` is not zero, calculates the largest integral power of two that is not greater than `x`. If `x` is zero, returns zero.
.

## Parameters


### Parameters

- `x` - unsigned integer value

## Return value

Zero if `x` is zero; otherwise, the largest integral power of two that is not greater than `x`.

## Notes


## Possible implementation

eq fun
|1=
template<typename T, typename ... U>
concept neither = (!std::same_as<T, U> && ...);
template<std::unsigned_integral T>
requires neither<T, bool, char, char8_t, char16_t, char32_t, wchar_t>
constexpr T bit_floor(T x) noexcept
{
if (x != 0)
return T{1} << (std::bit_width(x) - 1);
return 0;
}

## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <iostream>

int main()
{
    using bin = std::bitset<8>;
    for (unsigned x{}; x != 012; ++x)
        std::cout << "bit_floor( " << bin(x) << " ) = "
                  << bin(std::bit_floor(x)) << '\n';
}
```


**Output:**
```
bit_floor( 00000000 ) = 00000000
bit_floor( 00000001 ) = 00000001
bit_floor( 00000010 ) = 00000010
bit_floor( 00000011 ) = 00000010
bit_floor( 00000100 ) = 00000100
bit_floor( 00000101 ) = 00000100
bit_floor( 00000110 ) = 00000100
bit_floor( 00000111 ) = 00000100
bit_floor( 00001000 ) = 00001000
bit_floor( 00001001 ) = 00001000
```


## See also


| cpp/numeric/dsc bit_ceil | (see dedicated page) |
| cpp/numeric/dsc rotr | (see dedicated page) |
| cpp/numeric/dsc bit_width | (see dedicated page) |
| cpp/numeric/dsc has_single_bit | (see dedicated page) |

