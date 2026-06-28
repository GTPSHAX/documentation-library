---
title: std::generator::promise_type::initial_suspend
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/initial_suspend
---


# small|generator<Ref,V,Allocator>::promise_type::

initial_suspend
ddcl|since=c++23|
std::suspend_always initial_suspend() const noexcept;
Informs that  always starts lazily (in suspended state).
Equivalent to }.

## Return value

An awaitable object.
