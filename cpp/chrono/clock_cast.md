---
title: std::chrono::clock_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/clock_cast
---

ddcl|header = chrono|since=c++20|1=
template< class Dest, class Source, class Duration >
auto clock_cast( const std::chrono::time_point<Source, Duration>& t );
Converts the time point `t` of a clock `Source` to an equivalent time point of the clock `Dest`, using `std::chrono::system_clock` and/or `std::chrono::utc_clock` as intermediaries if necessary.
* If the expression } is well-formed, returns the result of that expression.
* Otherwise, if at least one of the following two expressions are well-formed, then
:* If both expressions are well-formed, the conversion is ambiguous, and the program is ill-formed.
:* Otherwise, exactly one of the two expressions is well-formed; the result of that expression is returned.
:@1@c|std::chrono::clock_time_conversion<Dest, std::chrono::system_clock>{}(
std::chrono::clock_time_conversion<std::chrono::system_clock, Source>{}(t))
:@2@c|std::chrono::clock_time_conversion<Dest, std::chrono::utc_clock>{}(
std::chrono::clock_time_conversion<std::chrono::utc_clock, Source>{}(t))
* Otherwise, if at least one of the following two expressions are well-formed, then
:* If both expressions are well-formed, the conversion is ambiguous, and the program is ill-formed.
:* Otherwise, exactly one of the two expressions is well-formed; the result of that expression is returned.
:@1@c|std::chrono::clock_time_conversion<Dest, std::chrono::utc_clock>{}(
std::chrono::clock_time_conversion<std::chrono::utc_clock, std::chrono::system_clock>{}(
std::chrono::clock_time_conversion<std::chrono::system_clock, Source>{}(t)))
:@2@c|std::chrono::clock_time_conversion<Dest, std::chrono::system_clock>{}(
std::chrono::clock_time_conversion<std::chrono::system_clock, std::chrono::utc_clock>{}(
std::chrono::clock_time_conversion<std::chrono::utc_clock, Source>{}(t)))
* Otherwise, this function does not participate in overload resolution.

## Return value

The result of the conversion, determined as described above.

## Example

