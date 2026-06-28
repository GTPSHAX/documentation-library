---
title: std::fetestexcept
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/fetestexcept
---


```cpp
dcl | since=c++11 |
int fetestexcept( int excepts );
```

Determines which of the specified subset of the floating point exceptions are currently set. The argument `excepts` is a bitwise OR of the floating point exception macros.

## Parameters


### Parameters


## Return value

Bitwise OR of the floating-point exception macros that are both included in `excepts` and correspond to floating-point exceptions currently set.

## Example


## See also

