---
title: std::byteswap
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/byteswap
---

ddcl|since=c++23|header=bit|
template< class T >
constexpr T byteswap( T n ) noexcept;
Reverses the bytes in the given integer value `n`.
`std::byteswap` participates in overload resolution only if `T` satisfies , i.e., `T` is an integer type. The program is ill-formed if `T` has padding bits.

## Parameters


### Parameters

- `n` - integer value

## Return value

An integer value of type `T` whose object representation comprises the bytes of that of `n` in reversed order.

## Notes

This function is useful for processing data of different endianness.

## Possible implementation

eq fun
|1=
template<std::integral T>
constexpr T byteswap(T value) noexcept
{
static_assert(std::has_unique_object_representations_v<T>,
"T may not have padding bits");
auto value_representation = std::bit_cast<std::array<std::byte, sizeof(T)>>(value);
std::ranges::reverse(value_representation);
return std::bit_cast<T>(value_representation);
}

## Example


### Example


**Output:**
```
byteswap for U16:
CAFE : FE CA
FECA : CA FE

byteswap for U32:
DEADBEEF : EF BE AD DE
EFBEADDE : DE AD BE EF

byteswap for U64:
0123456789ABCDEF : EF CD AB 89 67 45 23 01
EFCDAB8967452301 : 01 23 45 67 89 AB CD EF
```


## See also


| cpp/types/dsc endian | (see dedicated page) |
| cpp/numeric/dsc rotl | (see dedicated page) |
| cpp/numeric/dsc rotr | (see dedicated page) |
| cpp/numeric/dsc bit_reverse | (see dedicated page) |

