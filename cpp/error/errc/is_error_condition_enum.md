---
title: std::is_error_condition_enum<std::errc>
type: Utilities
source: https://en.cppreference.com/w/cpp/error/errc/is_error_condition_enum
---


# is_error_condition_enumsmall|<std::errc>

ddcl|header=system_error|since=c++11|
template<>
struct is_error_condition_enum<std::errc> : std::true_type;
Specifies that `std::errc` is an error condition enum. This enables implicit conversion to `std::error_condition`.

## See also


| cpp/error/error condition/dsc is_error_condition_enum | (see dedicated page) |

