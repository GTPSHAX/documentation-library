---
title: std::basic_syncbuf::get_wrapped
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/get_wrapped
---


```cpp
dcl | 1=
streambuf_type* get_wrapped() const noexcept;
```

Returns a pointer to the wrapped `std::basic_streambuf`.

## Parameters

(none)

## Notes

This function is not expected to be called directly: it is called through `cpp/io/basic_osyncstream/get_wrapped|std::basic_osyncstream::get_wrapped`.

## Example

