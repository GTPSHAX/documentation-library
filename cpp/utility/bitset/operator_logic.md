---
title: std::bitset::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/operator_logic
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
bitset& operator&=( const bitset& other );
dcla|num=2|noexcept=c++11|constexpr=c++23|1=
bitset& operator|=( const bitset& other );
dcla|num=3|noexcept=c++11|constexpr=c++23|1=
bitset& operator^=( const bitset& other );
dcla|num=4|noexcept=c++11|constexpr=c++23|1=
bitset operator~() const;
```

Performs binary AND, OR, XOR and NOT.
1. Sets the bits to the result of binary AND on corresponding pairs of bits of `*this` and `other`.
2. Sets the bits to the result of binary OR on corresponding pairs of bits of `*this` and `other`.
3. Sets the bits to the result of binary XOR on corresponding pairs of bits of `*this` and `other`.
4. Returns a temporary copy of `*this` with all bits flipped (binary NOT).
Note that `1=&=`, `1=, and `1=^=` are only defined for bitsets of the same size `N`.

## Parameters


### Parameters

- `other` - another bitset

## Return value

@1-3@ `*this`
4. `std::bitset<N>(*this).flip()`

## Example


### Example

```cpp
#include <bitset>
#include <cstddef>
#include <iostream>
#include <string>

int main()
{
    const std::string pattern_str{"1001"};
    std::bitset<16> pattern{pattern_str}, dest;

    for (std::size_t i = dest.size() / pattern_str.size(); i != 0; --i)
    {
        dest <<= pattern_str.size();
        dest {{!
```

std::cout << dest << " (i = " << i << ")\n";
}
std::cout << ~dest << " (~dest)\n";
}
|output=
0000000000001001 (i = 4)
0000000010011001 (i = 3)
0000100110011001 (i = 2)
1001100110011001 (i = 1)
0110011001100110 (~dest)

## See also


| cpp/utility/bitset/dsc operator_ltltgtgt | (see dedicated page) |

