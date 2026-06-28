---
title: std::feholdexcept
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feholdexcept
---


```cpp
dcl | since=c++11 |
int feholdexcept( std::fenv_t* envp )
```

First, saves the current floating-point environment to the object pointed to by `envp` (similar to `std::fegetenv`), then clears all floating-point status flags, and then installs the non-stop mode: future floating-point exceptions will not interrupt execution (will not trap), until the floating-point environment is restored by `std::feupdateenv` or `std::fesetenv`.
This function may be used in the beginning of a subroutine that must hide the floating-point exceptions it may raise from the caller. If only some exceptions must be suppressed, while others must be reported, the non-stop mode is usually ended with a call to `std::feupdateenv` after clearing the unwanted exceptions.

## Parameters


### Parameters


## Return value

`0` on success, non-zero otherwise.

## See also

