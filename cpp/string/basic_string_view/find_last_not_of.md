---
title: std::basic_string_view::find_last_not_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/find_last_not_of
---


```cpp
dcl|num=1|since=c++17|1=
constexpr size_type
find_last_not_of( basic_string_view v, size_type pos = npos ) const noexcept;
dcl|num=2|since=c++17|1=
constexpr size_type
find_last_not_of( CharT ch, size_type pos = npos ) const noexcept;
dcl|num=3|since=c++17|
constexpr size_type
find_last_not_of( const CharT* s, size_type pos, size_type count ) const;
dcl|num=4|since=c++17|1=
constexpr size_type
find_last_not_of( const CharT* s, size_type pos = npos ) const;
```

Finds the last character not equal to any of the characters in the given character sequence. The search considers only the interval .
1. Finds the last character not equal to any of the characters of `v` in this view, starting at position `pos`.
2. Equivalent to `find_last_not_of(basic_string_view(std::addressof(ch), 1), pos)`.
3. Equivalent to `find_last_not_of(basic_string_view(s, count), pos)`.
4. Equivalent to `find_last_not_of(basic_string_view(s), pos)`.

## Parameters


### Parameters

- `v` - view to search for
- `pos` - position at which to start the search
- `count` - length of the string of characters to compare
- `s` - pointer to a string of characters to compare
- `ch` - character to compare

## Return value

Position of the last character not equal to any of the characters in the given string, or `npos` if no such character is found.

## Complexity

O(`size()`` * v.``size()`) at worst.

## Example


## See also


| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc rfind | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |

