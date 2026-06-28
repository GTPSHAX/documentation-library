---
title: std::filesystem::directory_entry::is_other
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_other
---


```cpp
dcl|num=1|since=c++17|
bool is_other() const;
dcl|num=2|since=c++17|
bool is_other( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is an ''other'' file  (not a regular file, directory or symlink). Effectively returns:
1. `std::filesystem::is_other(status())`.
2. `std::filesystem::is_other(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is an ''other'' file, `false` otherwise.

## Exceptions


## Example


## See also


| cpp/filesystem/dsc is_other | (see dedicated page) |

