---
title: std::filesystem::is_block_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_block_file
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_block_file( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool is_block_file( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool is_block_file( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to a block special file, as if determined by the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html `S_ISBLK`]. Examples of block special files are block devices such as `/dev/sda` or `/dev/loop0` on Linux.
1. Equivalent to `1=s.type() == file_type::block`.
@2,3@ Equivalent to `is_block_file(status(p))` or `is_block_file(status(p, ec))`.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the file indicated by `p` or if the type indicated `s` refers to a block device. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_block_file | (see dedicated page) |

