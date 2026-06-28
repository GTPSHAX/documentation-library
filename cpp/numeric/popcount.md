---
title: std::popcount
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/popcount
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr int popcount( T x ) noexcept;
Returns the number of `1` bits in the value of `x`.
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The number of `1` bits in the value of `x`.

## Notes


## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <cstdint>
#include <iostream>

static_assert(std::popcount(0xFULL) == 4);

int main()
{
    for (const std::uint8_t x : {0, 0b00011101, 0b11111111})
        std::cout << "popcount( " << std::bitset<8>(x) << " ) = "
                  << std::popcount(x) << '\n';
}
```


**Output:**
```
popcount( 00000000 ) = 0
popcount( 00011101 ) = 4
popcount( 11111111 ) = 8
```


## See also


| cpp/numeric/dsc countl_zero | (see dedicated page) |
| cpp/numeric/dsc countl_one | (see dedicated page) |
| cpp/numeric/dsc countr_zero | (see dedicated page) |
| cpp/numeric/dsc countr_one | (see dedicated page) |
| cpp/numeric/dsc has_single_bit | (see dedicated page) |
| cpp/utility/bitset/dsc count | (see dedicated page) |
| cpp/utility/bitset/dsc all_any_none | (see dedicated page) |

