---
title: std::basic_filebuf::is_open
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/is_open
---

ddcl |
bool is_open() const;
Returns `true` if the most recent call to `open()` succeeded and there has been no call to `close()` since then.

## Parameters

(none)

## Return value

`true` if the associated file is open, `false` otherwise.

## Notes

This function is typically called by `std::basic_fstream::is_open()`.

## Example


## See also

de:cpp/io/basic filebuf/is open
es:cpp/io/basic filebuf/is open
fr:cpp/io/basic filebuf/is open
it:cpp/io/basic filebuf/is open
ja:cpp/io/basic filebuf/is open
pt:cpp/io/basic filebuf/is open
ru:cpp/io/basic filebuf/is open
zh:cpp/io/basic filebuf/is open
