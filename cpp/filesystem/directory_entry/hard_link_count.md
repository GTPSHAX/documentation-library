---
title: std::filesystem::directory_entry::hard_link_count
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/hard_link_count
---


```cpp
dcl|num=1|since=c++17|
std::uintmax_t hard_link_count() const;
dcl|num=2|since=c++17|
std::uintmax_t hard_link_count( std::error_code& ec ) const noexcept;
```

If the number of hard links is cached in this `directory_entry`, returns the cached value. Otherwise, returns:
1. `std::filesystem::hard_link_count(path())`,
2. `std::filesystem::hard_link_count(path(), ec)`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The number of hard links for the referred-to filesystem object.

## Exceptions


## Example

