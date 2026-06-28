---
title: std::filesystem::file_status::file_status
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_status/file_status
---


```cpp
dcl|since=c++17|num=1|1=
file_status() noexcept : file_status(std::filesystem::file_type::none) {}
dcl|since=c++17|num=2|1=
file_status( const file_status& ) noexcept = default;
dcl|since=c++17|num=3|1=
file_status( file_status&& ) noexcept = default;
dcl|since=c++17|num=4|1=
explicit file_status(
std::filesystem::file_type type,
std::filesystem::perms permissions = std::filesystem::perms::unknown ) noexcept;
```

Constructs a new `file_status` object.
1. Default constructor that calls  with `std::filesystem::file_type::none`.
@2,3@ Copy and move constructors are defaulted.
4. Initializes the file status object with `type` as type and `permissions` as permissions.

## Parameters


### Parameters

- `type` - type of the file status
- `permissions` - permissions of the file status

## Example

