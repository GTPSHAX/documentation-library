---
title: va_end
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variadic/va_end
---


```cpp
**Header:** `<`cstdarg`>`
dcl|
void va_end( std::va_list ap );
```

The `va_end` macro performs cleanup for an `ap` object initialized by a call to `va_start` or `va_copy`. `va_end` may modify `ap` so that it is no longer usable.
If there is no corresponding call to `va_start` or `va_copy`, or if `va_end` is not called before a function that calls `va_start` or `va_copy` returns, the behavior is undefined.

## Parameters


### Parameters

- `ap` - an instance of the `va_list` type to clean up

## Expanded value

(none)

## See also


| cpp/utility/variadic/dsc va_start | (see dedicated page) |
| cpp/utility/variadic/dsc va_copy | (see dedicated page) |
| cpp/utility/variadic/dsc va_arg | (see dedicated page) |

