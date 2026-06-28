---
title: std::fflush
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fflush
---

ddcl|header=cstdio|
int fflush( std::FILE* stream );
For output streams (and for update streams on which the last operation was output), writes any unwritten data from the `stream`'s buffer to the associated output device.
For input streams (and for update streams on which the last operation was input), the behavior is undefined.
rrev|since=c++26|
If any data are written to an output device, returning from `std::fflush` establishes an observable checkpoint.
If `stream` is a null pointer, the flushing operation specified above are performed on all open output streams, including the ones manipulated within library packages or otherwise not directly accessible to the program.

## Parameters


### Parameters

- `stream` - the file stream to write out

## Return value

Returns `0` on success. Otherwise returns `EOF` and sets the error indicator of the file stream.

## Notes

POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/fflush.html extends the specification of `fflush`] by defining its effects on an input stream, as long as that stream represents a file or another seekable device: in that case the POSIX file pointer is repositioned to match the C stream pointer (which effectively undoes any read buffering) and the effects of any `std::ungetc` or `std::ungetwc` that weren't yet read back from the stream are discarded.
Microsoft also extends the specification of `fflush` by defining its effects on an input stream: in Visual Studio 2013 and prior, it [https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/9yky46tz(v=vs.120) discarded the input buffer], in Visual Studio 2015 and newer, it [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/fflush?view=msvc-140 has no effect, buffers are retained].

## See also


| cpp/io/c/dsc fopen | (see dedicated page) |
| cpp/io/c/dsc fclose | (see dedicated page) |

