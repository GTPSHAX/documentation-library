---
title: std::vsprintf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/vfprintf
---


```cpp
**Header:** `<`cstdio`>`
dcl|num=1|
int vprintf( const char* format, std::va_list vlist );
dcl|num=2|
int vfprintf( std::FILE* stream, const char* format, std::va_list vlist );
dcl|num=3|
int vsprintf( char* buffer, const char* format, std::va_list vlist );
dcl|num=4|since=c++11|
int vsnprintf( char* buffer, std::size_t buf_size, const char* format, std::va_list vlist );
```

Loads the data from the locations, defined by `vlist`, converts them to character string equivalents and writes the results to a variety of sinks.
1. Writes the results to `stdout`.
2. Writes the results to a file stream `stream`.
3. Writes the results to a character string `buffer`.
4. Writes the results to a character string `buffer`. At most `buf_size - 1` characters are written. The resulting character string will be terminated with a null character, unless `buf_size` is zero. If `buf_size` is zero, nothing is written and `buffer` may be a null pointer, however the return value (number of bytes that would be written not including the null terminator) is still calculated and returned.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `buffer` - pointer to a character string to write to
- `buf_size` - maximum number of characters to write
- `format` - pointer to a null-terminated character string specifying how to interpret the data
- `vlist` - variable argument list containing the data to print

## Return value

@1-3@ Number of characters written if successful or negative value if an error occurred.
4. Number of characters written if successful or negative value if an error occurred. If the resulting string gets truncated due to `buf_size` limit, function returns the total number of characters (not including the terminating null-byte) which would have been written, if the limit was not imposed.

## Notes

All these functions invoke `va_arg` at least once, the value of `arg` is indeterminate after the return. These functions do not invoke `va_end`, and it must be done by the caller.

## Example


### Example

```cpp
#include <cstdarg>
#include <cstdio>
#include <ctime>
#include <vector>

void debug_log(const char *fmt, ...)
{
    std::time_t t = std::time(nullptr);
    char time_buf[100];
    std::strftime(time_buf, sizeof time_buf, "%D %T", std::gmtime(&t));
    std::va_list args1;
    va_start(args1, fmt);
    std::va_list args2;
    va_copy(args2, args1);
    std::vector<char> buf(1 + std::vsnprintf(nullptr, 0, fmt, args1));
    va_end(args1);
    std::vsnprintf(buf.data(), buf.size(), fmt, args2);
    va_end(args2);
    std::printf("%s [debug]: %s\n", time_buf, buf.data());
}

int main()
{
    debug_log("Logging, %d, %d, %d", 1, 2, 3);
}
```


**Output:**
```
04/13/15 15:09:18 [debug]: Logging, 1, 2, 3
```


## See also


| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/c/dsc vfscanf | (see dedicated page) |
| cpp/io/dsc vprint_unicode | (see dedicated page) |
| cpp/io/dsc vprint_nonunicode | (see dedicated page) |

