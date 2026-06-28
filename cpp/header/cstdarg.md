---
title: cstdarg
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cstdarg
---

This header provides support for C-style variadic functions, while the C definition of "default argument promotions" is replaced with the C++ definition.


| cpp/utility/variadic/dsc va_list | (see dedicated page) |
| cpp/utility/variadic/dsc va_start | (see dedicated page) |
| cpp/utility/variadic/dsc va_arg | (see dedicated page) |
| cpp/utility/variadic/dsc va_copy | (see dedicated page) |
| cpp/utility/variadic/dsc va_end | (see dedicated page) |


## Synopsis


```cpp
#define __STDC_VERSION_STDARG_H__ 202311L

namespace std {
  using va_list = /* see description */ ;
}

#define va_arg(V, P)        /* see description */
#define va_copy(VDST, VSRC) /* see description */
#define va_end(V)           /* see description */
#define va_start(V, ...)    /* see description */
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2645 | C++98 | C++ defines “default argument promotions”, but its C definition was used | the C++ definition overrides the C definition |

