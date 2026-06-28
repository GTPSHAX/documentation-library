---
title: std::fputws
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fputws
---

ddcl|header=cwchar|
int fputws( const wchar_t* str, std::FILE* stream );
Writes every wide character from the null-terminated wide string `str` to the output stream `stream`, as if by repeatedly executing `std::fputwc`.
The terminating null wide character from `str` is not written.

## Parameters


### Parameters

- `str` - null-terminated wide string to be written
- `stream` - output stream

## Return value

On success, returns a non-negative value
On failure, returns `EOF` and sets the ''error'' indicator (see `std::ferror`) on `stream`.

## Example


### Example


**Output:**
```
御休みなさい
```


## See also


| cpp/io/c/dsc fputs | (see dedicated page) |
| cpp/io/c/dsc fwprintf | (see dedicated page) |
| cpp/io/c/dsc fputws | (see dedicated page) |
| cpp/io/c/dsc fgetws | (see dedicated page) |

