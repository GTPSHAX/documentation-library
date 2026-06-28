---
title: std::formatter<std::basic_stacktrace>
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/formatter
---


# formattersmall|<std::basic_stacktrace>

ddcl|header=stacktrace|since=c++23|1=
template< class Allocator >
struct formatter<std::basic_stacktrace<Allocator>>;
The template specialization of `std::formatter` for `std::basic_stacktrace<Allocator>` allows users to convert a stacktrace object to string using formatting functions such as `std::format`.
No format specifier is allowed.
A stacktrace object `s` is formatted as if by copying  to the output.

## Example


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |

