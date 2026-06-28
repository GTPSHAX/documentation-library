---
title: std::filesystem::directory_entry::is_symlink
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_symlink
---


```cpp
dcl|num=1|since=c++17|
bool is_symlink() const;
dcl|num=2|since=c++17|
bool is_symlink( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a symlink. Effectively returns:
1. `std::filesystem::is_symlink(symlink_status())`,
2. `std::filesystem::is_symlink(symlink_status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a symlink, `false` otherwise.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc is_symlink | (see dedicated page) |

