---
title: std::fegetenv
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feenv
---


```cpp
dcl | since=c++11 | num=1|
int fegetenv( std::fenv_t* envp )
dcl | since=c++11 | num=2|
int fesetenv( const std::fenv_t* envp );
```

Manages the status of the floating-point environment.
1. Attempts to store the status of the floating-point environment in the object pointed to by `envp`.
2. Attempts to establish the floating-point environment from the object pointed to by `envp`. The value of that object must be previously obtained by a call to `std::feholdexcept` or `std::fegetenv` or be a floating-point macro constant. If any of the floating-point status flags are set in `envp`, they become set in the environment (and are then testable with `std::fetestexcept`), but the corresponding floating-point exceptions are not raised (execution continues uninterrupted)

## Parameters


### Parameters


## Return value

`0` on success, non-zero otherwise.

## See also

