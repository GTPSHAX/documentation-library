---
title: std::expected::value
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/value
---


```cpp
dcl|num=1|since=c++23|
constexpr T& value() &;
dcl|num=2|since=c++23|
constexpr const T& value() const&;
dcl|num=3|since=c++23|
constexpr T&& value() &&;
dcl|num=4|since=c++23|
constexpr const T&& value() const&&;
dcla|num=5|since=c++23|
constexpr void value() const&;
dcl|num=6|since=c++23|
constexpr void value() &&;
```

If `*this` contains an expected value, returns a reference to the contained value. Returns nothing for `void` partial specialization.
Otherwise, throws an exception of type `std::bad_expected_access<std::decay_t<E>>` that contains a copy of .
@1,2@ If `std::is_copy_constructible_v<E>` is `false`, the program is ill-formed.
@3,4@ If `std::is_copy_constructible_v<E>` or `std::is_constructible_v<E, decltype(std::move(error()))>` is `false`, the program is ill-formed.
5. If `std::is_copy_constructible_v<E>` is `false`, the program is ill-formed.
6. If `std::is_move_constructible_v<E>` is `false`, the program is ill-formed.

## Return value

@1,2@
@3,4@

## Exceptions

@1,2,5@ Throws `std::bad_expected_access(std::as_const(error()))` if `*this` contains an unexpected value.
@3,4,6@ Throws `std::bad_expected_access(std::move(error()))` if `*this` contains an unexpected value.

## Example


### Example

```cpp
#include <charconv>
#include <concepts>
#include <expected>
#include <print>
#include <string>
#include <string_view>
#include <system_error>
#include <utility>

template<std::integral Int = int>
constexpr std::expected<Int, std::errc> to_int(std::string_view str)
{
    Int value{};
    const auto [_, ec] = std::from_chars(str.data(), str.data() + str.size(), value);
    if (ec == std::errc())
        return value;
    return std::unexpected{ec};
}

int main()
{
    try
    {
        auto result = to_int("42"); // returns std::expected{42}
        std::println("{}", result.value()); // prints 42
        result = to_int("not a number"); // returns expected{unexpected{errc}<!-- -->}
        [[maybe_unused]] int x_x = result.value(); // throws
    }
    catch(const std::bad_expected_access<std::errc>& ex)
    {
        const std::errc ec{ex.error()};
        std::println("{}: {}", ex.what(), std::make_error_code(ec).message());
    }
}
```


**Output:**
```
42
bad access to std::expected without expected value: Invalid argument
```


## Defect reports


## See also


| cpp/utility/expected/dsc value_or | (see dedicated page) |
| cpp/utility/expected/dsc operator* | (see dedicated page) |
| cpp/utility/expected/dsc error | (see dedicated page) |
| cpp/utility/expected/dsc bad_expected_access | (see dedicated page) |

