---
title: std::basic_string::compare
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/compare
---


```cpp
dcla|num=1|noexcept=c++11|constexpr=c++20|1=
int compare( const basic_string& str ) const;
dcla|anchor=no|num=2|constexpr=c++20|
int compare( size_type pos1, size_type count1,
const basic_string& str ) const;
dcl rev multi|num=3
|dcl1=
int compare( size_type pos1, size_type count1,
const basic_string& str,
size_type pos2, size_type count2 ) const;
|since2=c++14|notes2=<sup>(constexpr C++20)</sup>|dcl2=
int compare( size_type pos1, size_type count1,
const basic_string& str,
size_type pos2, size_type count2 = npos ) const;
dcla|anchor=no|num=4|constexpr=c++20|
int compare( const CharT* s ) const;
dcla|anchor=no|num=5|constexpr=c++20|
int compare( size_type pos1, size_type count1,
const CharT* s ) const;
dcla|anchor=no|num=6|constexpr=c++20|
int compare( size_type pos1, size_type count1,
const CharT* s, size_type count2 ) const;
dcla|anchor=no|num=7|since=c++17|constexpr=c++20|
template< class StringViewLike >
int compare( const StringViewLike& t ) const noexcept(/* see below */);
dcla|anchor=no|num=8|since=c++17|constexpr=c++20|
template< class StringViewLike >
int compare( size_type pos1, size_type count1,
const StringViewLike& t ) const;
dcla|anchor=no|num=9|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
int compare( size_type pos1, size_type count1,
const StringViewLike& t,
size_type pos2, size_type count2 = npos) const;
```

Compares two character sequences.
1. Compares this string to `str`.
2. Compares a [pos1, pos1 + count1) substring of this string to `str`.
* If `count1 > size() - pos1`, the substring is [pos1, size()).
3. Compares a [pos1, pos1 + count1) substring of this string to a substring [pos2, pos2 + count2) of `str`.
* If `count1 > size() - pos1`, the first substring is [pos1, size()).
* If `count2 > str.size() - pos2`, the second substring is [pos2, str.size()).
4. Compares this string to the null-terminated character sequence beginning at the character pointed to by `s` with length `Traits::length(s)`.
5. Compares a [pos1, pos1 + count1) substring of this string to the null-terminated character sequence beginning at the character pointed to by `s` with length `Traits::length(s)`.
* If `count1 > size() - pos1`, the substring is [pos1, size()).
6. Compares a [pos1, pos1 + count1) substring of this string to the characters in the range [s, s + count2). The characters in [s, s + count2) may include null characters.
* If `count1 > size() - pos1`, the substring is [pos1, size()).
@7-9@ cpp/string/sv hack|plural=yes|
:@7@ compares this string to `sv`;
:@8@ compares a [pos1, pos1 + count1) substring of this string to `sv`, as if by `std::basic_string_view<CharT, Traits>(*this).substr(pos1, count1).compare(sv)`;
:@9@ compares a [pos1, pos1 + count1) substring of this string to a substring [pos2, pos2 + count2) of `sv`, as if by c multi|
std::basic_string_view<CharT, Traits>(*this)|
.substr(pos1, count1).compare(sv.substr(pos2, count2)).
A character sequence consisting of `count1` characters starting at `data1` is compared to a character sequence consisting of `count2` characters starting at `data2` as follows:
* First, calculate the number of characters to compare, as if by `1=size_type rlen = std::min(count1, count2)`.
* Then compare the sequences by calling `Traits::compare(data1, data2, rlen)`. For standard strings this function performs character-by-character lexicographical comparison. If the result is zero (the character sequences are equal so far), then their sizes are compared as follows:


| colspan=2 | Condition |
| Result |
| Return value |
| - |
| colspan=2 style="text-align:left;" | tt | Traits::compare(spar | data1, spar | data2, spar | rlen) < 0 |
| spar | data1 is ''less'' than spar | data2 |
| c | <0 |
| - |
| rowspan=3 | tt | Traits::compare(spar | data1, spar | data2, spar | rlen)  0 |
| spar | size1 < spar | size2 |
| spar | data1 is ''less'' than spar | data2 |
| c | <0 |
| - |
| spar | size1  spar | size2 |
| spar | data1 is ''equal'' to spar | data2 |
| c | 0 |
| - |
| spar | size1 > spar | size2 |
| spar | data1 is ''greater'' than spar | data2 |
| c | >0 |
| - |
| colspan=2 style="text-align:left;" | tt | Traits::compare(spar | data1, spar | data2, spar | rlen) > 0 |
| spar | data1 is ''greater'' than spar | data2 |
| c | >0 |


## Parameters


### Parameters

- `str` - other string to compare to
- `s` - pointer to the character string to compare to
- `count1` - number of characters of this string to compare
- `pos1` - position of the first character in this string to compare
- `count2` - number of characters of the given string to compare
- `pos2` - position of the first character of the given string to compare
- `t` - object (convertible to `std::basic_string_view`) to compare to

## Return value

* Negative value if `*this` appears before the character sequence specified by the arguments, in lexicographical order.
* Zero if both character sequences compare equivalent.
* Positive value if `*this` appears after the character sequence specified by the arguments, in lexicographical order.

## Exceptions

The overloads taking parameters named `pos1` or `pos2` throws `std::out_of_range` if the argument is out of range.
7.
@8,9@ Throws anything thrown by the conversion to `std::basic_string_view`.

## Possible implementation

eq impl
|title1=overload (1)|ver1=1|1=
template<class CharT, class Traits, class Alloc>
int std::basic_string<CharT, Traits, Alloc>::compare
(const std::basic_string& s) const noexcept
{
size_type lhs_sz = size();
size_type rhs_sz = s.size();
int result = traits_type::compare(data(), s.data(), std::min(lhs_sz, rhs_sz));
if (result != 0)
return result;
if (lhs_sz < rhs_sz)
return -1;
if (lhs_sz > rhs_sz)
return 1;
return 0;
}

## Notes

For the situations when three-way comparison is not required, `std::basic_string` provides the usual `relational operators` (`<`, `1=<=`, `1===`, `>`, etc).
By default (with the default `std::char_traits`), this function is not locale-sensitive. See `std::collate::compare` for locale-aware three-way string comparison.

## Example


### Example

```cpp
#include <cassert>
#include <iomanip>
#include <iostream>
#include <string>
#include <string_view>

void print_compare_result(std::string_view str1,
                          std::string_view str2,
                          int compare_result)
{
    if (compare_result < 0)
        std::cout << std::quoted(str1) << " comes before "
                  << std::quoted(str2) << ".\n";
    else if (compare_result > 0)
        std::cout << std::quoted(str2) << " comes before "
                  << std::quoted(str1) << ".\n";
    else
        std::cout << std::quoted(str1) << " and "
                  << std::quoted(str2) << " are the same.\n";
}

int main()
{
    std::string batman{"Batman"};
    std::string superman{"Superman"};
    int compare_result{0};

    // 1) Compare with other string
    compare_result = batman.compare(superman);
    std::cout << "1) ";
    print_compare_result("Batman", "Superman", compare_result);

    // 2) Compare substring with other string
    compare_result = batman.compare(3, 3, superman);
    std::cout << "2) ";
    print_compare_result("man", "Superman", compare_result);

    // 3) Compare substring with other substring
    compare_result = batman.compare(3, 3, superman, 5, 3);
    std::cout << "3) ";
    print_compare_result("man", "man", compare_result);

    // Compare substring with other substring
    // defaulting to end of other string
    assert(compare_result == batman.compare(3, 3, superman, 5));

    // 4) Compare with char pointer
    compare_result = batman.compare("Superman");
    std::cout << "4) ";
    print_compare_result("Batman", "Superman", compare_result);

    // 5) Compare substring with char pointer
    compare_result = batman.compare(3, 3, "Superman");
    std::cout << "5) ";
    print_compare_result("man", "Superman", compare_result);

    // 6) Compare substring with char pointer substring
    compare_result = batman.compare(0, 3, "Superman", 5);
    std::cout << "6) ";
    print_compare_result("Bat", "Super", compare_result);
}
```


**Output:**
```
1) "Batman" comes before "Superman".
2) "Superman" comes before "man".
3) "man" and "man" are the same.
4) "Batman" comes before "Superman".
5) "Superman" comes before "man".
6) "Bat" comes before "Super".
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc operator cmp | (see dedicated page) |
| cpp/string/basic_string/dsc substr | (see dedicated page) |
| cpp/locale/dsc collate | (see dedicated page) |
| cpp/string/byte/dsc strcoll | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/string/basic_string_view/dsc compare | (see dedicated page) |

