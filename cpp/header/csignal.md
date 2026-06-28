---
title: csignal
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/csignal
---

This header is part of the program support library.


| cpp/utility/program/sig_atomic_t|the integer type that can be accessed as an atomic entity from an asynchronous signal handler | |
| cpp/utility/program/dsc SIG_types | (see dedicated page) |
| cpp/utility/program/dsc SIG_strategies | (see dedicated page) |
| cpp/utility/program/dsc SIG_ERR | (see dedicated page) |
| cpp/utility/program/dsc signal | (see dedicated page) |
| cpp/utility/program/dsc raise | (see dedicated page) |


## Synopsis


```cpp
namespace std {
  using sig_atomic_t = /*see description*/ ;
  extern "C" using /*signal-handler*/ = void(int); // exposition only
  /*signal-handler*/ * signal(int sig, /*signal-handler*/ * func);
}
#define SIG_DFL  /* see description */
#define SIG_ERR  /* see description */
#define SIG_IGN  /* see description */
#define SIGABRT  /* see description */
#define SIGFPE   /* see description */
#define SIGILL   /* see description */
#define SIGINT   /* see description */
#define SIGSEGV  /* see description */
#define SIGTERM  /* see description */
```

