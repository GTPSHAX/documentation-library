---
title: std::bitset::to_string
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/to_string
---


```cpp
dcl rev multi|num=1|until1=c++11|dcl1=
template< class CharT, class Traits, class Allocator >
std::basic_string<CharT, Traits, Allocator>
to_string( CharT zero = CharT('0'),
CharT one = CharT('1') ) const;
|constexpr2=c++23|dcl2=
template<
class CharT = char,
class Traits = std::char_traits<CharT>,
class Allocator = std::allocator<CharT>
>
std::basic_string<CharT, Traits, Allocator>
to_string( CharT zero = CharT('0'),
CharT one = CharT('1') ) const;
dcla|num=2|until=c++11|1=
template< class CharT, class Traits >
std::basic_string<CharT, Traits>
to_string( CharT zero = CharT('0'),
CharT one = CharT('1') ) const;
dcl|num=3|until=c++11|1=
template< class CharT >
std::basic_string<CharT> to_string( CharT zero = CharT('0'),
CharT one = CharT('1') ) const;
dcl|num=4|until=c++11|1=
std::string to_string( char zero = '0', char one = '1' ) const;
```

Converts the contents of the bitset to a string. Uses `zero` to represent bits with value of `false` and `one` to represent bits with value of `true`.
The resulting string contains `N` characters with the first character corresponds to the last (`N-1`) bit and the last character corresponding to the first bit.
rrev|until=c++11|
All template type arguments need to be provided because function templates cannot have default template arguments. Overloads  are provided to simplify the invocations of `to_string`:
2. Uses the default allocator `std::allocator`.
3. Uses the default character trait `std::char_traits` and the default allocator `std::allocator`.
4. Uses the default character type `char`, the default character trait `std::char_traits` and the default allocator `std::allocator`.

## Parameters


### Parameters

- `zero` - character to use to represent `false`
- `one` - character to use to represent `true`

## Return value

1. The converted string.
2. `to_string<CharT, Traits, std::allocator<CharT>>(zero, one)`.
3. `to_string<CharT, std::char_traits<CharT>, std::allocator<CharT>>(zero, one)`.
4. `to_string<char, std::char_traits<char>, std::allocator<char>>(zero, one)`.

## Exceptions

May throw `std::bad_alloc` from the `std::basic_string` constructor.

## Notes

Since C++11, functions templates can have default template arguments.  removed the helper overloads  and added the corresponding default template arguments in .

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<8> b{42};
    std::cout << b.to_string() << '\n'
              << b.to_string('*') << '\n'
              << b.to_string('O', 'X') << '\n';
}
```


**Output:**
```
00101010
**1*1*1*
OOXOXOXO
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-434 | C++98 | all template arguments needed to be provided | added overloads vl |


## See also


| cpp/utility/bitset/dsc to_ulong | (see dedicated page) |
| cpp/utility/bitset/dsc to_ullong | (see dedicated page) |

