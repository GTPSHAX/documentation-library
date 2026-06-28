---
title: std::bitset
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset
---

ddcl|header=bitset|
template< std::size_t N >
class bitset;
The class template `bitset` represents a fixed-size sequence of `N` bits. Bitsets can be manipulated by standard logic operators and converted to and from strings and integers. For the purpose of the string representation and of naming directions for shift operations, the sequence is thought of as having its lowest indexed elements at the ''right'', as in the binary representation of integers.
`bitset` meets the requirements of *CopyConstructible* and *CopyAssignable*.

## Template parameters


### Parameters

- `N` - the number of bits to allocate storage for

## Member types


| cpp/utility/bitset/reference|proxy class representing a reference to a bit | |


## Member functions


| cpp/utility/bitset/dsc constructor | (see dedicated page) |
| cpp/utility/bitset/dsc operator_cmp | (see dedicated page) |

#### Element access

| cpp/utility/bitset/dsc operator_at | (see dedicated page) |
| cpp/utility/bitset/dsc test | (see dedicated page) |
| cpp/utility/bitset/dsc all_any_none | (see dedicated page) |
| cpp/utility/bitset/dsc count | (see dedicated page) |

#### Capacity

| cpp/utility/bitset/dsc size | (see dedicated page) |

#### Modifiers

| cpp/utility/bitset/dsc operator_logic | (see dedicated page) |
| cpp/utility/bitset/dsc operator_ltltgtgt | (see dedicated page) |
| cpp/utility/bitset/dsc set | (see dedicated page) |
| cpp/utility/bitset/dsc reset | (see dedicated page) |
| cpp/utility/bitset/dsc flip | (see dedicated page) |

#### Conversions

| cpp/utility/bitset/dsc to_string | (see dedicated page) |
| cpp/utility/bitset/dsc to_ulong | (see dedicated page) |
| cpp/utility/bitset/dsc to_ullong | (see dedicated page) |


## Non-member functions


| cpp/utility/bitset/dsc operator_logic2 | (see dedicated page) |
| cpp/utility/bitset/dsc operator_ltltgtgt2 | (see dedicated page) |


## Helper classes


| cpp/utility/bitset/dsc hash | (see dedicated page) |


## Notes

If the size of a bit-set is not known at compile time, or it is necessary to change its size at run-time, the dynamic types such as `cpp/container/vector bool|std::vector<bool>` or [https://www.boost.org/doc/libs/release/libs/dynamic_bitset/dynamic_bitset.html `boost::dynamic_bitset<>`] may be used instead.

## Example


### Example

```cpp
#include <bitset>
#include <cassert>
#include <cstddef>
#include <iostream>

int main()
{
    typedef std::size_t length_t, position_t; // the hints

    // constructors:
    constexpr std::bitset<4> b1;
    constexpr std::bitset<4> b2{0xA}; // == 0B1010
    std::bitset<4> b3{"0011"}; // can also be constexpr since C++23
    std::bitset<8> b4{"ABBA", length_t(4), /*0:*/'A', /*1:*/'B'}; // == 0B0000'0110

    // bitsets can be printed out to a stream:
    std::cout << "b1:" << b1 << "; b2:" << b2 << "; b3:" << b3 << "; b4:" << b4 << '\n';

    // bitset supports bitwise operations:
    b3 {{!
```

b3 &= 0b0011; assert(b3 == 0b0011);
b3 ^= std::bitset<4>{0b1100}; assert(b3 == 0b1111);
// operations on the whole set:
b3.reset(); assert(b3 == 0);
b3.set(); assert(b3 == 0b1111);
assert(b3.all() && b3.any() && !b3.none());
b3.flip(); assert(b3 == 0);
// operations on individual bits:
b3.set(position_t(1), true); assert(b3 == 0b0010);
b3.set(position_t(1), false); assert(b3 == 0);
b3.flip(position_t(2)); assert(b3 == 0b0100);
b3.reset(position_t(2)); assert(b3 == 0);
// subscript operator[] is supported:
b3[2] = true; assert(true == b3[2]);
// other operations:
assert(b3.count() == 1);
assert(b3.size() == 4);
assert(b3.to_ullong() == 0b0100ULL);
assert(b3.to_string() == "0100");
}
|output=b1:0000; b2:1010; b3:0011; b4:00000110

## See also


| cpp/container/dsc vector_bool | (see dedicated page) |

