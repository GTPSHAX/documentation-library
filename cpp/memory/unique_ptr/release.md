---
title: std::unique_ptr::release
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/release
---

ddcl | since=c++11 | notes= | 1=
pointer release() noexcept;
Releases the ownership of the managed object, if any.
`get()` returns `nullptr` after the call.
The caller is responsible for cleaning up the object (e.g. by use of `get_deleter()`).

## Parameters

(none)

## Return value

Pointer to the managed object or `nullptr` if there was no managed object, i.e. the value which would be returned by `get()` before the call.

## Example


## See also

