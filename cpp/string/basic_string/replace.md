---
title: std::basic_string::replace
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/replace
---


```cpp
|num=1|
basic_string& replace( size_type pos, size_type count,
const basic_string& str );
|num=2|
basic_string& replace( const_iterator first, const_iterator last,
const basic_string& str );
dcl rev multi|num=3
|dcl1=
basic_string& replace( size_type pos, size_type count,
const basic_string& str,
size_type pos2, size_type count2 );
|since2=c++14|notes2=<sup>(constexpr C++20)</sup>|dcl2=
basic_string& replace( size_type pos, size_type count,
const basic_string& str,
size_type pos2, size_type count2 = npos );
|num=4|
basic_string& replace( size_type pos, size_type count,
const CharT* cstr, size_type count2 );
|num=5|
basic_string& replace( const_iterator first, const_iterator last,
const CharT* cstr, size_type count2 );
|num=6|
basic_string& replace( size_type pos, size_type count,
const CharT* cstr );
|num=7|
basic_string& replace( const_iterator first, const_iterator last,
const CharT* cstr );
|num=8|
basic_string& replace( size_type pos, size_type count,
size_type count2, CharT ch );
|num=9|
basic_string& replace( const_iterator first, const_iterator last,
size_type count2, CharT ch );
|num=10|
template< class InputIt >
basic_string& replace( const_iterator first, const_iterator last,
InputIt first2, InputIt last2 );
|num=11|
basic_string& replace( const_iterator first, const_iterator last,
std::initializer_list<CharT> ilist );
|num=12|
template< class StringViewLike >
basic_string& replace( size_type pos, size_type count,
const StringViewLike& t );
|num=13|
template< class StringViewLike >
basic_string& replace( const_iterator first, const_iterator last,
const StringViewLike& t );
|num=14|1=
template< class StringViewLike >
basic_string& replace( size_type pos, size_type count,
const StringViewLike& t,
size_type pos2, size_type count2 = npos );
```

Replaces the characters in the range [begin() + pos, begin() + std::min(pos + count, size())) or [first, last) with given characters.
@1,2@ Those characters are replaced with `str`.
3. Those characters are replaced with a substring [pos2, std::min(pos2 + count2, str.size())) of `str`.
@4,5@ Those characters are replaced with the characters in the range [cstr, cstr + count2).
@@ If [cstr, cstr + count2) is not a valid range, the behavior is undefined.
@6,7@ Those characters are replaced with the characters in the range [cstr, cstr + Traits::length(cstr)).
@8,9@ Those characters are replaced with `count2` copies of `ch`.
10. Those characters are replaced with the characters in the range [first2, last2) as if by `replace(first, last, basic_string(first2, last2, get_allocator()))`.
11. Those characters are replaced with the characters in `ilist`.
@12,13@
14.
If [begin(), first) or [first, last) is not a valid range, the behavior is undefined.

## Parameters


### Parameters

- `pos` - start of the substring that is going to be replaced
- `count` - length of the substring that is going to be replaced
- `first, last` - range of characters that is going to be replaced
- `str` - string to use for replacement
- `pos2` - start of the substring to replace with
- `count2` - number of characters to replace with
- `cstr` - pointer to the character string to use for replacement
- `ch` - character value to use for replacement
- `first2, last2` - range of characters to use for replacement
- `ilist` - initializer list with the characters to use for replacement
- `t` - object (convertible to `std::basic_string_view`) with the characters to use for replacement

**Type requirements:**

- `InputIt`

## Return value

`*this`.

## Exceptions

1. Throws `std::out_of_range` if `pos > size()`.
3. Throws `std::out_of_range` if `pos > size()` or `pos2 > str.size()`.
@4,6,8@ Throws `std::out_of_range` if `pos > size()`.
@12,14@ Throws `std::out_of_range` if `pos > size()`.

## Example


## See also


| cpp/string/basic_string/dsc replace_with_range | (see dedicated page) |
| cpp/regex/dsc regex_replace | (see dedicated page) |
| cpp/algorithm/dsc replace | (see dedicated page) |

