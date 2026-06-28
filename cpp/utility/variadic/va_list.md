---
title: std::va_list
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variadic/va_list
---

`va_list` is a complete object type (in practice, a unique built-in type or `char*`) suitable for holding the information needed by the macros `va_start`, `va_copy`, `va_arg`, and `va_end`.
If a `va_list` instance is created, passed to another function, and used via `va_arg` in that function, then any subsequent use in the calling function should be preceded by a call to `va_end`.
It is legal to pass a pointer to a `va_list` object to another function and then use that object after the function returns.

## Example

