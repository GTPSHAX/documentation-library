---
title: std::fputs
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fputs
---

ddcl|header=cstdio|
int fputs( const char* str, std::FILE* stream );
Writes every character from the null-terminated string `str` to the output stream `stream`, as if by repeatedly executing `std::fputc`.
The terminating null character from `str` is not written.

## Parameters


### Parameters

- `str` - null-terminated character string to be written
- `stream` - output stream

## Return value

On success, returns a non-negative value
On failure, returns `EOF` and sets the ''error'' indicator (see `std::ferror`) on `stream`.

## Notes

The related function `std::puts` appends a newline character to the output, while `std::fputs` writes the string unmodified.
Different implementations return different non-negative numbers: some return the last character written, some return the number of characters written (or `INT_MAX` if the string was longer than that), some simply return a non-negative constant such as zero.

## Example


### Example


**Output:**
```
Hello World
```


## See also


| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/c/dsc puts | (see dedicated page) |
| cpp/io/c/dsc fputws | (see dedicated page) |
| cpp/io/c/dsc fgets | (see dedicated page) |

