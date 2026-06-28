---
title: std::error_category::error_category
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_category/error_category
---


```cpp
dcl | num=1 | since=c++11 | 1=
constexpr error_category() noexcept;
dcl | num=2 | since=c++11 | 1=
error_category( const error_category& ) = delete;
```

1. Constructs the error category object.
2. Copy constructor is deleted. `error_category` is neither *MoveConstructible* nor *CopyConstructible*.

## Parameters

(none)

## Defect reports

