---
title: std::filesystem::is_character_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_character_file
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_character_file( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool is_character_file( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool is_character_file( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to a character special file, as if determined by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html `S_ISCHR`]. Examples of character special files are character devices such as `/dev/null`, `/dev/tty`, `/dev/audio`, or `/dev/nvram` on Linux.
1. Equivalent to `1=s.type() == file_type::character`.
@2,3@ Equivalent to `is_character_file(status(p))` or `is_character_file(status(p, ec))` respectively.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the file indicated by `p` or if the type indicated `s` refers to a character device, `false` otherwise. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |
| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_character_file | (see dedicated page) |

