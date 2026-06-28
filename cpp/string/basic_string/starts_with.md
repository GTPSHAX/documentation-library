---
title: std::basic_string::starts_with
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/starts_with
---


```cpp
dcl|num=1|since=c++20|1=
constexpr bool
starts_with( std::basic_string_view<CharT,Traits> sv ) const noexcept;
dcl|num=2|since=c++20|1=
constexpr bool
starts_with( CharT ch ) const noexcept;
dcl|num=3|since=c++20|1=
constexpr bool
starts_with( const CharT* s ) const;
```

Checks if the string begins with the given prefix. The prefix may be one of the following:
1. A string view `sv` (which may be a result of implicit conversion from another `std::basic_string`).
2. A single character `ch`.
3. A null-terminated character string `s`.
All three overloads effectively return `std::basic_string_view<CharT, Traits>(data(), size()).starts_with(x)`, where `x` is the parameter.

## Parameters


### Parameters

- `sv` - a string view which may be a result of implicit conversion from another `std::basic_string`
- `ch` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string begins with the provided prefix, `false` otherwise.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string>
#include <string_view>

int main()
{
    using namespace std::literals;

    const auto str = "Hello, C++20!"s;

    assert
    (""
        && str.starts_with("He"sv)  // (1)
        && !str.starts_with("he"sv) // (1)
        && str.starts_with("He"s)   // (1) implicit conversion string to string_view
        && !str.starts_with("he"s)  // (1) implicit conversion string to string_view
        && str.starts_with('H')     // (2)
        && !str.starts_with('h')    // (2)
        && str.starts_with("He")    // (3)
        && !str.starts_with("he")   // (3)
    );
}
```


## See also


| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc contains | (see dedicated page) |
| cpp/string/basic_string/dsc compare | (see dedicated page) |
| cpp/string/basic_string/dsc substr | (see dedicated page) |

