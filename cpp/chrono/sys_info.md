---
title: std::chrono::sys_info
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/sys_info
---

ddcl|header=chrono|since=c++20|
struct sys_info;
The class `sys_info` describes time zone information associated with a time zone at a particular point in time (represented as either a `std::chrono::sys_time` or a `std::chrono::local_time`). This is a low-level data structure typically not used directly by user code.

## Member objects


| Item | Description |
|------|-------------|
| **Member object** | Type |

The `begin` and `end` data members indicate the range -  - in which the `offset` and `abbrev` are in effect for the time zone associated with this `sys_info`.
The `offset` and `abbrev` data member indicate the UTC offset and time zone abbreviation, respectively, in effect for the associated time zone and `std::chrono::time_point`. Note that time zone abbreviations are not unique.
The `save` data member, if nonzero, indicates that the time zone is on daylight saving time at the specified time point. In this case, `offset - save` is a suggestion of what offset this time zone might use if it were off daylight saving time. However, this information is not authoritative: the only way to ascertain the actual offset is to query the time zone with a time point that is actually off daylight savings time (i.e. returns a `sys_info` such that `1=save == 0min`).

## Nonmember functions


| cpp/chrono/sys_info/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|sys_info | (see dedicated page) |


## Example

