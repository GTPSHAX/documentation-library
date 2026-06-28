---
title: std::basic_stringbuf::init_buf_ptrs
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/init_buf_ptrs
---

ddcl|notes=|1=
void init_buf_ptrs();
Initializes the input and output sequences from `buf` according to `mode`. `buf` and `mode` are `exposition-only data members` of `*this`.
Immediately after this function returns:
* If `std::ios_base::out` is set in `mode`,  points to `buf.front()` and `1=epptr() >= pbase() + buf.size()` is `true`;
** in addition, if `std::ios_base::ate` is set in `mode`, `1=pptr() == pbase() + buf.size()` is `true`,
** otherwise `1=pptr() == pbase()` is `true`.
* If `std::ios_base::in` is set in `mode`,  points to `buf.front()`, and `1=gptr() == eback() && egptr() == eback() + buf.size()` is `true`.

## Notes

For efficiency reasons, stream buffer operations can violate invariants of `buf` while it is held encapsulated in the `std::basic_stringbuf`, e.g., by writing to characters in the range [buf.data() + buf.size(), buf.data() + buf.capacity()).
All operations retrieving a `std::basic_string` from `buf` ensure that the `std::basic_string` invariants hold on the returned value.

## Defect reports

