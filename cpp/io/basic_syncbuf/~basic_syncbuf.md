---
title: std::basic_syncbuf::~basic_syncbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/~basic_syncbuf
---


```cpp
dcl |1=
~basic_syncbuf();
```

Calls `cpp/io/basic_syncbuf/emit|emit()` to transmit all pending output (and delayed flush, if any) to the wrapped stream. If an exception is thrown by this call, it is caught and ignored.

## Parameters

(none)

## Notes

Normally called by the destructor of the owning `std::basic_osyncstream`.

## Example

