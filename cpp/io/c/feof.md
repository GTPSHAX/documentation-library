---
title: std::feof
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/feof
---

ddcl|header=cstdio|
int feof( std::FILE* stream );
Checks if the end of the given file stream has been reached.

## Parameters


### Parameters

- `stream` - the file stream to check

## Return value

Nonzero value if the end of the stream has been reached, otherwise `0`.

## Notes

This function only reports the stream state as reported by the most recent I/O operation, it does not examine the associated data source. For example, if the most recent I/O was a `std::fgetc`, which returned the last byte of a file, `std::feof` returns zero. The next `std::fgetc` fails and changes the stream state to ''end-of-file''. Only then `std::feof` returns non-zero.
In typical usage, input stream processing stops on any error; `feof` and `std::ferror` are then used to distinguish between different error conditions.

## Example

