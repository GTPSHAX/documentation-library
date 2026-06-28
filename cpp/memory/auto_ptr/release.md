---
title: std::auto_ptr::release
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr/release
---


```cpp
dcl | deprecated=c++11 | removed=c++17 |
T* release() throw();
```

Releases the held pointer. After the call `*this` holds the null pointer.

## Parameters

(none)

## Return value

`get()`.

## See also

