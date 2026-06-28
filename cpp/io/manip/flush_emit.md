---
title: std::flush_emit
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/flush_emit
---

ddcl | header=ostream | since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>& flush_emit( std::basic_ostream<CharT, Traits>& os );
Flushes the output sequence `os` as if by calling `os.flush()`. Then, if `os.rdbuf()` actually points to a `std::basic_syncbuf<CharT, Traits, Allocator>` `buf`, calls `buf.emit()`.
This is an output-only I/O manipulator, it may be called with an expression such as `out << std::flush_emit` for any `out` of type `std::basic_ostream`.

## Parameters


### Parameters


## Return value

`os` (reference to the stream after manipulation)

## Example

