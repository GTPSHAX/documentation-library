---
title: std::generator::promise_type::return_void
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/return_void
---


# small|generator<Ref,V,Allocator>::promise_type::

return_void
ddcl|since=c++23|
void return_void() const noexcept {}
No-op. A user provided coroutine that uses the  cannot issue a value via `co_return` operator or reaching the end of the coroutine body.
