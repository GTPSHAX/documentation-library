---
title: std::numeric_limits::is_signed
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_signed
---


```cpp
dcl rev multi
|dcl1=
static const bool is_signed;
|since2=c++11|dcl2=
static constexpr bool is_signed;
```

The value of `std::numeric_limits<T>::is_signed` is `true` for all signed arithmetic types `T` and `false` for the unsigned types. This constant is meaningful for all specializations.

## Standard specializations


## Example


### Example


**Output:**
```
bool            : unsigned
char            : signed
wchar_t         : signed
char16_t        : unsigned
char32_t        : unsigned
float           : signed
non-specialized : unsigned
decltype(42)    : signed
```


## See also


| cpp/types/dsc is_signed | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_exact | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_bounded | (see dedicated page) |

