---
title: csetjmp
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/csetjmp
---

This header is part of the program support library.


| cpp/utility/program/dsc jmp_buf | (see dedicated page) |
| cpp/utility/program/dsc setjmp | (see dedicated page) |
| cpp/utility/program/dsc longjmp | (see dedicated page) |


## Synopsis


```cpp
#define __STDC_VERSION_SETJMP_H__ 202311L

namespace std {
  using jmp_buf = /* see description */ ;
  [[noreturn]] void longjmp(jmp_buf env, int val);
}

#define setjmp(env) /* see description */
```

