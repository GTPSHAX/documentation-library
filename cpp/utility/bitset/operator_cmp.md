---
title: std::bitset::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/operator_cmp
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
bool operator==( const bitset& rhs ) const;
dcla|num=2|noexcept=c++11|until=c++20|1=
bool operator!=( const bitset& rhs ) const;
```

1. Returns true if all of the bits in `*this` and `rhs` are equal.
2. Returns true if any of the bits in `*this` and `rhs` are not equal.
rrev|since=c++20|

## Parameters


### Parameters

- `rhs` - bitset to compare

## Return value

1. `true` if the value of each bit in `*this` equals the value of the corresponding bit in `rhs`, otherwise `false`.
2. `true` if `1=!(*this == rhs)`, otherwise `false`.

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> b1(0b0011);
    std::bitset<4> b2(b1);
    std::bitset<4> b3(0b0100);

    std::cout << std::boolalpha;
    std::cout << "b1 == b2: " << (b1 == b2) << '\n';
    std::cout << "b1 == b3: " << (b1 == b3) << '\n';
    std::cout << "b1 != b3: " << (b1 != b3) << '\n';

//  b1 == std::bitset<3>{}; // compile-time error: incompatible types
}
```


**Output:**
```
b1 == b2: true
b1 == b3: false
b1 != b3: true
```

