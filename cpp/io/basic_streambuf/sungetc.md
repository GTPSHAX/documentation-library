---
title: std::basic_streambuf::sungetc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sungetc
---

ddcl | 1=
int_type sungetc();
If a putback position is available in the get area (`gptr() > eback()`), then decrements the next pointer (`gptr()`) and returns the character it now points to.
If a putback position is not available, then calls `pbackfail()` to back up the input sequence if possible.
The I/O stream function  is implemented in terms of this function.

## Parameters

(none)

## Return value

If putback position was available, returns the character that the next pointer is now pointing at, converted to `int_type` with `Traits::to_int_type(*gptr())`. The next single-character input from this streambuf will return this character.
If putback position was not available, returns what `pbackfail()` returns, which is  `Traits::eof()` on failure.

## Example


## See also

