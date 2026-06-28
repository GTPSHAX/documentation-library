---
title: std::freopen
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/freopen
---

ddcl|header=cstdio|
std::FILE* freopen( const char* filename, const char* mode, std::FILE* stream );
First, attempts to close the file associated with `stream`, ignoring any errors. Then, if `filename` is not null, attempts to open the file specified by `filename` using `mode` as if by `std::fopen`, and associates that file with the file stream pointed to by `stream`. If `filename` is a null pointer, then the function attempts to reopen the file that is already associated with `stream` (it is implementation defined which mode changes are allowed in this case).

## Parameters


### Parameters

- `filename` - file name to associate the file stream to
- `mode` - null-terminated character string determining new file access mode
- `stream` - the file stream to modify

## File access flags


## Return value

`stream` on success, a null pointer on failure.

## Notes

`std::freopen` is the only way to change the narrow/wide orientation of a stream once it has been established by an I/O operation or by `std::fwide`.
Microsoft CRT version of `std::freopen` does not support any mode changes when `filename` is a null pointer and treats this as an error (see [https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/freopen-wfreopen documentation]). A possible workaround is the non-standard function [https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setmode `_setmode()`].

## Example


### Example

```cpp
#include <cstdio>

int main()
{
    std::printf("stdout is printed to console\n");
    if (std::freopen("redir.txt", "w", stdout))
    {
        std::printf("stdout is redirected to a file\n"); // this is written to redir.txt
        std::fclose(stdout);
    }
}
```


**Output:**
```
stdout is printed to console
```


## See also


| cpp/io/c/dsc fopen | (see dedicated page) |
| cpp/io/c/dsc fclose | (see dedicated page) |

