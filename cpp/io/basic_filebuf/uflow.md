---
title: std::basic_filebuf::uflow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/uflow
---

ddcl |
protected:
virtual int_type uflow()
Behaves like the `underflow()`, except that if `underflow()` succeeds (does not return `Traits::eof()`), then advances the next pointer for the get area. In other words, consumes one of the characters obtained by `underflow()`.

## Parameters

(none)

## Return value

The value of the character that was read and consumed in case of success, or `Traits::eof()` in case of failure.

## Example


## See also

de:cpp/io/basic filebuf/uflow
es:cpp/io/basic filebuf/uflow
fr:cpp/io/basic filebuf/uflow
it:cpp/io/basic filebuf/uflow
ja:cpp/io/basic filebuf/uflow
pt:cpp/io/basic filebuf/uflow
ru:cpp/io/basic filebuf/uflow
zh:cpp/io/basic filebuf/uflow
