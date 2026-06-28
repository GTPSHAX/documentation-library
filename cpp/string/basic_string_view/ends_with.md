---
title: std::basic_string_view::ends_with
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/ends_with
---


```cpp
dcl|num=1|since=c++20|1=
constexpr bool ends_with( basic_string_view sv ) const noexcept;
dcl|num=2|since=c++20|1=
constexpr bool ends_with( CharT ch ) const noexcept;
dcl|num=3|since=c++20|1=
constexpr bool ends_with( const CharT* s ) const;
```

Checks if the string view ends with the given suffix, where
1. the suffix is a string view. Effectively returns `1=size() >= sv.size() && compare(size() - sv.size(), npos, sv) == 0`.
2. the suffix is a single character. Effectively returns `1=!empty() && Traits::eq(back(), ch)`.
3. the suffix is a null-terminated character string. Effectively returns `1=ends_with(basic_string_view(s))`.

## Parameters


### Parameters

- `sv` - a string view which may be a result of implicit conversion from `std::basic_string`
- `ch` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string view ends with the provided suffix, `false` otherwise.

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
        // (1) ends_with( basic_string_view sv )
        && std::string_view("https://cppreference.com").ends_with(".com"sv) == true
        && std::string_view("https://cppreference.com").ends_with(".org"sv) == false

        // (2) ends_with( CharT c )
        && std::string_view("C++20").ends_with('0') == true
        && std::string_view("C++20").ends_with('3') == false

        // (3) ends_with( const CharT* s )
        && std::string_view("string_view").ends_with("view") == true
        && std::string_view("string_view").ends_with("View") == false
    );
}
```


## See also


| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc compare | (see dedicated page) |

