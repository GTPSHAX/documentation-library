---
title: std::basic_filebuf::native_handle
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/native_handle
---

ddcl|since=c++26|
native_handle_type native_handle() const noexcept;
Returns the implementation defined underlying handle associated with `*this`. The behavior is undefined if `is_open()` is `false`.

## Return value

implementation defined handle.

## Notes


## Example

