---
title: std::chrono::zoned_time
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
template<
class Duration,
class TimeZonePtr = const std::chrono::time_zone*
> class zoned_time;
dcl|since=c++20|1=
using zoned_seconds = std::chrono::zoned_time<std::chrono::seconds>;
```

The class `zoned_time` represents a logical pairing of a time zone and a `std::chrono::time_point` whose resolution is `Duration`.
An invariant of `zoned_time` is that it always refers to a valid time zone and represents an existing and unambiguous time point in that time zone. Consistent with this invariant, `zoned_time` has no move constructor or move assignment operator; attempts to move a `zoned_time` will perform a copy.
The program is ill-formed if `Duration` is not a specialization of `std::chrono::duration`.
The template parameter `TimeZonePtr` allows users to supply their own time zone pointer types and further customize the behavior of `zoned_time` via `std::chrono::zoned_traits`. Custom time zone types need not support all the operations supported by `std::chrono::time_zone`, only those used by the functions actually called on the `zoned_time`.
`TimeZonePtr` must be *MoveConstructible*. Move-only `TimeZonePtr`s are allowed but difficult to use, as the `zoned_time` will be immovable and it is not possible to access the stored `TimeZonePtr`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/chrono/zoned_time/dsc constructor | (see dedicated page) |
| 1=cpp/chrono/zoned_time/dsc operator= | (see dedicated page) |
| cpp/chrono/zoned_time/dsc get_time_zone | (see dedicated page) |
| cpp/chrono/zoned_time/dsc get_local_time | (see dedicated page) |
| cpp/chrono/zoned_time/dsc get_sys_time | (see dedicated page) |
| cpp/chrono/zoned_time/dsc get_info | (see dedicated page) |


## Non-member functions


| cpp/chrono/zoned_time/dsc operator cmp | (see dedicated page) |
| cpp/chrono/zoned_time/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|zoned_time | (see dedicated page) |
| cpp/chrono/zoned_time|nested=true|notes= | |


## Helper specializations


```cpp
dcl|since=c++23|1=
template< class Duration >
constexpr bool enable_nonlocking_formatter_optimization
<chrono::zoned_time<Duration, const chrono::time_zone*>> = true;
```

This specialization of  enables efficient implementation of  and  for printing a `chrono::zoned_time` object.

## 


## Example


### Example


**Output:**
```
<nowiki/>
             Africa/Casablanca - Zoned Time: 2023-06-29 20:58:34.697449319 +01
America/Argentina/Buenos_Aires - Zoned Time: 2023-06-29 16:58:34.709957354 -03
              America/Barbados - Zoned Time: 2023-06-29 15:58:34.709977888 AST
    America/Indiana/Petersburg - Zoned Time: 2023-06-29 15:58:34.709998072 EDT
Error: tzdb: cannot locate zone: America/Tarasco_Bar
              Antarctica/Casey - Zoned Time: 2023-06-30 06:58:34.710093685 +11
             Antarctica/Vostok - Zoned Time: 2023-06-30 01:58:34.710107932 +06
                  Asia/Magadan - Zoned Time: 2023-06-30 06:58:34.710121831 +11
                   Asia/Manila - Zoned Time: 2023-06-30 03:58:34.710134751 PST
                 Asia/Shanghai - Zoned Time: 2023-06-30 03:58:34.710153259 CST
                    Asia/Tokyo - Zoned Time: 2023-06-30 04:58:34.710172815 JST
              Atlantic/Bermuda - Zoned Time: 2023-06-29 16:58:34.710191043 ADT
              Australia/Darwin - Zoned Time: 2023-06-30 05:28:34.710236720 ACST
            Europe/Isle_of_Man - Zoned Time: 2023-06-29 20:58:34.710256834 BST
Error: tzdb: cannot locate zone: Europe/Laputa
              Indian/Christmas - Zoned Time: 2023-06-30 02:58:34.710360409 +07
                  Indian/Cocos - Zoned Time: 2023-06-30 02:28:34.710377520 +0630
             Pacific/Galapagos - Zoned Time: 2023-06-29 13:58:34.710389952 -06
```


## See also


| cpp/chrono/dsc time_zone | (see dedicated page) |

