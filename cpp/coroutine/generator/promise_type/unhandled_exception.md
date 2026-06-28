---
title: std::generator::promise_type::unhandled_exception
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/unhandled_exception
---


# small|generator<Ref,V,Allocator>::promise_type::

unhandled_exception
ddcl|since=c++23|
void unhandled_exception();
Let `x` be some  object.
If a handle referring to the coroutine whose `promise object` is `*this` is at the top of  of `x`:
* If the handle referring to the coroutine whose promise object is `*this` is the only element of `*x.active_`, equivalent to `throw;`.
* Otherwise, assigns `std::current_exception()` to .
Otherwise, the behavior is undefined.

## Exceptions

May throw.
