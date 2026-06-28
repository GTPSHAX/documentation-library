---
title: std::to_chars
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/to_chars
---


```cpp
**Header:** `<`charconv`>`
dcla|num=1|since=c++17|notes=<sup>(constexpr C++23)</sup>|1=
std::to_chars_result
to_chars( char* first, char* last,
/* integer-type */ value, int base = 10 );
dcl|num=2|since=c++17|1=
std::to_chars_result
to_chars( char*, char*, bool, int = 10 ) = delete;
dcl|num=3|since=c++17|
std::to_chars_result
to_chars( char* first, char* last, /* floating-point-type */ value );
dcl|num=4|since=c++17|
std::to_chars_result
to_chars( char* first, char* last, /* floating-point-type */ value,
std::chars_format fmt );
dcl|num=5|since=c++17|
std::to_chars_result
to_chars( char* first, char* last, /* floating-point-type */ value,
std::chars_format fmt, int precision );
```

Converts `value` into a character string by successively filling the range [first, last), where [first, last) is required to be a valid range.
1. Integer formatters: `value` is converted to a string of digits in the given `base` (with no redundant leading zeroes). Digits in the range `10..35` (inclusive) are represented as lowercase characters `a..z`. If value is less than zero, the representation starts with a minus sign. The library provides overloads for all<sup>(since C++23)</sup>  cv-unqualified signed and unsigned integer types and for the type `char` as the type of the parameter `value`.
2. Overload for `bool` is deleted. `std::to_chars` rejects argument of type `bool` because the result would be `"0"`/`"1"` but not `"false"`/`"true"` if it is permitted.
3. `value` is converted to a string as if by `std::printf` in the default ("C") locale. The conversion specifier is `f` or `e` (resolving in favor of `f` in case of a tie), chosen according to the requirement for a shortest representation: the string representation consists of the smallest number of characters such that there is at least one digit before the radix point (if present) and parsing the representation using the corresponding  function recovers value exactly. If there are several such representations, one with the smallest difference to `value` is chosen, resolving any remaining ties using rounding according to `std::round_to_nearest`. The library provides overloads for all cv-unqualified <sup>(until C++23)</sup> standard floating-point types as the type of the parameter `value`.
4. Same as , but the conversion specified for the as-if printf is `f` if `fmt` is `cpp/utility/chars_format|std::chars_format::fixed`, `e` if `fmt` is `cpp/utility/chars_format|std::chars_format::scientific`, `a` (but without leading "0x" in the result) if `fmt` is `cpp/utility/chars_format|std::chars_format::hex`, and `g` if `fmt` is `cpp/utility/chars_format|chars_format::general`. The library provides overloads for all cv-unqualified <sup>(until C++23)</sup> standard floating-point types as the type of the parameter `value`.
5. Same as , except the precision is specified by the parameter `precision` rather than by the shortest representation requirement. The library provides overloads for all cv-unqualified <sup>(until C++23)</sup> standard floating-point types as the type of the parameter `value`.

## Parameters


### Parameters

- `first, last` - character range to write to
- `value` - the value to convert to its string representation
- `base` - integer base to use: a value between 2 and 36 (inclusive).
- `fmt` - floating-point formatting to use, a bitmask of type 
- `precision` - floating-point precision to use

## Return value

On success, returns a value of type  such that `ec` equals value-initialized `std::errc` and `ptr` is the one-past-the-end pointer of the characters written. Note that the string is ''not'' NUL-terminated.
On error, returns a value of type  holding `std::errc::value_too_large` in `ec`, a copy of the value `last` in `ptr`, and leaves the contents of the range [first, last) in unspecified state.

## Exceptions

Throws nothing.

## Notes

Unlike other formatting functions in C++ and C libraries, `std::to_chars` is locale-independent, non-allocating, and non-throwing. Only a small subset of formatting policies used by other libraries (such as `std::sprintf`) is provided. This is intended to allow the fastest possible implementation that is useful in common high-throughput contexts such as text-based interchange ([JSON](https://en.wikipedia.org/wiki/JSON) or [XML](https://en.wikipedia.org/wiki/XML)).
The guarantee that  can recover every floating-point value formatted by `std::to_chars` exactly is only provided if both functions are from the same implementation.
It is required to explicitly cast a `bool` value to another integer type if it is wanted to format the value as `"0"`/`"1"`.

## Example


### Example

```cpp
#include <charconv>
#include <iomanip>
#include <iostream>
#include <string_view>
#include <system_error>

void show_to_chars(auto... format_args)
{
    const size_t buf_size = 10;
    char buf[buf_size]{};
    std::to_chars_result result = std::to_chars(buf, buf + buf_size, format_args...);

    if (result.ec != std::errc())
        std::cout << std::make_error_code(result.ec).message() << '\n';
    else
    {
        std::string_view str(buf, result.ptr - buf);
        std::cout << std::quoted(str) << '\n';
    }
}

int main()
{
    show_to_chars(42);
    show_to_chars(+3.14159F);
    show_to_chars(-3.14159, std::chars_format::fixed);
    show_to_chars(-3.14159, std::chars_format::scientific, 3);
    show_to_chars(3.1415926535, std::chars_format::fixed, 10);
}
```


**Output:**
```
"42"
"3.14159"
"-3.14159"
"-3.142e+00"
Value too large for defined data type
```


## Defect reports


## See also


| cpp/utility/dsc to_chars_result | (see dedicated page) |
| cpp/utility/dsc from_chars | (see dedicated page) |
| cpp/string/basic_string/dsc to_string | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/basic_ostream/dsc operator_ltlt | (see dedicated page) |

