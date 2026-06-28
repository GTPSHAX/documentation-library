---
title: std::rotr
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/rotr
---

ddcl|header=bit|since=c++20|
template< class T >
constexpr T rotr( T x, int s ) noexcept;
Computes the result of bitwise right-rotating the value of `x` by `s` positions. This operation is also known as a right [Circular shift|circular shift](https://en.wikipedia.org/wiki/Circular shift|circular shift).
Formally, let `N` be `std::numeric_limits<T>::digits` and `r` be `s % N`.
* If `r` is `0`, returns `x`;
* if `r` is positive, returns `(x >> r) ;
* if `r` is negative, returns `std::rotl(x, -r)`.
.

## Parameters


### Parameters

- `x` - value of unsigned integer type
- `s` - number of positions to shift

## Return value

The result of bitwise right-rotating `x` by `s` positions.

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
    for (const int s : {0, 1, 9, -1, 2})
        std::cout << bin(std::rotr(x, s)) << " <- rotr(x, " << s << ")\n";
}
```


**Output:**
```
00011101 <- x
00011101 <- rotr(x, 0)
10001110 <- rotr(x, 1)
10001110 <- rotr(x, 9)
00111010 <- rotr(x, -1)
01000111 <- rotr(x, 2)
```


## See also


| cpp/numeric/dsc rotl | (see dedicated page) |
| cpp/numeric/dsc bit_reverse | (see dedicated page) |
| cpp/utility/bitset/dsc operator_ltltgtgt | (see dedicated page) |

