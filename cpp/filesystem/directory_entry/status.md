---
title: std::filesystem::directory_entry::symlink_status
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/status
---


```cpp
dcl|since=c++17|num=1|
std::filesystem::file_status status() const;
dcl|since=c++17|num=2|
std::filesystem::file_status status( std::error_code& ec ) const noexcept;
dcl|since=c++17|num=3|
std::filesystem::file_status symlink_status() const;
dcl|since=c++17|num=4|
std::filesystem::file_status symlink_status( std::error_code& ec ) const noexcept;
```

@1,2@ Returns status of the entry, as if determined by a `std::filesystem::status|filesystem::status` call (symlinks are followed to their targets).
@3,4@ Returns status of the entry, as if determined by a `std::filesystem::symlink_status|filesystem::symlink_status` call (symlinks are not followed).

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The status of the file referred to by the entry.

## Exceptions


## Notes


## Example


## See also


| cpp/filesystem/directory_entry/dsc refresh | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_directory | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_other | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_socket | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc file_size | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc hard_link_count | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc last_write_time | (see dedicated page) |

