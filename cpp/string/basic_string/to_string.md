---
title: std::to_string
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/to_string
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|
std::string to_string( int value );
dcl|num=2|since=c++11|
std::string to_string( long value );
dcl|num=3|since=c++11|
std::string to_string( long long value );
dcl|num=4|since=c++11|
std::string to_string( unsigned value );
dcl|num=5|since=c++11|
std::string to_string( unsigned long value );
dcl|num=6|since=c++11|
std::string to_string( unsigned long long value );
dcl|num=7|since=c++11|
std::string to_string( float value );
dcl|num=8|since=c++11|
std::string to_string( double value );
dcl|num=9|since=c++11|
std::string to_string( long double value );
```

Converts a numeric value to `std::string`.
rrev multi|until1=c++26
|rev1=
Let  be an internal to the conversion functions buffer, sufficiently large to contain the result of conversion.
1. Converts a signed integer to a string as if by `std::sprintf(buf, "%d", value)`.
2. Converts a signed integer to a string as if by `std::sprintf(buf, "%ld", value)`.
3. Converts a signed integer to a string as if by `std::sprintf(buf, "%lld", value)`.
4. Converts an unsigned integer to a string as if by `std::sprintf(buf, "%u", value)`.
5. Converts an unsigned integer to a string as if by `std::sprintf(buf, "%lu", value)`.
6. Converts an unsigned integer to a string as if by `std::sprintf(buf, "%llu", value)`.
@7,8@ Converts a floating point value to a string as if by `std::sprintf(buf, "%f", value)`.
9. Converts a floating point value to a string as if by `std::sprintf(buf, "%Lf", value)`.
|rev2=
@1-9@ Converts a numeric value to a string as if by }.

## Parameters


### Parameters

- `value` - a numeric value to convert

## Return value

A string holding the converted value.

## Exceptions

May throw `std::bad_alloc` from the `std::string` constructor.

## Notes

* With floating point types `std::to_string` may yield unexpected results as the number of significant digits in the returned string can be zero, see the example.
* The return value may differ significantly from what `std::cout` prints by default, see the example.
rrev|until=c++26|
* `std::to_string` relies on the current C locale for formatting purposes, and therefore concurrent calls to `std::to_string` from multiple threads may result in partial serialization of calls.
** The results of overloads for integer types do not rely on the current C locale, and thus implementations generally avoid access to the current C locale in these overloads for both correctness and performance. However, such avoidance is not guaranteed by the standard.
C++17 provides `cpp/utility/to_chars|std::to_chars` as a higher-performance locale-independent alternative.

## Example


### Example

```cpp
#include <cstdio>
#include <format>
#include <initializer_list>
#include <iostream>
#include <string>

#if __cpp_lib_to_string >= 202306L
constexpr auto revision() { return " (post C++26)"; }
#else
constexpr auto revision() { return " (pre C++26)"; }
#endif

int main()
{
    for (const double f : {1.23456789555555, 23.43, 1e-9, 1e40, 1e-40, 123456789.0})
    {
        std::cout << "to_string:\t" << std::to_string(f) << revision() << '\n';

        // Before C++26, the output of std::to_string matches std::printf.
        std::printf("printf:\t\t%f\n", f);

        // As of C++26, the output of std::to_string matches std::format.
        std::cout << std::format("format:\t\t{}\n", f);

        std::cout << "std::cout:\t" << f << "\n\n";
    }
}
```


**Output:**
```
to_string:      1.234568 (pre C++26)
printf:         1.234568
format:         1.23456789555555
std::cout:      1.23457

to_string:      23.430000 (pre C++26)
printf:         23.430000
format:         23.43
std::cout:      23.43

to_string:      0.000000 (pre C++26)
printf:         0.000000
format:         1e-09
std::cout:      1e-09

to_string:      10000000000000000303786028427003666890752.000000 (pre C++26)
printf:         10000000000000000303786028427003666890752.000000
format:         1e+40
std::cout:      1e+40

to_string:      0.000000 (pre C++26)
printf:         0.000000
format:         1e-40
std::cout:      1e-40

to_string:      123456789.000000 (pre C++26)
printf:         123456789.000000
format:         123456789
std::cout:      1.23457e+08
```


## See also


| cpp/string/basic_string/dsc to_wstring | (see dedicated page) |
| cpp/string/basic_string/dsc stoul | (see dedicated page) |
| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stof | (see dedicated page) |
| cpp/utility/dsc to_chars | (see dedicated page) |

