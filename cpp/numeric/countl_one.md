---
title: std::countl_one
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/countl_one
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr int countl_one( T x ) noexcept;
Returns the number of consecutive `1` (“one”) bits in the value of `x`, starting from the most significant bit (“left”).
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The number of consecutive `1` bits in the value of `x`, starting from the most significant bit.

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
    for (const std::uint8_t i : {0, 0b11111111, 0b01111111, 0b11100011})
        std::cout << "countl_one( " << std::bitset<8>(i) << " ) = "
                  << std::countl_one(i) << '\n';
}
```


**Output:**
```
countl_one( 00000000 ) = 0
countl_one( 11111111 ) = 8
countl_one( 01111111 ) = 0
countl_one( 11100011 ) = 3
```


## See also


| cpp/numeric/dsc countl_zero | (see dedicated page) |
| cpp/numeric/dsc countr_zero | (see dedicated page) |
| cpp/numeric/dsc countr_one | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/numeric/dsc has_single_bit | (see dedicated page) |
| cpp/utility/bitset/dsc count | (see dedicated page) |
| cpp/utility/bitset/dsc all_any_none | (see dedicated page) |

