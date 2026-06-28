---
title: std::formatter<std::chrono::zoned_time>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/formatter
---


# formattersmall|<std::chrono::zoned_time>

|local_time_format

```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++20|
template< class Duration, class TimeZonePtr, class CharT >
struct formatter<std::chrono::zoned_time<Duration, TimeZonePtr>, CharT>
: std::formatter</*local-time-format-t*/
<std::common_type_t<Duration,
std::chrono::seconds>>, CharT>
dcl|num=2|since=c++20|1=
template< class Duration >
/*local-time-format-t*/<Duration>
local_time_format( const std::chrono::local_time<Duration>& tp,
const std::string* abbrev = nullptr,
const std::chrono::seconds* offset_sec = nullptr );
dcla|num=3|since=c++20|expos=yes|
template< class Duration >
struct /*local-time-format-t*/
{
std::chrono::local_time<Duration> /*time*/;
const std::string* /*abbrev*/;
const std::chrono::seconds* /*offset_sec*/;
};
dcl|num=4|since=c++20|
template< class Duration, class CharT >
struct formatter</*local-time-format-t*/<Duration>, CharT>;
```

1. Specialization of `std::formatter` that defines formatting rules for a `std::chrono::zoned_time`.
* The `parse` member is inherited from the base class.
* Let `tp` be the formatting argument and `ctx` be the formatting context, the behavior of the `format` member is equivalent to:
box|
`1=using common_duration_type = std::common_type_t<Duration, std::chrono::seconds>;`<br>
`1=using formatter_type = std::formatter<``<common_duration_type>;`<br><br>
`1=std::chrono::sys_info info = tp.get_info();`<br>
}
2. Creates an object which can be formatted as a `std::chrono::zoned_time`.
@@ Returns }.
3. An exposition-only type containing all information needed for formatting a `std::chrono::zoned_time`:
*  contains the time zone abbreviation.
*  contains the offset from UTC.
*  contains all other information needed.
4. Specialization of `std::formatter` that defines underlying formatting rules for a `std::chrono::zoned_time`.
@@ Let `f` be the formatting argument, the specialization has the following extra formatting rules:
* If *chrono-spec* is omitted, the result is equivalent to using **`%F %T %Z`** as chrono-spec.
* If **`%Z`** is used, it is replaced with `*f.abbrev` if `f.abbrev` is not a null pointer value; otherwise an exception of type `std::format_error` is thrown.
* If **`%z`** or a modified variant of **`%z`** is used, it is replaced with `*f.offset_sec` if `f.offset_sec` is not a null pointer value; otherwise an exception of type `std::format_error` is thrown.
The `std::formatter` specialization is usually not directly accessed, but is used through formatting functions.

## Format specification


## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |

