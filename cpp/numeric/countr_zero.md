---
title: std::countr_zero
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/countr_zero
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr int countr_zero( T x ) noexcept;
Returns the number of consecutive `0` bits in the value of `x`, starting from the least significant bit (“right”).
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The number of consecutive `0` bits in the value of `x`, starting from the least significant bit.

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
    for (const std::uint8_t i : {0, 0b11111111, 0b00011100, 0b00011101})
        std::cout << "countr_zero( " << std::bitset<8>(i) << " ) = "
                  << std::countr_zero(i) << '\n';
}
```


**Output:**
```
countr_zero( 00000000 ) = 8
countr_zero( 11111111 ) = 0
countr_zero( 00011100 ) = 2
countr_zero( 00011101 ) = 0
```


## See also


| cpp/numeric/dsc countl_zero | (see dedicated page) |
| cpp/numeric/dsc countl_one | (see dedicated page) |
| cpp/numeric/dsc countr_one | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/utility/bitset/dsc all any none | (see dedicated page) |

