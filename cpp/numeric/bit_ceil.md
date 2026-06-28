---
title: std::bit_ceil
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/bit_ceil
---

ddcl|since=c++20|header=bit|
template< class T >
constexpr T bit_ceil( T x );
Calculates the smallest integral power of two that is not smaller than `x`.
If that value is not representable in `T`, the behavior is undefined. Call to this function is permitted in constant evaluation only if the undefined behavior does not occur.
.

## Parameters


### Parameters

- `x` - value of unsigned integer type

## Return value

The smallest integral power of two that is not smaller than `x`.

## Exceptions

Throws nothing.

## Notes


## Possible implementation

See possible implementations in [https://github.com/gcc-mirror/gcc/blob/62c25d7adb1a5664982449dda0e7f9ca63cf4735/libstdc%2B%2B-v3/include/std/bit#L217-L248 libstdc++ (gcc)] and [https://github.com/llvm/llvm-project/blob/llvmorg-14.0.4/libcxx/include/bit#L304-L321 libc++ (clang)].
eq fun|1=
template<typename T, typename ... U>
concept neither = (!std::same_as<T, U> && ...);
template<std::unsigned_integral T>
requires neither<T, bool, char, char8_t, char16_t, char32_t, wchar_t>
constexpr T bit_ceil(T x) noexcept
{
if (x <= 1u)
return T(1);
if constexpr (std::same_as<T, decltype(+x)>)
return T(1) << std::bit_width(T(x - 1));
else
{   // for types subject to integral promotion
constexpr int offset_for_ub =
std::numeric_limits<unsigned>::digits - std::numeric_limits<T>::digits;
return T(1u << (std::bit_width(T(x - 1)) + offset_for_ub) >> offset_for_ub);
}
}

## Example


### Example

```cpp
#include <bit>
#include <bitset>
#include <iostream>

int main()
{
    using bin = std::bitset<8>;
    for (auto x{0U}; 0XA != x; ++x)
        std::cout << "bit_ceil( " << bin(x) << " ) = "
                  << bin(std::bit_ceil(x)) << '\n';
}
```


**Output:**
```
bit_ceil( 00000000 ) = 00000001
bit_ceil( 00000001 ) = 00000001
bit_ceil( 00000010 ) = 00000010
bit_ceil( 00000011 ) = 00000100
bit_ceil( 00000100 ) = 00000100
bit_ceil( 00000101 ) = 00001000
bit_ceil( 00000110 ) = 00001000
bit_ceil( 00000111 ) = 00001000
bit_ceil( 00001000 ) = 00001000
bit_ceil( 00001001 ) = 00010000
```


## See also


| cpp/numeric/dsc bit_floor | (see dedicated page) |

