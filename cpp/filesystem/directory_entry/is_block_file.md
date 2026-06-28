---
title: std::filesystem::directory_entry::is_block_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_block_file
---


```cpp
dcl|num=1|since=c++17|1=
bool is_block_file() const;
dcl|num=2|since=c++17|1=
bool is_block_file( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a block device. Effectively returns:
1. `std::filesystem::is_block_file(status())`.
2. `std::filesystem::is_block_file(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a block device, `false` otherwise.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc is_block_file | (see dedicated page) |

