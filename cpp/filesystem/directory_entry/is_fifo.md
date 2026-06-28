---
title: std::filesystem::directory_entry::is_fifo
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_fifo
---


```cpp
dcl|num=1|since=c++17|
bool is_fifo() const;
dcl|num=2|since=c++17|
bool is_fifo( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a FIFO or pipe file. Effectively returns:
1. `std::filesystem::is_fifo(status())`.
2. `std::filesystem::is_fifo(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a FIFO or pipe file, `false` otherwise.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc is_fifo | (see dedicated page) |

