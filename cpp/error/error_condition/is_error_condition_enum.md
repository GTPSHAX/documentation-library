---
title: std::is_error_condition_enum
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/is_error_condition_enum
---


```cpp
**Header:** `<`system_error`>`
dcl|since=c++11|
template< class T >
struct is_error_condition_enum;
```

If `T` is an error condition enum (such as `std::errc`), this template provides the member constant `value` equal `true`. For any other type, `value` is `false`.
This template may be specialized for a  to indicate that the type is eligible for `std::error_condition` implicit conversions.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
inline constexpr bool is_error_condition_enum_v =
is_error_condition_enum<T>::value;

## See also


| cpp/error/error_code/dsc is_error_code_enum | (see dedicated page) |

