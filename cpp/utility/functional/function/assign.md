---
title: std::function::assign
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/assign
---

ddcl | since=c++11 | removed=c++17 |
template< class F, class Alloc >
void assign( F&& f, const Alloc& alloc );
Initializes the ''target'' with `f`. The `alloc` is used to allocate memory for any internal data structures that the `function` might use.
Equivalent to `function(std::allocator_arg, alloc, std::forward<F>(f)).swap(*this);`.

## Parameters


### Parameters


## Return value

(none)

## See also

