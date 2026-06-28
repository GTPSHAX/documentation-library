---
title: std::bitset::flip
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/flip
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
bitset& flip();
dcla|num=2|constexpr=c++23|
bitset& flip( std::size_t pos );
```

Flips bits, i.e. changes `true` values to `false` and `false` values to `true`.   Equivalent to a logical NOT operation on part or all of the bitset.
1. Flips all bits (like `operator~`, but in-place).
2. Flips the bit at the position `pos`.

## Parameters


### Parameters

- `pos` - the position of the bit to flip

## Return value

`*this`

## Exceptions

2. Throws `std::out_of_range` if `pos` does not correspond to a valid bit position.

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> flops;

    std::cout << flops << '\n'
              << flops.flip(0) << '\n'
              << flops.flip(2) << '\n'
              << flops.flip() << '\n';
}
```


**Output:**
```
0000
0001
0101
1010
```


## Defect reports


## See also


| cpp/utility/bitset/dsc set | (see dedicated page) |
| cpp/utility/bitset/dsc reset | (see dedicated page) |
| cpp/utility/bitset/dsc operator logic | (see dedicated page) |
| cpp/container/vector_bool/dsc flip | (see dedicated page) |

