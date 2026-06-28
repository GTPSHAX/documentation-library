---
title: std::vsscanf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/vfscanf
---


```cpp
**Header:** `<`cstdio`>`
dcl|num=1|since=c++11|
int vscanf( const char* format, std::va_list vlist );
dcl|num=2|since=c++11|
int vfscanf( std::FILE* stream, const char* format, std::va_list vlist );
dcl|num=3|since=c++11|
int vsscanf( const char* buffer, const char* format, std::va_list vlist );
```

Reads data from a variety of sources, interprets it according to `format` and stores the results into locations defined by `vlist`.
1. Reads the data from `stdin`.
2. Reads the data from file stream `stream`.
3. Reads the data from null-terminated character string `buffer`.

## Parameters


### Parameters

- `stream` - input file stream to read from
- `buffer` - pointer to a null-terminated character string to read from
- `format` - pointer to a null-terminated character string specifying how to read the input
- `vlist` - variable argument list containing the receiving arguments.

## Return value

Number of arguments successfully read, or `EOF` if failure occurs.

## Notes

All these functions invoke `va_arg` at least once, the value of `arg` is indeterminate after the return. These functions to not invoke `va_end`, and it must be done by the caller.

## Example


### Example

```cpp
#include <cstdarg>
#include <cstdio>
#include <iostream>
#include <stdexcept>

void checked_sscanf(int count, const char* buf, const char *fmt, ...)
{
    std::va_list ap;
    va_start(ap, fmt);
    if (std::vsscanf(buf, fmt, ap) != count)
        throw std::runtime_error("parsing error");
    va_end(ap);
}

int main()
{
    try
    {
        int n, m;
        std::cout << "Parsing '1 2'... ";
        checked_sscanf(2, "1 2", "%d %d", &n, &m);
        std::cout << "success\n";
        std::cout << "Parsing '1 a'... ";
        checked_sscanf(2, "1 a", "%d %d", &n, &m);
        std::cout << "success\n";
    }
    catch (const std::exception& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
Parsing '1 2'... success
Parsing '1 a'... parsing error
```


## See also


| cpp/io/c/dsc fscanf | (see dedicated page) |
| cpp/io/c/dsc vfprintf | (see dedicated page) |

