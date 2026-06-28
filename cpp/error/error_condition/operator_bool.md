---
title: std::error_condition::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/operator_bool
---


```cpp
dcl | since=c++11 |
explicit operator bool() const noexcept;
```

Checks whether the stored error value is not zero.

## Parameters

(none)

## Return value

`true` if `1=value != 0`, `false` otherwise.
