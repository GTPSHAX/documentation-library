---
title: std::countl_zero
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/countl_zero
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr int countl_zero( T x ) noexcept;
Returns the number of consecutive `0` bits in the value of `x`, starting from the most significant bit (“left”).
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The number of consecutive `0` bits in the value of `x`, starting from the most significant bit.

## Notes


## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <cstdint>
#include <iostream>

int main()
{
    for (const std::uint8_t i : {0, 0b11111111, 0b11110000, 0b00011110})
        std::cout << "countl_zero( " << std::bitset<8>(i) << " ) = "
                  << std::countl_zero(i) << '\n';
}
```


**Output:**
```
countl_zero( 00000000 ) = 8
countl_zero( 11111111 ) = 0
countl_zero( 11110000 ) = 0
countl_zero( 00011110 ) = 3
```


## See also


| cpp/numeric/dsc countl_one | (see dedicated page) |
| cpp/numeric/dsc countr_zero | (see dedicated page) |
| cpp/numeric/dsc countr_one | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/utility/bitset/dsc all_any_none | (see dedicated page) |

