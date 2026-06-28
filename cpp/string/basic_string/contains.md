---
title: std::basic_string::contains
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/contains
---


```cpp
dcl|num=1|since=c++23|1=
constexpr bool
contains( std::basic_string_view<CharT,Traits> sv ) const noexcept;
dcl|num=2|since=c++23|1=
constexpr bool
contains( CharT ch ) const noexcept;
dcl|num=3|since=c++23|1=
constexpr bool
contains( const CharT* s ) const;
```

Checks if the string contains the given substring. The substring may be one of the following:
1. A string view `sv` (which may be a result of implicit conversion from another `std::basic_string`).
2. A single character `ch`.
3. A null-terminated character string `s`.
All three overloads are equivalent to `1=return find(x) != npos;`, where `x` is the parameter.

## Parameters


### Parameters

- `sv` - a string view which may be a result of implicit conversion from another `std::basic_string`
- `ch` - a single character
- `s` - a null-terminated character string

## Return value

`true` if the string contains the provided substring, `false` otherwise.

## Notes


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <string_view>
#include <type_traits>

template<typename SubstrType>
void test_substring(const std::string& str, SubstrType subs)
{
    constexpr char delim = std::is_scalar_v<SubstrType> ? '\'' : '\"';
    std::cout << std::quoted(str)
              << (str.contains(subs) ? " contains "
                                     : " does not contain ")
              << std::quoted(std::string{subs}, delim) << '\n';
}

int main()
{
    using namespace std::literals;

    auto helloWorld = "hello world"s;

    test_substring(helloWorld, "hello"sv);
    test_substring(helloWorld, "goodbye"sv);
    test_substring(helloWorld, 'w');
    test_substring(helloWorld, 'x');
}
```


**Output:**
```
"hello world" contains "hello"
"hello world" does not contain "goodbye"
"hello world" contains 'w'
"hello world" does not contain 'x'
```


## See also


| cpp/string/basic_string/dsc starts_with | (see dedicated page) |
| cpp/string/basic_string/dsc ends_with | (see dedicated page) |
| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string/dsc substr | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

