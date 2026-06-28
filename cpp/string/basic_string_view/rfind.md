---
title: std::basic_string_view::rfind
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/rfind
---


```cpp
dcl|num=1|since=c++17|1=
constexpr size_type rfind( basic_string_view v, size_type pos = npos ) const noexcept;
dcl|num=2|since=c++17|1=
constexpr size_type rfind( CharT ch, size_type pos = npos ) const noexcept;
dcl|num=3|since=c++17|1=
constexpr size_type rfind( const CharT* s, size_type pos, size_type count ) const;
dcl|num=4|since=c++17|1=
constexpr size_type rfind( const CharT* s, size_type pos = npos ) const;
```

Finds the last substring that is equal to the given character sequence. The search begins at `pos` and proceeds towards the beginning (thus, the found substring, if any, cannot begin in a position following `pos`). If `npos` or any value not smaller than  is passed as `pos`, the whole string will be searched.
1. Finds the last occurrence of `v` in this view, starting at position `pos`.
2. Equivalent to `rfind(basic_string_view(std::addressof(ch), 1), pos)`.
3. Equivalent to `rfind(basic_string_view(s, count), pos)`.
4. Equivalent to `rfind(basic_string_view(s), pos)`.

## Parameters


### Parameters

- `v` - view to search for
- `pos` - position at which to start the search
- `count` - length of substring to search for
- `s` - pointer to a character string to search for
- `ch` - character to search for

## Return value

Position of the first character of the found substring or `npos` if no such substring is found.

## Complexity

O(`size()` * v.`size()`) at worst.

## Example


### Example

```cpp
#include <string_view>

int main()
{
    using namespace std::literals;
    constexpr auto N = std::string_view::npos;

    static_assert(true
        && (6 == "AB AB AB"sv.rfind("AB"))
        && (6 == "AB AB AB"sv.rfind("ABCD", N, 2))
        && (3 == "AB AB AB"sv.rfind("AB", 5))
        && (0 == "AB CD EF"sv.rfind("AB", 0))
        && (2 == "B AB AB "sv.rfind("AB", 2))
        && (N == "B AB AB "sv.rfind("AB", 1))
        && (5 == "B AB AB "sv.rfind('A'))
        && (4 == "AB AB AB"sv.rfind('B', 4))
        && (N == "AB AB AB"sv.rfind('C'))
    );
}
```


## See also


| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |

