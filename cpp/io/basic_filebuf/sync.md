---
title: std::basic_filebuf::sync
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/sync
---

ddcl |
protected:
virtual int sync()
If a put area exists (e.g. the file was opened for writing), calls `overflow()` to write all pending output to the file, then flushes the file as if by calling `std::fflush`.
If a get area exists (e.g. the file was opened for reading), the effect is implementation-defined. Typical implementation may empty out the get area and move the current file position back by the corresponding number of bytes.

## Parameters

(none)

## Return value

`0` in case of success, `-1` in case of failure.

## Notes

`sync()` or its equivalent is implicitly called for output streams by `close()`, `seekoff()`, and `seekpos()` and explicitly called by `std::basic_streambuf::pubsync()`

## Example


## See also

de:cpp/io/basic filebuf/sync
es:cpp/io/basic filebuf/sync
fr:cpp/io/basic filebuf/sync
it:cpp/io/basic filebuf/sync
ja:cpp/io/basic filebuf/sync
pt:cpp/io/basic filebuf/sync
ru:cpp/io/basic filebuf/sync
zh:cpp/io/basic filebuf/sync
