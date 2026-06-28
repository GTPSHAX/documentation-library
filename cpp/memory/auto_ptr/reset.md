---
title: std::auto_ptr::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/reset
---


```cpp
dcl|deprecated=c++11|removed=c++17|1=
void reset( T* p = 0 ) throw();
```

Replaces the held pointer by `p`. If the currently held pointer is not null pointer, `delete get()` is called.

## Parameters


### Parameters

- `p` - a pointer to an object to manage

## Return value

(none)

## See also


| cpp/memory/auto_ptr/dsc release | (see dedicated page) |

