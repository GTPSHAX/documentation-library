---
title: std::filesystem::symlink_status
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/status
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|num=1|
std::filesystem::file_status status( const std::filesystem::path& p );
dcl|since=c++17|num=2|
std::filesystem::file_status status( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
dcl|since=c++17|num=3|
std::filesystem::file_status symlink_status( const std::filesystem::path& p );
dcl|since=c++17|num=4|
std::filesystem::file_status symlink_status( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
```

@1,2@ Determines the type and attributes of the filesystem object identified by `p` as if by POSIX  (symlinks are followed to their targets). In the following description, `prms` is the result of `(m & perms::mask)`, where `m` is obtained as if by taking `st_mode` from the POSIX `struct stat` and converting it to the type `std::filesystem::perms`.
:* If `p` is a regular file (as if by POSIX `S_ISREG`), returns `file_status(file_type::regular, prms)`.
:* If `p` is a directory (as if by POSIX `S_ISDIR`), returns `file_status(file_type::directory, prms)`.
:* If `p` is a block special file (as if by POSIX `S_ISBLK`), returns `file_status(file_type::block, prms)`.
:* If `p` is a character special file (as if by POSIX `S_ISCHR`), returns `file_status(file_type::character, prms)`.
:* If `p` is a fifo or pipe file (as if by POSIX `S_ISFIFO`), returns `file_status(file_type::fifo, prms)`.
:* If `p` is a socket (as if by POSIX `S_ISSOCK`), returns `file_status(file_type::socket, prms)`.
:* If `p` has an implementation-defined file type, returns `file_status(file_type::A, prms)` where `A` is the implementation-defined `cpp/filesystem/file_type|file_type` constant for that type.
:* If `p` does not exist, returns `file_status(file_type::not_found)`.
:* If `p` exists but file attributes cannot be determined, e.g. due to lack of permissions, returns `file_status(file_type::unknown)`.
:* If errors prevent even knowing whether `p` exists, the non-throwing overload sets `ec` and returns `file_status(file_type::none)`, and the throwing overload throws `filesystem_error`.
:* Otherwise, returns `file_status(file_type::unknown, prms)`.
@3,4@ Same as  except that the behavior is as if the POSIX  is used (symlinks are not followed):
:* If `p` is a symlink, returns `file_status(file_type::symlink)`.

## Parameters


### Parameters

- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The file status (a `std::filesystem::file_status|filesystem::file_status` object).

## Exceptions


## Notes

The information provided by this function is usually also provided as a byproduct of directory iteration, and may be obtained by the member functions of `std::filesystem::directory_entry|filesystem::directory_entry`. During directory iteration, calling `status` again is unnecessary.

## Example


## See also


| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |
| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc status | (see dedicated page) |

