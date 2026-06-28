---
title: std::chrono::operator<<(std::chrono::weekday)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os, const std::chrono::weekday& wd );
If `!wd.ok()`, inserts `wd.c_encoding()` followed by `" is not a valid weekday"` into `os`. Otherwise, forms a `std::basic_string<CharT>` `s` consisting of the abbreviated weekday name for the weekday represented by `wd`, determined using the locale associated with `os`, and inserts `s` into `os`.
Equivalent to
cc|
return os << (wd.ok() ?
std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{:L%a}"), wd) :
std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{} is not a valid weekday"),
wd.c_encoding()));
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday | (see dedicated page) |

