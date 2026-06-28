---
title: std::basic_syncbuf::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/operator=
---


```cpp
dcl |1=
basic_syncbuf& operator=( basic_syncbuf&& other );
```

First, calls `cpp/io/basic_syncbuf/emit|emit()` to transmit all pending output (and delayed flush, if any) to the wrapped stream.
Then performs move-assignment by moving all contents from `other`, including the temporary storage, the wrapped stream pointer, policy, and all other state (such as the mutex pointer). After move, `other` is not associated with a stream, and `1=other.get_wrapped() == nullptr`. The put area member pointers of the base class `std::basic_streambuf` of `other` are guaranteed to be null. Destroying a moved-from `other` will not produce any output.
If `std::allocator_traits<Allocator>::propagate_on_container_move_assignment::value` is `false`, then the allocator is unchanged. Otherwise, after move-assignment, `get_allocator()` equals `other.get_allocator()`.

## Parameters


### Parameters

- `other` -  another std::basic_syncbuf to move from

## Return value

`*this`

## Example

