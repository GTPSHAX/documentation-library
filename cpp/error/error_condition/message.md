---
title: std::error_condition::message
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/message
---


```cpp
dcl | since=c++11 |
std::string message() const;
```

Returns an explanatory message for the stored error value and error category. Effectively calls `category().message(value())`.

## Parameters

(none)

## Return value

An explanatory message for the stored error value and error category.

## See also

