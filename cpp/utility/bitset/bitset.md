---
title: std::bitset::bitset
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/bitset
---


```cpp
dcla|num=1|constexpr=c++11|noexcept=c++11|
bitset();
dcl rev multi|num=2|until1=c++11|dcl1=
bitset( unsigned long val );
|dcl2=
constexpr bitset( unsigned long long val ) noexcept;
dcla|num=3|constexpr=c++23|1=
template< class CharT, class Traits, class Alloc >
explicit bitset
( const std::basic_string<CharT, Traits, Alloc>& str,
typename std::basic_string
<CharT, Traits, Alloc>::size_type pos = 0,
typename std::basic_string<CharT, Traits, Alloc>::size_type
n = std::basic_string<CharT, Traits, Alloc>::npos,
CharT zero = CharT('0'), CharT one = CharT('1') );
dcla|num=4|since=c++26|1=
template< class CharT, class Traits >
constexpr explicit bitset
( std::basic_string_view<CharT, Traits> str,
std::size_t pos = 0, std::size_t n = std::size_t(-1),
CharT zero = CharT('0'), CharT one = CharT('1') );
dcla|num=5|since=c++11|constexpr=c++23|1=
template< class CharT >
explicit bitset( const CharT* str, std::size_t n = std::size_t(-1),
CharT zero = CharT('0'), CharT one = CharT('1') );
```

Constructs a new bitset from one of several optional data sources:
1. Default constructor. Constructs a bitset with all bits set to zero.
2. Constructs a bitset from an unsigned integer `val`.
@@ Given the number of bits in the value representation of <sup>(until C++11)</sup> `unsigned long`<sup>(since C++11)</sup> `unsigned long long` as `S`:
* The first (rightmost, least significant) `std::min(S, N)` bit positions are initialized with the corresponding bit values of `val`.
* If `S` is less than `N`, the remaining bit positions are initialized to zeroes.
3. Constructs a bitset using the characters in `str`. An optional starting position `pos` and length `n` can be provided, as well as characters denoting alternate values for set (`one`) and unset (`zero`) bits. `Traits::eq()` is used to compare the character values.
@@ The effective length of the initializing string is `std::min(n, str.size() - pos)`.
4. Similar to , but uses a `std::basic_string_view` instead of a `std::basic_string`.
5. Similar to , but uses a `const CharT*` instead of a `std::basic_string`.
rev|until=c++26|
Equivalent to .
rev|since=c++26|
Equivalent to .

## Parameters


### Parameters

- `val` - number used to initialize the bitset
- `str` - string used to initialize the bitset
- `pos` - a starting offset into `str`
- `n` - number of characters to use from `str`
- `zero` - alternate character for unset bits in `str`
- `one` - alternate character for set bits in `str`

## Exceptions

@3,4@ `std::out_of_range` if `pos > str.size()`, `std::invalid_argument` if any character is not `one` or `zero`.
5. `std::invalid_argument` if any character is not `one` or `zero`.

## Notes


## Example


### Example

```cpp
#include <bitset>
#include <climits>
#include <iostream>
#include <string>

int main()
{
    // empty constructor (1)
    std::bitset<8> b1; // [0,0,0,0,0,0,0,0]

    // unsigned long long constructor (2)
    std::bitset<8> b2(42);          // [0,0,1,0,1,0,1,0]
    std::bitset<70> bl(ULLONG_MAX); // [0,0,0,0,0,0,1,1,1,...,1,1,1] in C++11
    std::bitset<8> bs(0xfff0);      // [1,1,1,1,0,0,0,0]

    // string constructor (3)
    std::string bit_string = "110010";
    std::bitset<8> b3(bit_string);       // [0,0,1,1,0,0,1,0]
    std::bitset<8> b4(bit_string, 2);    // [0,0,0,0,0,0,1,0]
    std::bitset<8> b5(bit_string, 2, 3); // [0,0,0,0,0,0,0,1]

    // string constructor using custom zero/one digits (3)
    std::string alpha_bit_string = "aBaaBBaB";
    std::bitset<8> b6(alpha_bit_string, 0, alpha_bit_string.size(),
                      'a', 'B');         // [0,1,0,0,1,1,0,1]

    // char* constructor using custom digits (5)
    std::bitset<8> b7("XXXXYYYY", 8, 'X', 'Y'); // [0,0,0,0,1,1,1,1]

    std::cout <<   "b1: " << b1 << "\nb2: " << b2 << "\nbl: " << bl
              << "\nbs: " << bs << "\nb3: " << b3 << "\nb4: " << b4
              << "\nb5: " << b5 << "\nb6: " << b6 << "\nb7: " << b7 << '\n';
}
```


**Output:**
```
b1: 00000000
b2: 00101010
bl: 0000001111111111111111111111111111111111111111111111111111111111111111
bs: 11110000
b3: 00110010
b4: 00000010
b5: 00000001
b6: 01001101
b7: 00001111
```


## Defect reports


## See also


| cpp/utility/bitset/dsc set | (see dedicated page) |
| cpp/utility/bitset/dsc reset | (see dedicated page) |

