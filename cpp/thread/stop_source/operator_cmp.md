---
title: operator==(std::stop_source)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/operator_cmp
---


# operator==


```cpp
dcl|since=c++20|1=
friend bool operator==( const stop_source& lhs, const stop_source& rhs ) noexcept;
```

Compares two `stop_source` values.

## Parameters


### Parameters

- `lhs, rhs` - `stop_source`s to compare

## Return value

`true` if `lhs` and `rhs` have the same stop-state, or both have no stop-state, otherwise `false`.
