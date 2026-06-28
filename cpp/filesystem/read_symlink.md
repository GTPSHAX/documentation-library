---
title: std::filesystem::read_symlink
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/read_symlink
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
std::filesystem::path read_symlink( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
std::filesystem::path read_symlink( const std::filesystem::path& p,
std::error_code& ec );
```

If the path `p` refers to a symbolic link, returns a new path object which refers to the target of that symbolic link.
It is an error if `p` does not refer to a symbolic link.
The non-throwing overload returns an empty path on errors.

## Parameters


### Parameters

- `p` - path to a symlink
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The target of the symlink (which may not necessarily exist).

## Exceptions


## Example


### Example


**Output:**
```
"/usr/bin/gcc" -> "gcc-5"
"/bin/cat" exists but it is not a symlink
"/bin/mouse" does not exist
```


## See also


| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc create_symlink | (see dedicated page) |
| cpp/filesystem/dsc copy_symlink | (see dedicated page) |
| cpp/filesystem/dsc status | (see dedicated page) |

