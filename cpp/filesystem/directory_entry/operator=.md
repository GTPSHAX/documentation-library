---
title: std::filesystem::directory_entry::operator=
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/operator=
---


```cpp
dcl | since=c++17 | num=1 | 1=
directory_entry& operator=( const directory_entry& other ) = default;
dcl | since=c++17 | num=2 | 1=
directory_entry& operator=( directory_entry&& other ) noexcept = default;
```

Replaces the contents of the directory entry (path and cached attributes, if any) with the contents of `other`.
Both copy- and move-assignment operators for `directory_entry` are defaulted.

## Parameters


### Parameters


## Return value

`*this`

## Example

