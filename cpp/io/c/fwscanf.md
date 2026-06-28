---
title: std::wscanf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fwscanf
---


```cpp
dcl | num=1 |
int wscanf( const wchar_t* format, ... );
dcl | num=2 |
int fwscanf( std::FILE* stream, const wchar_t* format, ... );
dcl | num=3 |
int swscanf( const wchar_t* buffer, const wchar_t* format, ... );
```

Reads data from the a variety of sources, interprets it according to `format` and stores the results into given locations.
1. Reads the data from `stdin`.
2. Reads the data from file stream `stream`.
3. Reads the data from null-terminated wide string `buffer`.

## Parameters


### Parameters


## Return value

Number of arguments successfully read, or `EOF` if failure occurs before the first receiving argument was assigned.

## Example


## See also

