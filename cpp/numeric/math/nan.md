---
title: std::nan
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/nan
---


```cpp
**Header:** `<`cmath`>`
dcl|since=c++11|num=1|
float       nanf( const char* arg );
dcl|since=c++11|num=2|
double      nan ( const char* arg );
dcl|since=c++11|num=3|
long double nanl( const char* arg );
```

Converts the character string `arg` into the corresponding quiet NaN value, as if by calling `std::strtof`, `std::strtod`, or `std::strtold`, respectively.
1. The call , where *n-char-sequence* is a sequence of digits, ASCII letters, and underscores, is equivalent to the call .
@@ The call `std::nanf("")` is equivalent to the call `std::strtof("NAN()", (char**)nullptr);`.
@@ The call , where *string* is neither an *n-char-sequence* nor an empty string, is equivalent to the call `std::strtof("NAN", (char**)nullptr);`.
2. Same as , but calls `std::strtod` instead of `std::strtof`.
3. Same as , but calls `std::strtold` instead of `std::strtof`.

## Parameters


### Parameters

- `arg` - narrow character string identifying the contents of a NaN

## Return value

The quiet NaN value that corresponds to the identifying string `arg` or zero if the implementation does not support quiet NaNs.
If the implementation supports IEEE floating-point arithmetic (IEC 60559), it also supports quiet NaNs.

## Error handling

This function is not subject to any of the error conditions specified in `cpp/numeric/math/math_errhandling`.

## Example


### Example

```cpp
#include <cmath>
#include <cstdint>
#include <cstring>
#include <iostream>

int main()
{
    double f1 = std::nan("1");
    std::uint64_t f1n; std::memcpy(&f1n, &f1, sizeof f1);
    std::cout << "nan(\"1\") = " << f1 << " (" << std::hex << f1n << ")\n";

    double f2 = std::nan("2");
    std::uint64_t f2n; std::memcpy(&f2n, &f2, sizeof f2);
    std::cout << "nan(\"2\") = " << f2 << " (" << std::hex << f2n << ")\n";
}
```


**Output:**
```
nan("1") = nan (7ff0000000000001)
nan("2") = nan (7ff0000000000002)
```


## See also


| cpp/numeric/math/dsc isnan | (see dedicated page) |
| cpp/numeric/math/dsc NAN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_signaling_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc signaling_NaN | (see dedicated page) |

