---
title: std::filesystem::last_write_time
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/last_write_time
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
std::filesystem::file_time_type last_write_time( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
std::filesystem::file_time_type last_write_time( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
dcl|num=3|since=c++17|1=
void last_write_time( const std::filesystem::path& p,
std::filesystem::file_time_type new_time );
dcl|num=4|since=c++17|1=
void last_write_time( const std::filesystem::path& p,
std::filesystem::file_time_type new_time,
std::error_code& ec ) noexcept;
```

@1,2@ Returns the time of the last modification of `p`, determined as if by accessing the member `st_mtime` of the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/stat.html `stat`] (symlinks are followed).
The non-throwing overload returns `file_time_type::min()` on errors.
@3,4@ Changes the time of the last modification of `p`, as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/futimens.html `futimens`] (symlinks are followed).

## Parameters


### Parameters

- `p` - path to examine or modify
- `new_time` - new modification time
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

@1,2@ The time of the last modification of `p`.
@3,4@ (none)

## Exceptions


## Notes

It is not guaranteed that immediately after setting the write time, the value returned by  is the same as what was passed as the argument to  because the file system's time may be more granular than `std::filesystem::file_time_type|filesystem::file_time_type`.

## Example


## See also


| cpp/filesystem/dsc file_time_type | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc last_write_time | (see dedicated page) |

