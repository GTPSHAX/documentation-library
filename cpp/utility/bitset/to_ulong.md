---
title: std::bitset::to_ulong
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/to_ulong
---

ddcl|notes=<sup>(constexpr C++23)</sup>|
unsigned long to_ulong() const
Converts the contents of the bitset to an `unsigned long` integer.
The first bit of the bitset corresponds to the least significant digit of the number and the last bit corresponds to the most significant digit.

## Return value

The converted integer.

## Exceptions

Throws `std::overflow_error` if the value can not be represented in `unsigned long`.

## Example


### Example

```cpp
#include <bitset>
#include <iostream>
#include <stdexcept>

int main()
{
    for (unsigned long i = 0; i < 10; ++i)
    {
        std::bitset<5> b(i);
        std::bitset<5> b_inverted = ~b;
        std::cout << i << '\t' << b << '\t' << b_inverted << '\t'
                  << b_inverted.to_ulong() << '\n';
    }

    std::cout << std::bitset<32>().to_string('-') << '\n';

    try
    {
        std::bitset<128> x(42);
        std::cout << x.to_ulong() << '\n';
        x.flip();
        std::cout << x.to_ulong() << '\n'; // throws
    }
    catch (const std::overflow_error& ex)
    {
        std::cout << "ex: " << ex.what() << '\n';
    }
}
```


**Output:**
```
0   00000   11111   31
1   00001   11110   30
2   00010   11101   29
3   00011   11100   28
4   00100   11011   27
5   00101   11010   26
6   00110   11001   25
7   00111   11000   24
8   01000   10111   23
9   01001   10110   22
--------------------------------
42
ex: bitset to_ulong overflow error
```


## See also


| cpp/utility/bitset/dsc to_string | (see dedicated page) |
| cpp/utility/bitset/dsc to_ullong | (see dedicated page) |

