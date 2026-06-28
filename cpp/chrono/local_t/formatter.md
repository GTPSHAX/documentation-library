---
title: std::formatter<std::chrono::local_time>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/local_t/formatter
---


# formattersmall|<std::chrono::local_time>

ddcl|header=chrono|
template< class Duration, class CharT >
struct formatter<std::chrono::local_time<Duration>, CharT>;
Specialization of `std::formatter` that defines formatting rules for a `std::chrono::local_time`.
If **`%Z`**, **`%z`** or a modified variant of **`%z`** is used, a `std::format_error` is thrown.
`std::formatter` is usually not directly accessed, but is used through formatting functions.

## Format specification


## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |

