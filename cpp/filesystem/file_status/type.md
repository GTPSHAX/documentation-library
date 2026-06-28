---
title: std::filesystem::file_status::type
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_status/type
---


```cpp
dcl | since=c++17  | num=1 | 1=
std::filesystem::file_type type() const noexcept;
dcl | since=c++17  | num=2 | 1=
void type( std::filesystem::file_type type ) noexcept;
```

Accesses the file type information.
1. Returns file type information.
2. Sets file type to `type`.

## Parameters


### Parameters


## Return value

1. File type information.
2. (none)

## Example

