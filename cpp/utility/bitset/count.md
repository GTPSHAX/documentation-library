---
title: std::bitset::count
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/count
---

ddcla|noexcept=c++11|constexpr=c++23|
std::size_t count() const;
Returns the number of bits that are set to `true`.

## Return value

Number of bits that are set to `true`.

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

constexpr auto popcount(unsigned x) noexcept
{
    unsigned num{};
    for (; x; ++num, x &= (x - 1));
    return num;
}
static_assert(popcount(0b101010) == std::bitset<8>{0b101010}.count());

int main()
{
    std::bitset<8> b("00010010");
    std::cout << "Initial value: " << b << '\n';

    // Find the first unset bit
    std::size_t idx = 0;
    while (idx < b.size() && b.test(idx))
        ++idx;

    // Continue setting bits until half the bitset is filled
    while (idx < b.size() && b.count() < b.size() / 2)
    {
        b.set(idx);
        std::cout << "Setting bit " << idx << ": " << b << '\n';
        while (idx < b.size() && b.test(idx))
            ++idx;
    }
}
```


**Output:**
```
Initial value: 00010010
Setting bit 0: 00010011
Setting bit 2: 00010111
```


## See also


| cpp/utility/bitset/dsc size | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |

