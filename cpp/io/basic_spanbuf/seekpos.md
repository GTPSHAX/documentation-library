---
title: std::basic_spanbuf::seekpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/seekpos
---

ddcl | since=c++23 | 1=
protected:
pos_type seekpos( pos_type sp, std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out ) override;
Repositions the next pointer to the get and/or put area, if possible, to the position indicated by `sp`.
Equivalent to `return seekoff(off_type(sp), std::ios_base::beg, which);`.

## Parameters


### Parameters


## Return value

`sp` on success or `pos_type(off_type(-1))` on failure.

## Notes

`seekpos()` is called by `std::basic_streambuf::pubseekpos()`, which is called by the single-argument versions of `std::basic_istream::seekg()` and `std::basic_ostream::seekp()`.

## Example

