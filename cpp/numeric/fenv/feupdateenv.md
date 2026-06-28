---
title: std::feupdateenv
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feupdateenv
---


```cpp
dcl | since=c++11 |
int feupdateenv( const std::fenv_t* envp )
```

First, remembers the currently raised floating-point exceptions, then restores the floating-point environment from the object pointed to by `envp` (similar to `std::fesetenv`), then raises the floating-point exceptions that were saved.
This function may be used to end the non-stop mode established by an earlier call to `std::feholdexcept`.

## Parameters


### Parameters


## Return value

`0` on success, non-zero otherwise.

## See also

