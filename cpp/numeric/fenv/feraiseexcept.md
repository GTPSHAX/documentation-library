---
title: std::feraiseexcept
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feraiseexcept
---


```cpp
**Header:** `<`cfenv`>`
dcl|since=c++11|
int feraiseexcept( int excepts );
```

Attempts to raise all floating point exceptions listed in `excepts` (a bitwise OR of the floating point exception macros). If one of the exceptions is `FE_OVERFLOW` or `FE_UNDERFLOW`, this function may additionally raise `FE_INEXACT`. The order in which the exceptions are raised is unspecified, except that `FE_OVERFLOW` and `FE_UNDERFLOW` are always raised before `FE_INEXACT`.

## Parameters


### Parameters

- `excepts` - bitmask listing the exception flags to raise

## Return value

`0` if all listed exceptions were raised, non-zero value otherwise.

## Example


### Example

```cpp
#include <cfenv>
#include <iostream>

// #pragma STDC FENV_ACCESS ON

int main()
{
    std::feclearexcept(FE_ALL_EXCEPT);
    const int r = std::feraiseexcept(FE_UNDERFLOW {{!
```

std::cout << "Raising divbyzero and underflow simultaneously "
<< (r ? "fails" : "succeeds") << " and results in\n";
const int e = std::fetestexcept(FE_ALL_EXCEPT);
if (e & FE_DIVBYZERO)
std::cout << "division by zero\n";
if (e & FE_INEXACT)
std::cout << "inexact\n";
if (e & FE_INVALID)
std::cout << "invalid\n";
if (e & FE_UNDERFLOW)
std::cout << "underflow\n";
if (e & FE_OVERFLOW)
std::cout << "overflow\n";
}
|output=
Raising divbyzero and underflow simultaneously succeeds and results in
division by zero
underflow

## See also


| cpp/numeric/fenv/dsc feclearexcept | (see dedicated page) |
| cpp/numeric/fenv/dsc fetestexcept | (see dedicated page) |

