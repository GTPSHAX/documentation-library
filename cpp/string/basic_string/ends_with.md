---
title: std::basic_string::ends_with
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/ends_with
---


```cpp
dcl|num=1|since=c++20|1=
constexpr bool
ends_with( std::basic_string_view<CharT, Traits> sv ) const noexcept;
dcl|num=2|since=c++20|1=
constexpr bool
ends_with( CharT ch ) const noexcept;
dcl|num=3|since=c++20|1=
constexpr bool
ends_with( const CharT* s ) const;
```

Checks if the string ends with the given suffix. The suffix may be one of the following:
1. A string view `sv` (which may be a result of implicit conversion from another `std::basic_string`).
2. A single character `ch`.
3. A null-terminated character string `s`.
All three overloads effectively return `std::basic_string_view<CharT, Traits>(data(), size()).ends_with(x)`, where `x` is the parameter.

## Parameters


### Parameters

- `sv` - a string view which may be a result of implicit conversion from another `std::basic_string`
- `ch` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string ends with the provided suffix, `false` otherwise.

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
        && str.ends_with("C++20!"sv)  // (1)
        && !str.ends_with("c++20!"sv) // (1)
        && str.ends_with("C++20!"s)   // (1) implicit conversion string to string_view
        && !str.ends_with("c++20!"s)  // (1) implicit conversion string to string_view
        && str.ends_with('!')         // (2)
        && !str.ends_with('?')        // (2)
        && str.ends_with("C++20!")    // (3)
        && !str.ends_with("c++20!")   // (3)
    );
}
```


## See also


| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string_view/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc contains | (see dedicated page) |
| cpp/string/basic_string_view/dsc contains | (see dedicated page) |
| cpp/string/basic_string/dsc compare | (see dedicated page) |
| cpp/string/basic_string/dsc substr | (see dedicated page) |

