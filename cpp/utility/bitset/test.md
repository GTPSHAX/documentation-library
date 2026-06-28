---
title: std::bitset::test
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/test
---

ddcla|constexpr=c++23|
bool test( std::size_t pos ) const;
Returns the value of the bit at the position `pos` (counting from 0).
Unlike `operator[]`, it performs a bounds check.

## Parameters


### Parameters

- `pos` - position of the bit to return (counting from 0)

## Return value

`true` if the requested bit is set, `false` otherwise.

## Exceptions

Throws `std::out_of_range` if `pos` does not correspond to a valid bit position.

## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <cassert>
#include <iostream>
#include <stdexcept>

int main()
{
    std::bitset<10> b1("1111010000");

    std::size_t idx = 0;
    while (idx < b1.size() && !b1.test(idx))
        ++idx;

    assert(static_cast<int>(idx) == std::countr_zero(b1.to_ulong()));

    if (idx < b1.size())
        std::cout << "The first set bit is at index " << idx << '\n';
    else
        std::cout << "no set bits\n";

    try
    {
        std::bitset<0B10'1001'1010> bad;
        if (bad.test(bad.size()))
            std::cout << "Expect unexpected!\n";
    }
    catch (std::out_of_range const& ex)
    {
        std::cout << "Exception: " << ex.what() << '\n';
    }
}
```


**Output:**
```
The first set bit is at index 4
Exception: bitset::test: __position (which is 666) >= _Nb (which is 666)
```


## Defect reports


## See also


| cpp/utility/bitset/dsc operator at | (see dedicated page) |
| cpp/numeric/dsc popcount | (see dedicated page) |
| cpp/numeric/dsc has_single_bit | (see dedicated page) |

