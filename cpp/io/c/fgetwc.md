---
title: std::fgetwc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fgetwc
---


```cpp
**Header:** `<`cwchar`>`
dcl|
std::wint_t fgetwc( std::FILE* stream );
dcl|
std::wint_t getwc( std::FILE* stream );
```

Reads the next wide character from the given input stream. `getwc()` may be implemented as a macro and may evaluate `stream` more than once.

## Parameters


### Parameters

- `stream` - to read the wide character from

## Return value

The next wide character from the stream or `WEOF` if an error has occurred or the end of file has been reached. If an encoding error occurred, `errno` is set to `EILSEQ`.

## See also


| cpp/io/c/dsc fgetc | (see dedicated page) |
| cpp/io/c/dsc fgetws | (see dedicated page) |
| cpp/io/c/dsc fputwc | (see dedicated page) |
| cpp/io/c/dsc ungetwc | (see dedicated page) |

