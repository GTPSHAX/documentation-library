---
title: std::format_to_n_result
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/format_to_n
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class OutputIt, class... Args >
std::format_to_n_result<OutputIt>
format_to_n( OutputIt out, std::iter_difference_t<OutputIt> n,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++20|1=
template< class OutputIt, class... Args >
std::format_to_n_result<OutputIt>
format_to_n( OutputIt out, std::iter_difference_t<OutputIt> n,
std::wformat_string<Args...> fmt, Args&&... args );
dcl|num=3|since=c++20|1=
template< class OutputIt, class... Args >
std::format_to_n_result<OutputIt>
format_to_n( OutputIt out, std::iter_difference_t<OutputIt> n,
const std::locale& loc,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=4|since=c++20|1=
template< class OutputIt, class... Args >
std::format_to_n_result<OutputIt>
format_to_n( OutputIt out, std::iter_difference_t<OutputIt> n,
const std::locale& loc,
std::wformat_string<Args...> fmt, Args&&... args );
dcl|num=5|since=c++20|1=
template< class OutputIt >
struct format_to_n_result {
OutputIt out;
std::iter_difference_t<OutputIt> size;
};
```

Format `args` according to the format string `fmt`, and write the result to the output iterator `out`. At most `n` characters are written. If present, `loc` is used for locale-specific formatting.
Let `CharT` be `char` for overloads ,  for overloads .
cpp/enable if|plural=true|
`OutputIt` satisfies the concept `std::output_iterator<const CharT&>`.
The behavior is undefined if `OutputIt` does not model (meet the semantic requirements of) the  concept `std::output_iterator<const CharT&>`, or if `std::formatter<std::remove_cvref_t<Ti>, CharT>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args`.
5. `std::format_to_n_result` has no base classes, or members other than `out`, `size` and implicitly declared special member functions.

## Parameters


### Parameters

- `out` - iterator to the output buffer
- `n` - maximum number of characters to be written to the buffer
- `fmt` - 
- `args...` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

A `format_to_n_result` such that the `out` member is an iterator past the end of the output range, and the `size` member is the total (not truncated) output size.

## Exceptions

Propagates any exception thrown by formatter or iterator operations.

## Notes

The libstdc++ implementation prior to GCC-13.3 had a [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=110990 bug] in reporting the correct `format_to_n_result::out` value.

## Example


### Example

```cpp
#include <format>
#include <initializer_list>
#include <iomanip>
#include <iostream>
#include <string_view>

int main()
{
    char buffer[64];

    for (std::size_t max_chars_to_write : {std::size(buffer) - 1, 23uz, 21uz})
    {
        const std::format_to_n_result result =
            std::format_to_n(
                buffer, max_chars_to_write,
                "Hubble's H{2} {3} {0}{4}{1} km/sec/Mpc.", // 24 bytes w/o formatters
                71,       // {0}, occupies 2 bytes
                8,        // {1}, occupies 1 byte
                "\u2080", // {2}, occupies 3 bytes, '₀' (SUBSCRIPT ZERO)
                "\u2245", // {3}, occupies 3 bytes, '≅' (APPROXIMATELY EQUAL TO)
                "\u00B1"  // {4}, occupies 2 bytes, '±' (PLUS-MINUS SIGN)
                ); // 24 + 2 + 1 + 3 + 3 + 2 == 35, no trailing '\0'

        *result.out = '\0'; // adds terminator to buffer

        const std::string_view str(buffer, result.out);

        std::cout << "Buffer until '\\0': " << std::quoted(str) << '\n'
                  << "Max chars to write: " << max_chars_to_write << '\n'
                  << "result.out offset: " << result.out - buffer << '\n'
                  << "Untruncated output size: " << result.size << "\n\n";
    }
}
```


**Output:**
```
Buffer until '\0': "Hubble's H₀ ≅ 71±8 km/sec/Mpc."
Max chars to write: 63
result.out offset: 35
Untruncated output size: 35

Buffer until '\0': "Hubble's H₀ ≅ 71±8"
Max chars to write: 23
result.out offset: 23
Untruncated output size: 35

Buffer until '\0': "Hubble's H₀ ≅ 71�"
Max chars to write: 21
result.out offset: 21
Untruncated output size: 35
```


## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/utility/format/dsc format_to | (see dedicated page) |
| cpp/utility/format/dsc formatted_size | (see dedicated page) |

