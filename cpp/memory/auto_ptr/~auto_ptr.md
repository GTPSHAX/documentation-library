---
title: std::auto_ptr::~auto_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/~auto_ptr
---


```cpp
dcl | deprecated=c++11 | removed=c++17 |
~auto_ptr() throw();
```

Destroys the managed object. Calls `delete get()`.
