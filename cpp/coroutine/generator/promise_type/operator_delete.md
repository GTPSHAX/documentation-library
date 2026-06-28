---
title: std::generator::promise_type::operator delete
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/operator_delete
---


# small|generator<Ref,V,Allocator>::promise_type::

operator delete
ddcl|since=c++23|
void operator delete( void* ptr, std::size_t n ) noexcept;
Deallocates the storage pointed to by `ptr` using an allocator equivalent to that used to `allocate` this memory.
The `ptr` passed to this function must be the one returned from an invocation of one of the `operator new` overloads with a size argument equal to `n`. Otherwise the behavior is undefined.

## Parameters


### Parameters

- `ptr` - a pointer obtained from the previous call to `operator new`
- `n` - the size of the storage to be deallocated
