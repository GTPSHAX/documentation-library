---
title: std::fopen
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fopen
---

ddcl|header=cstdio|
std::FILE* fopen( const char* filename, const char* mode );
Opens a file indicated by `filename` and returns a file stream associated with that file. `mode` is used to determine the file access mode.

## Parameters


### Parameters

- `filename` - file name to associate the file stream to
- `mode` - null-terminated character string determining file access mode

## File access flags


## Return value

If successful, returns a pointer to the object that controls the opened file stream, with both eof and error bits cleared. The stream is fully buffered unless *filename* refers to an interactive device.
On error, returns a null pointer. [https://pubs.opengroup.org/onlinepubs/9699919799/functions/fopen.html POSIX requires] that `errno` is set in this case.

## Notes

The format of `filename` is implementation-defined, and does not necessarily refer to a file (e.g. it may be the console or another device accessible through filesystem API). On platforms that support them, `filename` may include absolute or relative filesystem path.
For portable directory and file naming, see C++ filesystem library or [https://www.boost.org/doc/libs/release/libs/filesystem/doc/index.htm boost.filesystem].

## Example


## See also


| cpp/io/c/dsc fclose | (see dedicated page) |
| cpp/io/c/dsc fflush | (see dedicated page) |
| cpp/io/c/dsc freopen | (see dedicated page) |

