---
title: std::basic_syncbuf::emit
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/emit
---


```cpp
dcl |1=
bool emit();
```

Atomically transmits all pending output to the wrapped stream.
All `emit()` calls transferring characters to the same wrapped stream buffer object appear to execute in a total order, where each `emit()` call synchronizes-with subsequent `emit()` calls in that total order, even if these calls are made through difference instances of `std::basic_syncbuf`/`std::basic_osyncstream`. In practice, this means that emit() takes a lock uniquely associated with the wrapped stream object: for example, it could be held in a static hash map where the address of the wrapped stream is used as the key.
If a call had been made to `cpp/io/basic_syncbuf/sync|sync` since the last call to `emit()`, then also flushes the wrapped stream by calling `cpp/io/basic_streambuf/pubsync|pubsync()` on it.

## Parameters

(none)

## Return value

`true` if all of the following is true:
* there is a wrapped stream (the wrapped streambuf pointer is not null)
* all characters from the temporary storage were successfully sent into the wrapped stream
* the call to `cpp/io/basic_streambuf/pubsync|pubsync()`, if requested, also completed successfully.
Returns `false` otherwise.

## Notes

Normally called by the destructor or move assignment of the owning `std::basic_osyncstream`, or by `cpp/io/basic_osyncstream/emit|std::basic_osyncstream::emit`.

## Example

