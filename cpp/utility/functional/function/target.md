---
title: std::function::target
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/target
---


```cpp
dcl | num=1 | since=c++11 |
template< class T >
T* target() noexcept;
dcl | num=2 | since=c++11 |
template< class T >
const T* target() const noexcept;
```

Returns a pointer to the stored callable function target.

## Parameters

(none)

## Return value

A pointer to the stored function if `target_type() , otherwise a null pointer.

## Example


## Defect reports


## See also

