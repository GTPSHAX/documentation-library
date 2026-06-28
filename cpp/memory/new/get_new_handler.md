---
title: std::get_new_handler
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/get_new_handler
---


```cpp
dcl | since=c++11 |1=
std::new_handler get_new_handler() noexcept;
```

Returns the currently installed new-handler, which may be a null pointer.
This function is thread-safe. Previous call to `std::set_new_handler` ''synchronizes-with'' (see `std::memory_order`) the subsequent calls to `std::get_new_handler`.

## Parameters

(none)

## Return value

The currently installed ''new-handler'', which may be a null pointer value.

## See also

