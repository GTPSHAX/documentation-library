---
title: operator==(std::filesystem::file_status)
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_status/operator==
---


# 1=operator==<small>(std::filesystem::file_status)</small>


```cpp
dcl | since=c++20 | 1=
friend bool operator==( const file_status& lhs, const file_status& rhs ) noexcept;
```

Checks if two `file_status` values are equal, i.e. types and permissions represented by them are same respectively.

## Parameters


### Parameters


## Return value

`1=lhs.type() == rhs.type() && lhs.permissions() == rhs.permissions()`

## See also

