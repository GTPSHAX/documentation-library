---
title: std::filesystem::file_status::operator=
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_status/operator=
---


```cpp
dcl | since=c++17 | num=1 | 1=
file_status& operator=( const file_status& other ) noexcept = default;
dcl | since=c++17 | num=2 | 1=
file_status& operator=( file_status&& other ) noexcept = default;
```

Copy- or move-assigns another file status object.

## Parameters


### Parameters


## Return value

`*this`

## Example

