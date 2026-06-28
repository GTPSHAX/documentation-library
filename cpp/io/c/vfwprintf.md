---
title: std::vwprintf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/vfwprintf
---


```cpp
dcl | num=1 |
int vwprintf( const wchar_t* format, va_list vlist );
dcl | num=2 |
int vfwprintf( std::FILE* stream, const wchar_t* format, va_list vlist );
dcl | num=3 |
int vswprintf( wchar_t* buffer, std::size_t buf_size, const wchar_t* format, va_list vlist );
```

Loads the data from locations, defined by `vlist`,, converts them to wide string equivalents and writes the results to a variety of sinks.
1. Writes the results to `stdout`.
2. Writes the results to a file stream `stream`.
3. Writes the results to a wide string `buffer`. At most `size-1` wide characters are written followed by null wide character.

## Parameters


### Parameters


## Return value

@1,2@ Number of wide characters written if successful or negative value if an error occurred.
3. Number of wide characters written (not counting the terminating null wide character) if successful or negative value if an encoding error occurred or if the number of characters to be generated was equal or greater than `size`.

## Notes

While narrow strings provide `std::vsnprintf`, which makes it possible to determine the required output buffer size, there is no equivalent for wide strings, and in order to determine the buffer size, the program may need to call `std::vswprintf`, check the result value, and reallocate a larger buffer, trying again until successful.

## Example


## See also

