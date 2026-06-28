---
title: std::byte
type: Utilities
source: https://en.cppreference.com/w/cpp/types/byte
---

ddcl|header=cstddef|since=c++17|
enum class byte : unsigned char {};
`std::byte` is a distinct type that implements the concept of byte as specified in the C++ language definition.
Like `unsigned char`, it can be used to access raw memory occupied by other objects (object representation), but unlike `unsigned char`, it is not a character type and is not an arithmetic type. `std::byte` models a mere collection of bits, supporting only bitshift operations with an integer, and bitwise and comparison operations with another `std::byte`.

## Non-member functions

member|to_integer|2=

```cpp
dcl|since=c++17|
template< class IntegerType >
constexpr IntegerType to_integer( std::byte b ) noexcept;
```

Equivalent to: `return IntegerType(b);`
member|1=operator<<=,operator>>=|2=

```cpp
dcl|since=c++17|num=1|1=
template< class IntegerType >
constexpr std::byte& operator<<=( std::byte& b, IntegerType shift ) noexcept;
dcl|since=c++17|num=2|1=
template< class IntegerType >
constexpr std::byte& operator>>=( std::byte& b, IntegerType shift ) noexcept;
```

1. Equivalent to: `1=return b = b << shift;`
.
2. Equivalent to: `1=return b = b >> shift;`
.
member|operator<<,operator>>|2=

```cpp
dcl|since=c++17|num=1|
template< class IntegerType >
constexpr std::byte operator<<( std::byte b, IntegerType shift ) noexcept;
dcl|since=c++17|num=2|
template< class IntegerType >
constexpr std::byte operator>>( std::byte b, IntegerType shift ) noexcept;
```

1. Equivalent to: `return std::byte(static_cast<unsigned int>(b) << shift);`
.
2. Equivalent to: `return std::byte(static_cast<unsigned int>(b) >> shift);`
.
member|1=operator|=,operator&=,operator^=|2=

```cpp
dcl|since=c++17|num=1|1=
constexpr std::byte& operator|=( std::byte& l, std::byte r ) noexcept;
dcl|since=c++17|num=2|1=
constexpr std::byte& operator&=( std::byte& l, std::byte r ) noexcept;
dcl|since=c++17|num=3|1=
constexpr std::byte& operator^=( std::byte& l, std::byte r ) noexcept;
```

1. Equivalent to: `1=return l = l .
2. Equivalent to: `1=return l = l & r;`.
3. Equivalent to: `1=return l = l ^ r;`.
member|operator|,operator&,operator^,operator~|2=

```cpp
dcl|since=c++17|num=1|1=
constexpr std::byte operator|( std::byte l, std::byte r ) noexcept;
dcl|since=c++17|num=2|
constexpr std::byte operator&( std::byte l, std::byte r ) noexcept;
dcl|since=c++17|num=3|
constexpr std::byte operator^( std::byte l, std::byte r ) noexcept;
dcl|since=c++17|num=4|
constexpr std::byte operator~( std::byte b ) noexcept;
```

1. Equivalent to: `1=return std::byte(static_cast<unsigned int>(l) .
2. Equivalent to: `1=return std::byte(static_cast<unsigned int>(l) & static_cast<unsigned int>(r));`.
3. Equivalent to: `1=return std::byte(static_cast<unsigned int>(l) ^ static_cast<unsigned int>(r));`.
4. Equivalent to: `1=return std::byte(~static_cast<unsigned int>(b));`

## Notes

A numeric value `n` can be converted to a byte value using }, due to C++17 relaxed enum class initialization rules.
A byte can be converted to a numeric value (such as to produce an integer hash of an object) the usual way with an explicit conversion or alternatively with `std::to_integer`.

## Example


### Example

```cpp
#include <bitset>
#include <cassert>
#include <cstddef>
#include <iostream>
#include <utility>

std::ostream& operator<<(std::ostream& os, std::byte b)
{
    return os << std::bitset<8>(std::to_integer<int>(b));
}

int main()
{
    // std::byte y = 1; // Error: cannot convert int to byte.
    std::byte y{1}; // OK

    // if (y == 13) {} // Error: cannot be compared.
    if (y == std::byte{13}) {} // OK, bytes are comparable

    int arr[]{1, 2, 3};
    // int c = a[y]; // Error: array subscript is not an integer
    [[maybe_unused]] int i = arr[std::to_integer<int>(y)]; // OK
    [[maybe_unused]] int j = arr[std::to_underlying(y)];   // OK

    auto to_int = [](std::byte b) { return std::to_integer<int>(b); };

    std::byte b{42};
    assert(to_int(b) == 0b00101010);
    std::cout << b << '\n';

    // b *= 2; // Error: b is not of arithmetic type
    b <<= 1;
    assert(to_int(b) == 0b01010100);

    b >>= 1;
    assert(to_int(b) == 0b00101010);

    assert(to_int(b << 1) == 0b01010100);
    assert(to_int(b >> 1) == 0b00010101);

    b {{!
```

assert(to_int(b) == 0b11111010);
b &= std::byte{0b11110000};
assert(to_int(b) == 0b11110000);
b ^= std::byte{0b11111111};
assert(to_int(b) == 0b00001111);
}
|output=
00101010
