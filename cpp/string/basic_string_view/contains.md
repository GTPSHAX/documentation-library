---
title: std::basic_string_view::contains
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/contains
---


```cpp
dcl|num=1|since=c++23|1=
constexpr bool contains( basic_string_view sv ) const noexcept;
dcl|num=2|since=c++23|1=
constexpr bool contains( CharT c ) const noexcept;
dcl|num=3|since=c++23|1=
constexpr bool contains( const CharT* s ) const;
```

Checks if the string view contains the given substring, where
1. the substring is a string view.
2. the substring is a single character.
3. the substring is a null-terminated character string.
All three overloads are equivalent to `1=return find(x) != npos;`, where `x` is the parameter.

## Parameters


### Parameters

- `sv` - a string view
- `c` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string view contains the provided substring, `false` otherwise.

## Notes


## Example


### Example

```cpp
#include <string_view>
using namespace std::literals;

static_assert
(
    // bool contains(basic_string_view x) const noexcept;
    "https://cppreference.com"sv.contains("cpp"sv) == true and
    "https://cppreference.com"sv.contains("php"sv) == false and

    // bool contains(CharT x) const noexcept;
    "C++23"sv.contains('+') == true and
    "C++23"sv.contains('-') == false and

    // bool contains(const CharT* x) const;
    std::string_view("basic_string_view").contains("string") == true and
    std::string_view("basic_string_view").contains("String") == false
);

int main() {}
```


## See also


| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc substr | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |

