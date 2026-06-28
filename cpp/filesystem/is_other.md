---
title: std::filesystem::is_other
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_other
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_other( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool is_other( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool is_other( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to a file of type ''other'' type. That is, the file exists, but is neither regular file, nor directory nor a symlink.
1. Equivalent to `exists(s) && !is_regular_file(s) && !is_directory(s) && !is_symlink(s)`.
@2,3@ Equivalent to `is_other(status(p))` or `is_other(status(p, ec))`, respectively.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to examine
- `ec` - error code to store the error status to

## Return value

`true` if the file indicated by `p` or if the type indicated `s` refers to a file that is not regular file, directory, or a symlink, `false` otherwise. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Example

