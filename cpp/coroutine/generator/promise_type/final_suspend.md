---
title: std::generator::promise_type::final_suspend
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/promise_type/final_suspend
---


# small|generator<Ref,V,Allocator>::promise_type::

final_suspend
ddcl|since=c++23|
auto final_suspend() noexcept;
Let `x` be some  object. `final_suspend` does the following:
# Pops the coroutine handle from the top of .
# If `*x.active_` is not empty, resumes execution of the coroutine referred to by `x.active_->top()`. If it is empty, control flow returns to the current coroutine caller or resumer.
A handle referring to the coroutine whose promise object is `*this` must be at the top of `*x.active_` of `x`.

## Return value

An awaitable object of unspecified type whose member functions are configured to suspend the calling coroutine.
