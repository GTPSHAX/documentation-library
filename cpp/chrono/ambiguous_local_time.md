---
title: std::chrono::ambiguous_local_time
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/ambiguous_local_time
---

ddcl|header=chrono|since=c++20|
class ambiguous_local_time;
Defines a type of object to be thrown as exception to report that an attempt was made to convert an ambiguous `std::chrono::local_time` to a `std::chrono::sys_time` without specifying a `std::chrono::choose` (such as `choose::earliest` or `choose::latest`).
This exception is thrown by `std::chrono::time_zone::to_sys` and functions that call it (such as the constructors of `std::chrono::zoned_time` that take a `std::chrono::local_time`).

## Member functions

member|ambiguous_local_time|2=

```cpp
dcl|num=1|since=c++20|
template< class Duration >
ambiguous_local_time( const std::chrono::local_time<Duration>& tp,
const std::chrono::local_info& i );
dcl|num=2|since=c++20|
ambiguous_local_time( const ambiguous_local_time& other ) noexcept;
```

Constructs the exception object.
1. The explanatory string returned by `what()` is equivalent to that produced by `os.str()` after the following code:

```cpp
std::ostringstream os;
os << tp << " is ambiguous.  It could be\n"
   << tp << ' ' << i.first.abbrev << " == "
   << tp - i.first.offset << " UTC or\n"
   << tp << ' ' << i.second.abbrev  << " == "
   << tp - i.second.offset  << " UTC";
```

@@ The behavior is undefined if `1=i.result != std::chrono::local_info::ambiguous`.
2. Copy constructor. If `*this` and `other` both have dynamic type `std::chrono::ambiguous_local_time` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `tp` - the time point for which conversion was attempted
- `i` - a `std::chrono::local_info` describing the result of the conversion attempt
- `other` - another `ambiguous_local_time` to copy

## Exceptions

May throw `std::bad_alloc`

## Notes

Because copying a standard library class derived from `std::exception` is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string.

## See also


| cpp/chrono/dsc nonexistent_local_time | (see dedicated page) |

