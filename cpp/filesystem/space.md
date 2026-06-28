---
title: std::filesystem::space
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/space
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|
std::filesystem::space_info space( const std::filesystem::path& p );
dcl|num=2|since=c++17|
std::filesystem::space_info space( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
```

Determines the information about the filesystem on which the pathname `p` is located, as if by POSIX .
Populates and returns an object of type `filesystem::space_info`, set from the members of the POSIX `struct statvfs` as follows:
* `space_info.capacity` is set as if by `f_blocks * f_frsize`.
* `space_info.free` is set to `f_bfree * f_frsize`.
* `space_info.available` is set to `f_bavail * f_frsize`.
* Any member that could not be determined is set to `static_cast<std::uintmax_t>(-1)`.
The non-throwing overload sets all members to `static_cast<std::uintmax_t>(-1)` on error.

## Parameters


### Parameters

- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The filesystem information (a `filesystem::space_info` object).

## Exceptions


## Notes

`space_info.available` may be less than `space_info.free`.

## Example


## See also


| cpp/filesystem/dsc space_info | (see dedicated page) |

