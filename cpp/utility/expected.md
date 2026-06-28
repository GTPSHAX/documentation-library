---
title: std::expected
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected
---


```cpp
**Header:** `<`expected`>`
dcl|num=1|since=c++23|
template< class T, class E >
class expected;
dcl|num=2|since=c++23|
template< class T, class E >
requires std::is_void_v<T>
class expected<T, E>;
```

The class template `std::expected` provides a way to represent either of two values: an ''expected'' value of type `T`, or an ''unexpected'' value of type `E`. `expected` is never valueless.
1. The main template. Contains the expected or unexpected value within its own storage, which is nested within the `expected` object.
2. The `void` partial specialization. Represents an expected `void` value or contains an unexpected value. If it contains an unexpected value, it is nested within the `expected` object.
A program is ill-formed if it instantiates an `expected` with a reference type, a function type, or a specialization of . In addition, `T` must not be `std::in_place_t` or .

## Template parameters


### Parameters

- `T` - the type of the expected value. The type must either be (possibly cv-qualified) `void`, or meet the *Destructible* requirements (in particular, array and reference types are not allowed).
- `E` - the type of the unexpected value. The type must meet the *Destructible* requirements, and must be a valid template argument for `cpp/utility/expected/unexpected|std::unexpected` (in particular, arrays, non-object types, and cv-qualified types are not allowed).

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member templates


| Item | Description |
|------|-------------|
| **Template** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/utility/expected/dsc constructor | (see dedicated page) |
| cpp/utility/expected/dsc destructor | (see dedicated page) |
| cpp/utility/expected/dsc operator{{= | (see dedicated page) |

#### Observers

| cpp/utility/expected/dsc operator* | (see dedicated page) |
| cpp/utility/expected/dsc operator bool | (see dedicated page) |
| cpp/utility/expected/dsc value | (see dedicated page) |
| cpp/utility/expected/dsc error | (see dedicated page) |
| cpp/utility/expected/dsc value_or | (see dedicated page) |
| cpp/utility/expected/dsc error_or | (see dedicated page) |

#### Monadic operations

| cpp/utility/expected/dsc and_then | (see dedicated page) |
| cpp/utility/expected/dsc transform | (see dedicated page) |
| cpp/utility/expected/dsc or_else | (see dedicated page) |
| cpp/utility/expected/dsc transform_error | (see dedicated page) |

#### Modifiers

| cpp/utility/expected/dsc emplace | (see dedicated page) |
| cpp/utility/expected/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/utility/expected/dsc operator cmp | (see dedicated page) |
| cpp/utility/expected/dsc swap2 | (see dedicated page) |


## Helper classes


| cpp/utility/expected/dsc unexpected | (see dedicated page) |
| cpp/utility/expected/dsc bad_expected_access | (see dedicated page) |
| cpp/utility/expected/dsc unexpect_t | (see dedicated page) |


## Notes

Types with the same functionality are called [https://doc.rust-lang.org/std/result/enum.Result.html `Result`] in Rust and [https://hackage.haskell.org/package/base-4.17.0.0/docs/Data-Either.html `Either`] in Haskell.

## Example


### Example

```cpp
#include <cmath>
#include <expected>
#include <iomanip>
#include <iostream>
#include <string_view>

enum class parse_error
{
    invalid_input,
    overflow
};

auto parse_number(std::string_view& str) -> std::expected<double, parse_error>
{
    const char* begin = str.data();
    char* end;
    double retval = std::strtod(begin, &end);

    if (begin == end)
        return std::unexpected(parse_error::invalid_input);
    else if (std::isinf(retval))
        return std::unexpected(parse_error::overflow);

    str.remove_prefix(end - begin);
    return retval;
}

int main()
{
    auto process = [](std::string_view str)
    {
        std::cout << "str: " << std::quoted(str) << ", ";
        if (const auto num = parse_number(str); num.has_value())
            std::cout << "value: " << *num << '\n';
            // If num did not have a value, dereferencing num
            // would cause an undefined behavior, and
            // num.value() would throw std::bad_expected_access.
            // num.value_or(123) uses specified default value 123.
        else if (num.error() == parse_error::invalid_input)
            std::cout << "error: invalid input\n";
        else if (num.error() == parse_error::overflow)
            std::cout << "error: overflow\n";
        else
            std::cout << "unexpected!\n"; // or invoke std::unreachable();
    };

    for (auto src : {"42", "42abc", "meow", "inf"})
        process(src);
}
```


**Output:**
```
str: "42", value: 42
str: "42abc", value: 42
str: "meow", error: invalid input
str: "inf", error: overflow
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4141 | C++23 | the requirement of storage<br>allocation was confusing | the contained object must be<br>nested within the tt |


## References


## See also


| cpp/utility/dsc variant | (see dedicated page) |
| cpp/utility/dsc optional | (see dedicated page) |

