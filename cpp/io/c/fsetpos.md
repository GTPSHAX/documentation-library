---
title: std::fsetpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fsetpos
---

ddcl | header=cstdio |
int fsetpos( std::FILE* stream, const std::fpos_t* pos );
Sets the file position indicator and the multibyte parsing state (if any) for the C file stream `stream` according to the value pointed to by `pos`.
Besides establishing new parse state and position, a call to this function undoes the effects of `std::ungetc` and clears the end-of-file state, if it is set.
If a read or write error occurs, the error indicator (`std::ferror`) for the stream is set.

## Parameters


### Parameters


## Return value

`0` upon success, nonzero value otherwise. Also, sets `errno` on failure.

## Notes

After seeking to a non-end position in a wide stream, the next call to any output function may render the remainder of the file undefined, e.g. by outputting a multibyte sequence of a different length.

## Example


## See also

