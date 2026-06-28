---
title: std::chrono::high_resolution_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/high_resolution_clock
---

ddcl|header=chrono|since=c++11|
class high_resolution_clock;
Class `std::chrono::high_resolution_clock` represents the clock with the smallest tick period provided by the implementation. It may be an alias of `std::chrono::system_clock` or `std::chrono::steady_clock`, or a third, independent clock.
`std::chrono::high_resolution_clock` meets the requirements of *TrivialClock*.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member constants


## Member functions


## Notes

There has been some controversy around the use of `high_resolution_clock`. Howard Hinnant, who claims to have introduced `high_resolution_clock` to the language, stated in 2016 on the [https://lists.isocpp.org/mailman/listinfo.cgi/std-discussion ISO C++ Standard - Discussion mailing list] that he was in favor of deprecating it. His rationale was that, because the standard allows for it to be an alias for `std::chrono::steady_clock` or `std::chrono::system_clock`, its use adds uncertainty to a program without benefit. However, other participants in the thread spoke out its favor, for instance on the basis that, because neither `std::chrono::steady_clock` nor `std::chrono::system_clock` come with any particular resolution guarantees, `high_resolution_clock` serves a useful role by giving the vendor an opportunity to supply the platform's highest-resolution clock, when neither its `std::chrono::steady_clock` nor its `std::chrono::system_clock` would be that.
It is often just an alias for `std::chrono::steady_clock` or `std::chrono::system_clock`, but which one it is depends on the library or configuration. When it is a `system_clock`, it is not monotonic (e.g., the time can go backwards). For example, as of 2023, libstdc++ has it aliased to `system_clock` "until higher-than-nanosecond definitions become feasible"<ref>[https://github.com/gcc-mirror/gcc/blob/63663e4e69527b308687c63bacb0cc038b386593/libstdc%2B%2B-v3/include/bits/chrono.h#L1285 libstdc++ `<chrono.h>`]</ref>, MSVC has it as `steady_clock`, and libc++ uses `steady_clock` when the C++ standard library implementation supports a monotonic clock and `system_clock` otherwise<ref>[https://github.com/llvm/llvm-project/blob/aa97f6b4947e599e17e900aebd511d8d497c3be9/libcxx/include/__chrono/high_resolution_clock.h#L26 libc++ `<high_resolution_clock.h>`]</ref>.

## See also


| cpp/chrono/system_clock|wall clock time from the system-wide realtime clock|notes= | |
| cpp/chrono/steady_clock|monotonic clock that will never be adjusted|notes= | |


## External links

