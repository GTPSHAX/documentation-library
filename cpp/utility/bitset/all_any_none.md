---
title: std::bitset::none
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/all_any_none
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
bool all() const;
dcla|num=2|noexcept=c++11|constexpr=c++23|1=
bool any() const;
dcla|num=3|noexcept=c++11|constexpr=c++23|1=
bool none() const;
```

1. Checks if all bits are set to `true`.
2. Checks if any bits are set to `true`.
3. Checks if none of the bits are set to `true`.

## Return value

1. `true` if all bits are set to `true`, otherwise `false`.
2. `true` if any of the bits are set to `true`, otherwise `false`.
3. `true` if none of the bits are set to `true`, otherwise `false`.

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> b1("0000");
    std::bitset<4> b2("0101");
    std::bitset<4> b3("1111");

    std::cout
        << "bitset\t" << "all\t" << "any\t" << "none\n"
        << b1 << '\t' << b1.all() << '\t' << b1.any() << '\t' << b1.none() << '\n'
        << b2 << '\t' << b2.all() << '\t' << b2.any() << '\t' << b2.none() << '\n'
        << b3 << '\t' << b3.all() << '\t' << b3.any() << '\t' << b3.none() << '\n';
}
```


**Output:**
```
bitset  all any none
0000    0   0   1
0101    0   1   0
1111    1   1   0
```


## Defect reports


## See also


| cpp/utility/bitset/dsc count | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |

