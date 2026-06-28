---
title: std::filesystem::directory_entry::is_socket
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_socket
---


```cpp
dcl|num=1|since=c++17|
bool is_socket() const;
dcl|num=2|since=c++17|
bool is_socket( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a named socket. Effectively returns:
1. `std::filesystem::is_socket(status())`,
2. `std::filesystem::is_socket(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a named socket, `false` otherwise.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc is_socket | (see dedicated page) |

