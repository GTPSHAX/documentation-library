---
title: std::chrono::local_info
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/local_info
---

ddcl|header=chrono|since=c++20|
struct local_info;
The class `local_info` describes the result of converting a `std::chrono::local_time` to a `std::chrono::sys_time`.
* If the result of the conversion is unique, then `1=result == local_info::unique`, `first` is filled out with the correct `std::chrono::sys_info`, and `second` is zero-initialized.
* If the `local_time` is nonexistent, then `1=result == local_info::nonexistent`, `first` is filled out with the `std::chrono::sys_info` that ends just prior to the `local_time`, and `second` is filled out with the `std::chrono::sys_info` that begins just after the `local_time`.
* If the `local_time` is ambiguous, then `1=result == local_info::ambiguous`, `first` is filled out with the `std::chrono::sys_info` that ends just after the `local_time`, and `second` is filled with the `std::chrono::sys_info` that starts just before the `local_time`.
This is a low-level data structure; typical conversions from `local_time` to `sys_time` will use it implicitly rather than explicitly.

## Member constants


| Item | Description |
|------|-------------|
| **Name** | Value |


## Member objects


| Item | Description |
|------|-------------|
| **Member object** | Type |


## Nonmember functions


| cpp/chrono/local_info/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|local_info | (see dedicated page) |

