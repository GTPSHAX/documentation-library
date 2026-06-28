---
title: std::filesystem::is_directory
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_directory
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_directory( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool is_directory( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool is_directory( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to a directory.
1. Equivalent to `1=s.type() == file_type::directory`.
@2,3@ Equivalent to `is_directory(status(p))` or `is_directory(status(p, ec))`, respectively.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to query
- `ec` - error code to modify in case of errors

## Return value

`true` if the file indicated by `p` or if the type indicated `s` refers to a directory, `false` otherwise. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |
| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_directory | (see dedicated page) |

