---
title: std::basic_string_view::starts_with
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/starts_with
---


```cpp
dcl|num=1|since=c++20|1=
constexpr bool starts_with( basic_string_view sv ) const noexcept;
dcl|num=2|since=c++20|1=
constexpr bool starts_with( CharT ch ) const noexcept;
dcl|num=3|since=c++20|1=
constexpr bool starts_with( const CharT* s ) const;
```

Checks if the string view begins with the given prefix, where
1. the prefix is a string view. Effectively returns `1=basic_string_view(data(), std::min(size(), sv.size())) == sv`.
2. the prefix is a single character. Effectively returns `1=!empty() && Traits::eq(front(), ch)`.
3. the prefix is a null-terminated character string. Effectively returns `1=starts_with(basic_string_view(s))`.

## Parameters


### Parameters

- `sv` - a string view which may be a result of implicit conversion from `std::basic_string`
- `ch` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string view begins with the provided prefix, `false` otherwise.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string_view>

int main()
{
    using namespace std::literals;

    assert
    (""
        // (1) starts_with( basic_string_view )
        && "https://cppreference.com"sv.starts_with("http"sv) == true
        && "https://cppreference.com"sv.starts_with("ftp"sv) == false

        // (2) starts_with( CharT )
        && "C++20"sv.starts_with('C') == true
        && "C++20"sv.starts_with('J') == false

        // (3) starts_with( const CharT* )
        && std::string_view("string_view").starts_with("string") == true
        && std::string_view("string_view").starts_with("String") == false
    );
}
```


## See also


| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc compare | (see dedicated page) |

