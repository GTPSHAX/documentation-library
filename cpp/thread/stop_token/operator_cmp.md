---
title: operator==(std::stop_token)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token/operator_cmp
---


# operator==


```cpp
dcl|since=c++20|1=
friend bool operator==( const stop_token& lhs, const stop_token& rhs ) noexcept;
```

Compares two `stop_token` values.

## Parameters


### Parameters

- `lhs, rhs` - `stop_token`s to compare

## Return value

`true` if `lhs` and `rhs` have the same associated stop-state, or both have no associated stop-state, otherwise `false`.
