---
title: std::vprint_unicode
type: Input/output
source: https://en.cppreference.com/w/cpp/io/vprint_unicode
---


```cpp
**Header:** `<`print`>`
dcl|num=1|since=c++23|
void vprint_unicode( std::FILE* stream,
std::string_view fmt, std::format_args args );
dcl|num=2|since=c++23|
void vprint_unicode_buffered( std::FILE* stream,
std::string_view fmt, std::format_args args );
dcl|num=3|since=c++23|
void vprint_unicode_buffered( std::string_view fmt, std::format_args args );
```

Format `args` according to the format string `fmt`, and writes the result to the output stream.
1. Performs the following operations in order:
# Locks `stream`.
# Let `out` denote the character representation of formatting arguments provided by `args` formatted according to specifications given in `fmt`.
# Writes `out` to `stream`:
:* If `stream` refers to a terminal that is only capable of displaying Unicode via a native Unicode API, flushes `stream` and writes `out` to the terminal using the native Unicode API.
:* Otherwise, writes unmodified `out` to the `stream`.
@@ Unconditionally unlocks `stream` on function exit.
@@ If any of the following conditions is satisfied, the behavior is undefined:
* `stream` is not a valid pointer to an output C stream.
* `out` contains invalid Unicode [Character encoding#Terminology|code units](https://en.wikipedia.org/wiki/Character encoding#Terminology|code units) when the native Unicode API is used.

```cpp
std::string out = std::vformat(fmt, args);
std::vprint_unicode(stream, "{}", std::make_format_args(out));
```

3. Equivalent to `std::vprint_unicode_buffered(stdout, fmt, args)`.
rrev|since=c++26|
After writing characters to the output stream, establishes an observable checkpoint.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `fmt` - 
- `args` - arguments to be formatted

## Exceptions


## Notes

The C++ standard encourages the implementers to produce a diagnostic message if `out` contains invalid Unicode code units.
On POSIX, writing to a terminal is done using the usual standard I/O functions, so there is no need to treat a terminal differently to any other file stream.
On Windows, the stream refers to a terminal if `GetConsoleMode(_get_osfhandle(_fileno(stream)))` returns nonzero (see Windows documentation for [https://docs.microsoft.com/en-us/windows/console/getconsolemode `GetConsoleMode`], [https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-osfhandle `_get_osfhandle`], and [https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fileno `_fileno`]). The native Unicode API on Windows is [https://docs.microsoft.com/en-us/windows/console/writeconsole `WriteConsoleW`].
If invoking the native Unicode API requires transcoding, the invalid code units are substituted with `U+FFFD` REPLACEMENT CHARACTER (see "The Unicode Standard - Core Specification", Chapter 3.9).

## Example


### Example

```cpp
<!--
#include <print>

int main()
{
}
-->
```


## Defect reports


## See also


| cpp/io/dsc vprint_nonunicode | (see dedicated page) |
| cpp/io/basic_ostream/dsc vprint_unicode | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |


## External links

