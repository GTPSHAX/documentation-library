---
title: std::chrono::nonexistent_local_time
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/nonexistent_local_time
---

ddcl|header=chrono|since=c++20|
class nonexistent_local_time;
Defines a type of object to be thrown as exception to report that an attempt was made to convert a nonexistent `std::chrono::local_time` to a `std::chrono::sys_time` without specifying a `std::chrono::choose` (such as `choose::earliest` or `choose::latest`).
This exception is thrown by `std::chrono::time_zone::to_sys` and functions that call it (such as the constructors of `std::chrono::zoned_time` that take a `std::chrono::local_time`).

## Member functions

member|nonexistent_local_time|2=

```cpp
dcl|num=1|since=c++20|
template< class Duration >
nonexistent_local_time( const std::chrono::local_time<Duration>& tp,
const std::chrono::local_info& i );
dcl|num=2|since=c++20|
nonexistent_local_time( const nonexistent_local_time& other ) noexcept;
```

Constructs the exception object.
1. The explanatory string returned by `what()` is equivalent to that produced by `os.str()` after the following code:

```cpp
std::ostringstream os;
os << tp << " is in a gap between\n"
   << std::chrono::local_seconds(i.first.end.time_since_epoch()) + i.first.offset
   << ' ' << i.first.abbrev << " and\n"
   << std::chrono::local_seconds(i.second.begin.time_since_epoch()) + i.second.offset
   << ' ' << i.second.abbrev
   << " which are both equivalent to\n"
   << i.first.end << " UTC";
```

@@ The behavior is undefined if `1=i.result != std::chrono::local_info::nonexistent`.
2. Copy constructor. If `*this` and `other` both have dynamic type `std::chrono::nonexistent_local_time` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `tp` - the time point for which conversion was attempted
- `i` - a `std::chrono::local_info` describing the result of the conversion attempt
- `other` - another `nonexistent_local_time` to copy

## Exceptions

May throw `std::bad_alloc`

## Notes

Because copying a standard library class derived from `std::exception` is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string.

## See also


| cpp/chrono/dsc ambiguous_local_time | (see dedicated page) |

