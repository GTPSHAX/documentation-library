---
title: std::rotl
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/rotl
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr T rotl( T x, int s ) noexcept;
Computes the result of bitwise left-rotating the value of `x` by `s` positions. This operation is also known as a left [Circular shift|circular shift](https://en.wikipedia.org/wiki/Circular shift|circular shift).
Formally, let `N` be `std::numeric_limits<T>::digits` and `r` be `s % N`.
* If `r` is `0`, returns `x`;
* if `r` is positive, returns `(x << r) ;
* if `r` is negative, returns `std::rotr(x, -r)`.
.

## Parameters


### Parameters

- `x` - value of unsigned integer type
- `s` - number of positions to shift

## Return value

The result of bitwise left-rotating `x` by `s` positions.

## Notes


## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <cstdint>
#include <iostream>

int main()
{
    using bin = std::bitset<8>;
    const std::uint8_t x{0b00011101};
    std::cout << bin(x) << " <- x\n";
    for (const int s : {0, 1, 4, 9, -1})
        std::cout << bin(std::rotl(x, s)) << " <- rotl(x, " << s << ")\n";
}
```


**Output:**
```
00011101 <- x
00011101 <- rotl(x, 0)
00111010 <- rotl(x, 1)
11010001 <- rotl(x, 4)
00111010 <- rotl(x, 9)
10001110 <- rotl(x, -1)
```


## See also


| cpp/numeric/dsc rotr | (see dedicated page) |
| cpp/numeric/dsc bit_reverse | (see dedicated page) |
| cpp/utility/bitset/dsc operator_ltltgtgt | (see dedicated page) |

