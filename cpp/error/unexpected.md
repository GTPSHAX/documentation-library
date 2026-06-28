---
title: std::unexpected
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/unexpected
---


```cpp
**Header:** `<`exception`>`
dcl rev multi|until1=c++11|dcl1=
void unexpected();
|until2=c++17|notes2=|dcl2=
noreturn void unexpected();
```

`std::unexpected()` is called by the C++ runtime when a dynamic exception specification is violated: an exception is thrown from a function whose exception specification forbids exceptions of this type.
`std::unexpected()` may also be called directly from the program.
In either case, `std::unexpected` calls the currently installed `std::unexpected_handler`. The default `std::unexpected_handler` calls `std::terminate`.
rev|until=c++11|
If a destructor reset the unexpected handler during stack unwinding and the unwinding later led to `unexpected` being called, the handler that was installed at the end of the throw expression is the one that will be called (note: it was ambiguous whether re-throwing applied the new handlers).
rev|since=c++11|
If a destructor reset the unexpected handler during stack unwinding, it is unspecified which handler is called if the unwinding later led to `unexpected` being called.

## Exceptions

Throw any exception thrown by the currently installed `std::unexpected_handler`.

## Defect reports


## See also


| cpp/utility/expected/dsc unexpected | (see dedicated page) |
| cpp/error/dsc unexpected_handler | (see dedicated page) |

