---
title: std::bitset::set
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/set
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|
bitset& set();
|1=
bitset& set( std::size_t pos, bool value = true );
```

Sets all bits to `true` or sets one bit to specified value.
1. Sets all bits to `true`.
2. Sets the bit at position `pos` to the value `value`.

## Parameters


### Parameters

- `pos` - the position (counting from `0`, i.e. from least significant to most significant) of the bit to set
- `value` - the value to set the bit to

## Return value

`*this`

## Exceptions

2. Throws `std::out_of_range` if `pos` does not correspond to a valid bit position.

## Example


### Example

```cpp
#include <bitset>
#include <cstddef>
#include <iostream>

int main()
{
    std::bitset<8> b;
    std::cout << b << '\n';
    std::cout << b.set() << '\n';
    std::cout << b.reset() << '\n';

    for (std::size_t i = 1; i < b.size(); i += 2)
        b.set(i);

    std::cout << b << '\n';
}
```


**Output:**
```
00000000
11111111
00000000
10101010
```


## Defect reports


## See also


| cpp/utility/bitset/dsc reset | (see dedicated page) |
| cpp/utility/bitset/dsc flip | (see dedicated page) |

