---
title: print(std::ostream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/print
---


# printsmall|(std::ostream)

ddcl|header=ostream|since=c++23|
template< class... Args >
void print( std::ostream& os, std::format_string<Args...> fmt, Args&&... args );
Formats `args` according to the format string `fmt`, and inserts the result into `os` stream.
If the ordinary literal encoding is UTF-8, equivalent to:
* . Otherwise,
* .
The behavior is undefined if `std::formatter<Ti, char>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args` (as required by `std::make_format_args`).

## Parameters


### Parameters

- `os` - output stream to insert data into
- `fmt` - 
- `args...` - arguments to be formatted

## Exceptions


## Notes


## Example


### Example

```cpp
#include <array>
#include <cctype>
#include <cstdio>
#include <format>
#include <numbers>
#include <ranges>
#include <sstream>

int main()
{
    std::array<char, 24> buf;
    std::format_to(buf.begin(), "{:.15f}", std::numbers::sqrt2);

    unsigned num{}, sum{};

    for (auto n : buf
                {{!
```

| std::views::transform([](char x) { return x - '0'; })
| std::views::take_while([&sum](char) { return sum < 42; }))
sum += n, ++num;
std::stringstream stream;
#ifdef __cpp_lib_print
std::print(stream,
#else
stream << std::format(
#endif
"√2 \N{ALMOST EQUAL TO} {0}.\n"
"The sum of its first {1} digits is {2}.",
std::numbers::sqrt2, num, sum
);
std::puts(stream.str().data());
}
|output=
√2 ≈ 1.4142135623730951.
The sum of its first 13 digits is 42.

## See also


| cpp/io/basic_ostream/dsc println | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |

