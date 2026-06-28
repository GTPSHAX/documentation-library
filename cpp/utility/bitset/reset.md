---
title: std::bitset::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/reset
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
bitset& reset();
dcla|num=2|constexpr=c++23|
bitset& reset( std::size_t pos );
```

Sets bits to `false`.
1. Sets all bits to `false`
2. Sets the bit at position `pos` to `false`.

## Parameters


### Parameters

- `pos` - the position of the bit to set

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
    std::bitset<8> b(42);
    std::cout << "Bitset is         " << b << '\n';
    b.reset(1);
    std::cout << "After b.reset(1): " << b << '\n';
    b.reset();
    std::cout << "After b.reset():  " << b << '\n';
}
```


**Output:**
```
Bitset is         00101010
After b.reset(1): 00101000
After b.reset():  00000000
```


## Defect reports


## See also


| cpp/utility/bitset/dsc set | (see dedicated page) |
| cpp/utility/bitset/dsc flip | (see dedicated page) |

