---
title: std::filesystem::is_socket
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_socket
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_socket( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool is_socket( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool is_socket( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to a named IPC socket, as if determined by the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html `S_IFSOCK`].
1. Equivalent to `1=s.type() == file_type::socket`.
@2,3@ Equivalent to `is_socket(status(p))` or `is_socket(status(p, ec))`.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the file indicated by `p` or if the type indicated `s` refers to a named socket. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Notes

Named sockets are UNIX domain sockets constructed with [https://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html `socket`] and [https://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html `bind`] POSIX APIs, which may be used for advanced interprocess communication. In particular, they may be used to transport open file descriptors from one running process to another.

## Example


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |
| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_socket | (see dedicated page) |

