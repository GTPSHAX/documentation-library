---
title: std::new_handler
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/new_handler
---


```cpp
**Header:** `<`new`>`
dcl|1=
typedef void (*new_handler)();
```

`std::new_handler` is the function pointer type (pointer to function that takes no arguments and returns void), which is used by the functions `std::set_new_handler` and `std::get_new_handler`.

## See also


| cpp/memory/new/dsc operator_new | (see dedicated page) |
| cpp/memory/new/dsc set_new_handler | (see dedicated page) |
| cpp/memory/new/dsc get_new_handler | (see dedicated page) |

