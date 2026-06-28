---
title: std::basic_string_view::find
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/find
---


```cpp
dcl|num=1|since=c++17|1=
constexpr size_type find( basic_string_view v, size_type pos = 0 ) const noexcept;
dcl|num=2|since=c++17|1=
constexpr size_type find( CharT ch, size_type pos = 0 ) const noexcept;
dcl|num=3|since=c++17|
constexpr size_type find( const CharT* s, size_type pos, size_type count ) const;
dcl|num=4|since=c++17|1=
constexpr size_type find( const CharT* s, size_type pos = 0 ) const;
```

Finds the first substring equal to the given character sequence.
1. Finds the first occurence of `v` in this view, starting at position `pos`.
2. Equivalent to `find(basic_string_view(std::addressof(ch), 1), pos)`.
3. Equivalent to `find(basic_string_view(s, count), pos)`.
4. Equivalent to `find(basic_string_view(s), pos)`.

## Parameters


### Parameters

- `v` - view to search for
- `pos` - position at which to start the search
- `count` - length of substring to search for
- `s` - pointer to a character string to search for
- `ch` - character to search for

## Return value

Position of the first character of the found substring, or `npos` if no such substring is found.

## Complexity

O(`size()` * v.`size()`) at worst.

## Example


## See also


| cpp/string/basic_string_view/dsc rfind | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find | (see dedicated page) |

