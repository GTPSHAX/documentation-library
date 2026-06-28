---
title: std::formatted_size
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/formatted_size
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class... Args >
std::size_t formatted_size( std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++20|1=
template< class... Args >
std::size_t formatted_size( std::wformat_string<Args...> fmt, Args&&... args );
dcl|num=3|since=c++20|1=
template< class... Args >
std::size_t formatted_size( const std::locale& loc,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=4|since=c++20|1=
template< class... Args >
std::size_t formatted_size( const std::locale& loc,
std::wformat_string<Args...> fmt, Args&&... args );
```

Determine the total number of characters in the formatted string by formatting `args` according to the format string `fmt`. If present, `loc` is used for locale-specific formatting.
The behavior is undefined if `std::formatter<std::remove_cvref_t<Ti>, CharT>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args`.

## Parameters


### Parameters

- `fmt` - 
- `args...` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

The total number of characters in the formatted string.

## Exceptions

Propagates any exception thrown by formatter.

## Example


### Example

```cpp
#include <format>
#include <iomanip>
#include <iostream>
#include <string_view>
#include <vector>

int main()
{
    using namespace std::literals::string_view_literals;

    constexpr auto fmt_str{"Hubble's H{0} {1} {2:*^4} miles/sec/mpc."sv};
    constexpr auto sub_zero{"\N{SUBSCRIPT ZERO}"sv}; // "₀" or {0342, 130, 128}
    constexpr auto aprox_equ{"\N{APPROXIMATELY EQUAL TO}"sv}; // "≅" or {0342, 137, 133}
    constexpr int Ho{42}; // H₀

    const auto min_buffer_size{std::formatted_size(fmt_str, sub_zero, aprox_equ, Ho)};
    std::cout << "Min buffer size = " << min_buffer_size << '\n';

    // Use std::vector as dynamic buffer. The buffer does not include the trailing '\0'.
    std::vector<char> buffer(min_buffer_size);

    std::format_to_n(buffer.data(), buffer.size(), fmt_str, sub_zero, aprox_equ, Ho);
    std::cout << "Buffer: "
              << std::quoted(std::string_view{buffer.data(), min_buffer_size})
              << '\n';

    // Print the buffer directly after adding the trailing '\0'.
    buffer.push_back('\0');
    std::cout << "Buffer: " << std::quoted(buffer.data()) << '\n';
}
```


**Output:**
```
Min buffer size = 37
Buffer: "Hubble's H₀ ≅ *42* miles/sec/mpc."
Buffer: "Hubble's H₀ ≅ *42* miles/sec/mpc."
```


## Defect reports


## See also


| cpp/utility/format/dsc format_to | (see dedicated page) |
| cpp/utility/format/dsc format_to_n | (see dedicated page) |

