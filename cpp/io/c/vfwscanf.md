---
title: std::vwscanf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/vfwscanf
---


```cpp
**Header:** `<`cwchar`>`
dcl|num=1|since=c++11|
int vwscanf( const wchar_t* format, std::va_list vlist );
dcl|num=2|since=c++11|
int vfwscanf( std::FILE* stream, const wchar_t* format, std::va_list vlist );
dcl|num=3|since=c++11|
int vswscanf( const wchar_t* buffer, const wchar_t* format, std::va_list vlist );
```

Reads data from the a variety of sources, interprets it according to `format` and stores the results into locations defined by `vlist`.
1. Reads the data from `stdin`.
2. Reads the data from file stream `stream`.
3. Reads the data from null-terminated wide string `buffer`.

## Parameters


### Parameters

- `stream` - input file stream to read from
- `buffer` - pointer to a null-terminated wide string to read from
- `format` - pointer to a null-terminated wide string specifying how to read the input
- `vlist` - variable argument list containing the receiving arguments.

## Return value

Number of arguments successfully read, or `EOF` if failure occurs.

## Example


## See also


| cpp/io/c/dsc fwscanf | (see dedicated page) |

