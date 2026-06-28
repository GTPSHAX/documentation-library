---
title: std::pointer_traits::to_address
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/pointer_traits/to_address
---


```cpp
**Header:** `<`memory`>`
|
static element_type* to_address( pointer p ) noexcept;
```

Constructs a raw pointer that references the same object as its pointer-like ("fancy pointer") argument.
This function, if defined, is the inverse of `pointer_to`, and exists as the customization point to be called by `cpp/memory/to_address|std::to_address`.

## Parameters


### Parameters

- `p` - fancy pointer/pointer-like object

## Return value

A raw pointer of the type `element_type*` that references the same memory location as the argument `p`.

## See also


| cpp/memory/pointer_traits/dsc pointer_to | (see dedicated page) |
| cpp/memory/dsc to_address | (see dedicated page) |

