---
title: std::basic_syncbuf::set_emit_on_sync
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/set_emit_on_sync
---


```cpp
dcl | 1=
void set_emit_on_sync( bool b ) noexcept;
```

Changes the current emit-on-sync policy.
The value `false` (the default) indicates that any flush will be postponed until a call to emit.
The value `true` makes flushes apply immediately.

## Parameters


### Parameters

- `b` -  new value for the emit-on-sync policy

## Example

