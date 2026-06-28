---
title: std::filesystem::directory_entry::directory_entry
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/directory_entry
---


```cpp
dcl|since=c++17|num=1|1=
directory_entry() noexcept = default;
dcl|since=c++17|num=2|1=
directory_entry( const directory_entry& ) = default;
dcl|since=c++17|num=3|1=
directory_entry( directory_entry&& ) noexcept = default;
dcl|since=c++17|num=4|1=
explicit directory_entry( const std::filesystem::path& p );
dcl|since=c++17|num=5|1=
directory_entry( const std::filesystem::path& p, std::error_code& ec );
```

Constructs a new `directory_entry` object.
1. Default constructor.
2. Defaulted copy constructor.
3. Defaulted move constructor.
@4,5@ Initializes the directory entry with path `p` and calls `cpp/filesystem/directory_entry/refresh|refresh` to update the cached attributes. If an error occurs, the non-throwing overload leaves the `directory_entry` holding a default-constructed path.

## Parameters


### Parameters

- `p` - path to the filesystem object to which the directory entry will refer
- `ec` - out-parameter for error reporting in the non-throwing overload

## Exceptions


## Example

