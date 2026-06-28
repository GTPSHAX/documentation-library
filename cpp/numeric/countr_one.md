---
title: std::countr_one
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/countr_one
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr int countr_one( T x ) noexcept;
Returns the number of consecutive `1` bits in the value of `x`, starting from the least significant bit (“right”).
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The number of consecutive `1` bits in the value of `x`, starting from the least significant bit.

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
    for (const std::uint8_t i : {0, 0b11111111, 0b11111110, 0b11100011})
        std::cout << "countr_one( " << std::bitset<8>(i) << " ) = "
                  << std::countr_one(i) << '\n';
}
```


**Output:**
```
countr_one( 00000000 ) = 0
countr_one( 11111111 ) = 8
countr_one( 11111110 ) = 0
countr_one( 11100011 ) = 2
```


## See also


| cpp/numeric/dsc countl_zero | (see dedicated page) |
| cpp/numeric/dsc countl_one | (see dedicated page) |
| cpp/numeric/dsc countr_zero | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/numeric/dsc has_single_bit | (see dedicated page) |
| cpp/utility/bitset/dsc count | (see dedicated page) |
| cpp/utility/bitset/dsc all_any_none | (see dedicated page) |

