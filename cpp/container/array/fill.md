---
title: std::array::fill
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/fill
---

ddcl|since=c++11|notes=<sup>(constexpr C++20)</sup>|
void fill( const T& value );
Assigns the `value` to all elements in the container.

## Parameters


### Parameters

- `value` - the value to assign to the elements

## Return value

(none)

## Complexity

Linear in the size of the container.

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>

int main()
{
    constexpr std::size_t xy = 4;

    using Cell = std::array<unsigned char, 8>;

    std::array<Cell, xy * xy> board;

    board.fill({0xE2, 0x96, 0x84, 0xE2, 0x96, 0x80, 0, 0}); // "▄▀";

    for (std::size_t count{}; Cell c : board)
        std::cout << c.data() << ((++count % xy) ? "" : "\n");
}
```


**Output:**
```
▄▀▄▀▄▀▄▀
▄▀▄▀▄▀▄▀
▄▀▄▀▄▀▄▀
▄▀▄▀▄▀▄▀
```


## See also


| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc fill_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |

