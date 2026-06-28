---
title: std::stacktrace_entry::native_handle
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/native_handle
---

ddcl | since=c++23 |
constexpr native_handle_type native_handle() const noexcept;
Returns the implementation-defined underlying native handle. Successive invocations of this function for an unchanged `stacktrace_entry` object return identical values.
The semantics of this function is implementation-defined.

## Parameters

(none)

## Return value

Underlying native handle.

## Example

