---
title: std::chrono::zoned_time::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/operator=
---


```cpp
dcl|since=c++20|num=1|1=
zoned_time& operator=( const zoned_time& other ) = default;
dcl|since=c++20|num=2|1=
zoned_time& operator=( const std::chrono::sys_time<Duration>& other );
dcl|since=c++20|num=3|1=
zoned_time& operator=( const std::chrono::local_time<Duration>& other );
```

Assign the value of `other` to `*this`.
1. Defaulted copy assignment operator. Copy-assigns both the stored time point and the stored time zone pointer. `zoned_time` has no move assignment operator; a move is a copy.
2. Assigns `other` to the stored time point. The time zone pointer is unchanged. After this call, `1=get_sys_time() == other`.
3. Converts `other` to a `std::chrono::sys_time` as if by `zone->to_sys(other)` (where `zone` is the non-static data member holding the stored time zone pointer) and assigns the result to the stored time point. The time zone pointer is unchanged. After this call, `1=get_local_time() == other`.

## Return value

`*this`
