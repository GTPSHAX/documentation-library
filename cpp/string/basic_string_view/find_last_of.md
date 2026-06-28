---
title: std::basic_string_view::find_last_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/find_last_of
---


```cpp
dcl|num=1|since=c++17|1=
constexpr size_type
find_last_of( basic_string_view v, size_type pos = npos ) const noexcept;
dcl|num=2|since=c++17|1=
constexpr size_type
find_last_of( CharT ch, size_type pos = npos ) const noexcept;
dcl|num=3|since=c++17|
constexpr size_type
find_last_of( const CharT* s, size_type pos, size_type count ) const;
dcl|num=4|since=c++17|1=
constexpr size_type
find_last_of( const CharT* s, size_type pos = npos ) const;
```

Finds the last character equal to one of characters in the given character sequence. Exact search algorithm is not specified. The search considers only the interval . If the character is not present in the interval, `npos` will be returned.
1. Finds the last occurence of any of the characters of `v` in this view, ending at position `pos`.
2. Equivalent to `find_last_of(basic_string_view(std::addressof(ch), 1), pos)`.
3. Equivalent to `find_last_of(basic_string_view(s, count), pos)`.
4. Equivalent to `find_last_of(basic_string_view(s), pos)`.

## Parameters


### Parameters

- `v` - view to search for
- `pos` - position at which the search is to finish
- `count` - length of the string of characters to search for
- `s` - pointer to a string of characters to search for
- `ch` - character to search for

## Return value

Position of the last occurrence of any character of the substring, or `npos` if no such character is found.

## Complexity

O(`size()` * v.`size()`) at worst.

## Example


### Example

```cpp
#include <string_view>

using namespace std::literals;
constexpr auto N = std::string_view::npos;

static_assert(
    5 == "delete"sv.find_last_of("cdef"sv) &&
      //       └────────────────────┘
    N == "double"sv.find_last_of("fghi"sv) &&
      //
    0 == "else"sv.find_last_of("bcde"sv, 2 /* pos [0..2]: "els" */) &&
      //  └────────────────────────┘
    N == "explicit"sv.find_last_of("abcd"sv, 4 /* pos [0..4]: "expli" */) &&
      //
    3 == "extern"sv.find_last_of('e') &&
      //     └────────────────────┘
    N == "false"sv.find_last_of('x') &&
      //
    0 == "inline"sv.find_last_of('i', 2 /* pos [0..2]: "inl" */) &&
      //  └───────────────────────┘
    N == "mutable"sv.find_last_of('a', 2 /* pos [0..2]: "mut" */) &&
      //
    3 == "namespace"sv.find_last_of("cdef", 3 /* pos [0..3]: "name" */, 3 /* "cde" */) &&
      //     └─────────────────────────┘
    N == "namespace"sv.find_last_of("cdef", 3 /* pos [0..3]: "name" */, 2 /* "cd" */)
);

int main() {}
```


## See also


| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc rfind | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |

