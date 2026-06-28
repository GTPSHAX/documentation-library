---
title: std::basic_syncbuf::sync
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/sync
---


```cpp
dcl | 1=
protected:
int sync() override;
```

First, records that a flush is pending, by updating the appropriate private flag.
Then, if the current emit-on-sync policy is `true`, makes a call to `cpp/io/basic_syncbuf/emit|emit()`.
Otherwise (if the emit-on-sync policy is `false`, which is the default), the flush is suspended until `cpp/io/basic_syncbuf/emit|emit()` is called, such as through `cpp/io/basic_osyncstream/emit|std::basic_osyncstream::emit()` or `cpp/io/basic_osyncstream/~basic_osyncstream|std::basic_osyncstream::~basic_osyncstream`

## Parameters

(none)

## Notes

`sync()` or its equivalent is implicitly called by `close()`, `seekoff()`, and `seekpos()` and explicitly called by `std::basic_streambuf::pubsync()`

## Example

