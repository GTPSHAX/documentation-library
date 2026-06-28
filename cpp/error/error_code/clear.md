---
title: std::error_code::clear
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/clear
---


```cpp
dcl|since=c++11|1=
void clear() noexcept;
```

Replaces the error code and error category with default values.
Equivalent to `1=*this = error_code(0, std::system_category())`.

## Parameters

(none)

## Return value

(none)
