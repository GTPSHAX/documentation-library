---
title: std::filesystem::copy_symlink
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/copy_symlink
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void copy_symlink( const std::filesystem::path& from,
const std::filesystem::path& to);
dcl|num=2|since=c++17|1=
void copy_symlink( const std::filesystem::path& from,
const std::filesystem::path& to,
std::error_code& ec ) noexcept;
```

Copies a symlink to another location.
1. Effectively calls `f(read_symlink(from), to)` where `f` is `cpp/filesystem/create_symlink|create_symlink` or `cpp/filesystem/create_symlink|create_directory_symlink` depending on whether `from` resolves to a file or directory.
2. Effectively calls `f(read_symlink(from, ec), to, ec)` where `f` is `cpp/filesystem/create_symlink|create_symlink` or `cpp/filesystem/create_symlink|create_directory_symlink` depending on whether `from` resolves to a file or directory.

## Parameters


### Parameters

- `from` - path to a symbolic link to copy
- `to` - destination path of the new symlink
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Example

