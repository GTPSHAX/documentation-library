---
title: std::filesystem::file_status::permissions
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_status/permissions
---


```cpp
dcl|since=c++17|num=1|1=
std::filesystem::perms permissions() const noexcept;
dcl|since=c++17|num=2|1=
void permissions( std::filesystem::perms perm ) noexcept;
```

Accesses the file permissions information.
1. Returns file permissions information.
2. Sets file permissions to `perm`.

## Parameters


### Parameters

- `perm` - file permissions to set to

## Return value

1. File permissions information.
2. (none)

## Example

