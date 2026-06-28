---
title: std::feclearexcept
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feclearexcept
---


```cpp
dcl | since=c++11 |
int feclearexcept( int excepts );
```

Attempts to clear the floating-point exceptions that are listed in the bitmask argument `excepts`, which is a bitwise OR of the floating point exception macros.

## Parameters


### Parameters


## Return value

`0` if all indicated exceptions were successfully cleared or if `excepts` is zero. Returns a non-zero value on error.

## Example


## See also

