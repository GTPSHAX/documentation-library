---
title: std::basic_ios::eof
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/eof
---


```cpp
dcl | 1=
bool eof() const;
```

Returns `true` if the associated stream has reached end-of-file. Specifically, returns `true` if `eofbit` is set in `rdstate()`.
See  for the list of conditions that set `eofbit`.

## Parameters

(none)

## Return value

`true` if an end-of-file has occurred, `false` otherwise.

## Notes

This function only reports the stream state as set by the most recent I/O operation; it does not examine the associated data source. For example, if the most recent I/O was a `cpp/io/basic_istream/get|get()` which returned the last byte of a file, `eof()` returns `false`. The next `get()` fails to read anything and sets the `eofbit`. Only then does `eof()` return `true`.
In typical usage, input stream processing stops on any error. `eof()` and `fail()` can then be used to distinguish between different error conditions.

## Example

