---
title: std::expected::error
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/error
---


```cpp
dcl|num=1|since=c++23|
constexpr const E& error() const& noexcept;
dcl|num=2|since=c++23|
constexpr E& error() & noexcept;
dcl|num=3|since=c++23|
constexpr const E&& error() const&& noexcept;
dcl|num=4|since=c++23|
constexpr E&& error() && noexcept;
```

Accesses the unexpected value contained in `*this`.

## Return value

@1,2@
@3,4@

## Example


### Example

```cpp
#include <charconv>
#include <concepts>
#include <expected>
#include <iostream>
#include <string>
#include <string_view>
#include <system_error>

// Try to convert string to integer. If success,
// return integer, otherwise return an error code.
template<std::integral Int = int>
constexpr std::expected<Int, std::errc> to_int(std::string_view str)
{
    Int value{};
    const auto [_, ec] = std::from_chars(str.data(), str.data() + str.size(), value);
    if (ec == std::errc())
        return value;
    return std::unexpected{ec};
}

// Convert string to integer. If success, print the integer and return nothing
// (partial specialization: expected<void, E>). Otherwise, return an error string.
std::expected<void, std::string> print_as_int(std::string_view str)
{
    if (auto result = to_int(str))
    {
        std::cout << *result << '\n';
        return {};
    }
    else
        return std::unexpected{std::make_error_code(result.error()).message()};
}

int main()
{
    if (const auto result{print_as_int("1729")}; not result)
        std::cout << result.error() << '\n'; // skipped

    if (const auto result{print_as_int("NaN")}; not result)
        std::cout << result.error() << '\n'; // prints error
}
```


**Output:**
```
1729
Invalid argument
```


## See also


| cpp/utility/expected/dsc error_or | (see dedicated page) |
| cpp/utility/expected/dsc operator* | (see dedicated page) |
| cpp/utility/expected/dsc value | (see dedicated page) |
| cpp/utility/expected/dsc operator bool | (see dedicated page) |

