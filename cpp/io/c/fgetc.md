---
title: std::getc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fgetc
---

ddcl|header=cstdio|
int fgetc( std::FILE* stream );
int getc( std::FILE* stream );
Reads the next character from the given input stream.

## Parameters


### Parameters

- `stream` - to read the character from

## Return value

The obtained character on success or `EOF` on failure.
If the failure has been caused by end of file condition, additionally sets the ''eof'' indicator (see `std::feof()`) on `stream`. If the failure has been caused by some other error, sets the ''error'' indicator (see `std::ferror()`) on `stream`.

## Example


## See also


| cpp/io/c/dsc gets | (see dedicated page) |
| cpp/io/c/dsc fputc | (see dedicated page) |
| cpp/io/c/dsc ungetc | (see dedicated page) |

