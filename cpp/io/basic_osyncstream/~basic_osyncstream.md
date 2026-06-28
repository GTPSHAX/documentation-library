---
title: std::basic_osyncstream::~basic_osyncstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream/~basic_osyncstream
---


```cpp
dcl | 1=
~basic_osyncstream();
```

Destroys a synchronized output stream.
The destruction of the member `std::basic_syncbuf` will emit any buffered output not yet emitted.

## Parameters

(none)

## Example

