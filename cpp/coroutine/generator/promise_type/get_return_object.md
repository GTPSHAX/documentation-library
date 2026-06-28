---
title: std::generator::promise_type::get_return_object
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/get_return_object
---


# small|generator<Ref,V,Allocator>::promise_type::

get_return_object
ddcl|since=c++23|
std::generator get_return_object() noexcept;
Returns a  object whose member  is obtained via the expression `std::coroutine_handle<promise_type>::from_promise(*this)`,
and whose member  points to an empty stack.

## Parameters

(none)

## Return value

The  object.
