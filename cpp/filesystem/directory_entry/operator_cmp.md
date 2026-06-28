---
title: std::filesystem::directory_entry::operators
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/operator_cmp
---


```cpp
dcl|num=1|since=c++17|1=
bool operator==( const directory_entry& rhs ) const noexcept;
dcl|num=2|since=c++17|until=c++20|1=
bool operator!=( const directory_entry& rhs ) const noexcept;
dcl|num=3|since=c++17|until=c++20|1=
bool operator<( const directory_entry& rhs ) const noexcept;
dcl|num=4|since=c++17|until=c++20|1=
bool operator<=( const directory_entry& rhs ) const noexcept;
dcl|num=5|since=c++17|until=c++20|1=
bool operator>( const directory_entry& rhs ) const noexcept;
dcl|num=6|since=c++17|until=c++20|1=
bool operator>=( const directory_entry& rhs ) const noexcept;
dcl|num=7|since=c++20|1=
std::strong_ordering operator<=>( const directory_entry& rhs ) const noexcept;
```

Compares the path with the directory entry `rhs`.
rrev|since=c++20|

## Parameters


### Parameters

- `rhs` - directory_entry to compare

## Return value

1. `true` if `1=path() == rhs.path()`, `false` otherwise.
2. `true` if `1=path() != rhs.path()`, `false` otherwise.
3. `true` if `1=path() < rhs.path()`, `false` otherwise.
4. `true` if `1=path() <= rhs.path()`, `false` otherwise.
5. `true` if `1=path() > rhs.path()`, `false` otherwise.
6. `true` if `1=path() >= rhs.path()`, `false` otherwise.
7. The result of `1=path() <=> rhs.path()`.

## See also


| cpp/filesystem/directory_entry/dsc path | (see dedicated page) |

