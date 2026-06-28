---
title: std::noemit_on_flush
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/emit_on_flush
---


```cpp
**Header:** `<`ostream`>`
dcl| num=1 | since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>& emit_on_flush( std::basic_ostream<CharT, Traits>& os );
dcl| num=2 | since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>& noemit_on_flush( std::basic_ostream<CharT, Traits>& os );
```

If `os.rdbuf()` actually points to a `std::basic_syncbuf<CharT, Traits, Allocator>` `buf`, toggles whether it emits (i.e., transmits data to the underlying stream buffer) when flushed:
1. calls `buf.set_emit_on_sync(true)`
2. calls `buf.set_emit_on_sync(false)`
Otherwise, these manipulators have no effect.
This is an output-only I/O manipulator, it may be called with an expression such as `out << std::emit_on_flush` for any `out` of type `std::basic_ostream`.

## Parameters


### Parameters


## Return value

`os` (reference to the stream after manipulation)

## Example

