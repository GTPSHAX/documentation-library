---
title: std::bitset::operator[]
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/operator_at
---


```cpp
dcla|num=1|constexpr=c++11|
bool operator[]( std::size_t pos ) const;
dcla|num=2|constexpr=c++23|
reference operator[]( std::size_t pos );
```

Accesses the bit at position `pos`.
1. Returns the value of the bit.
2. Returns an object of type `std::bitset::reference` that allows modification of the value.

## Parameters


### Parameters

- `pos` - position of the bit to return

## Return value

1. The value of the requested bit.
2. An object of type `std::bitset::reference`, which allows writing to the requested bit.

## Exceptions

Throws nothing.

## Example


### Example

```cpp
#include <bitset>
#include <cstddef>
#include <iostream>

int main()
{
    std::bitset<8> b1{0b00101010}; // binary literal for 42

    for (std::size_t i = 0; i < b1.size(); ++i)
        std::cout << "b1[" << i << "]: " << b1[i] << '\n';
    b1[0] = true; // modifies the first bit through bitset::reference

    std::cout << "After setting bit 0, b1 holds " << b1 << '\n';
}
```


**Output:**
```
b1[0]: 0
b1[1]: 1
b1[2]: 0
b1[3]: 1
b1[4]: 0
b1[5]: 1
b1[6]: 0
b1[7]: 0
After setting bit 0, b1 holds 00101011
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-11 | C++98 | 1. the description was missing in the C++ standard<br>2. there was only the non-const overload | 1. description added<br>2. added the const overload |


## See also


| cpp/utility/bitset/dsc test | (see dedicated page) |

