---
title: std::bit_width
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/bit_width
---

ddcl|since=c++20|header=bit|
template< class T >
constexpr int bit_width( T x ) noexcept;
If `x` is not zero, calculates the number of bits needed to store the value `x`, that is, (x)). If `x` is zero, returns zero.
.

## Parameters


### Parameters

- `x` - unsigned integer value

## Return value

Zero if `x` is zero; otherwise, one plus the base-2 logarithm of `x`, with any fractional part discarded.

## Notes

This function is equivalent to `return std::numeric_limits<T>::digits - std::countl_zero(x);`.

## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <iostream>

int main()
{
    for (unsigned x{}; x != 010; ++x)
        std::cout << "bit_width( "
                  << std::bitset<4>{x} << " ) = "
                  << std::bit_width(x) << '\n';
}
```


**Output:**
```
bit_width( 0000 ) = 0
bit_width( 0001 ) = 1
bit_width( 0010 ) = 2
bit_width( 0011 ) = 2
bit_width( 0100 ) = 3
bit_width( 0101 ) = 3
bit_width( 0110 ) = 3
bit_width( 0111 ) = 3
```


## Defect reports


## See also


| cpp/numeric/dsc countl_zero | (see dedicated page) |

