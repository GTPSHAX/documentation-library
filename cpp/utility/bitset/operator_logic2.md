---
title: operators (std::bitset)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/operator_logic2
---


# 1=operator&,!


```cpp
**Header:** `<`bitset`>`
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
template< std::size_t N >
std::bitset<N> operator&( const std::bitset<N>& lhs,
const std::bitset<N>& rhs );
dcla|num=2|noexcept=c++11|constexpr=c++23|1=
template< std::size_t N >
std::bitset<N> operator|( const std::bitset<N>& lhs,
const std::bitset<N>& rhs );
dcla|num=3|noexcept=c++11|constexpr=c++23|1=
template< std::size_t N >
std::bitset<N> operator^( const std::bitset<N>& lhs,
const std::bitset<N>& rhs );
```

Performs binary AND, OR, and XOR between two bitsets, `lhs` and `rhs`.
1. Returns a `std::bitset<N>` containing the result of binary AND on corresponding pairs of bits of `lhs` and `rhs`.
2. Returns a `std::bitset<N>` containing the result of binary OR on corresponding pairs of bits of `lhs` and `rhs`.
3. Returns a `std::bitset<N>` containing the result of binary XOR on corresponding pairs of bits of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs` - the bitset on the left-hand side of the operator
- `rhs` - the bitset on the right-hand side of the operator

## Return value

1. `std::bitset<N>(lhs) &
2. `std::bitset<N>(lhs)
3. `std::bitset<N>(lhs) ^

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> b1("0110");
    std::bitset<4> b2("0011");

    std::cout << "b1 & b2: " << (b1 & b2) << '\n';
    std::cout << "b1 {{!
```

std::cout << "b1 ^ b2: " << (b1 ^ b2) << '\n';
}
|output=
b1 & b2: 0010
b1 | b2: 0111
b1 ^ b2: 0101

## See also


| cpp/utility/bitset/dsc operator_logic | (see dedicated page) |

