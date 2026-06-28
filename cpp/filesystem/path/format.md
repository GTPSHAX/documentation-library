---
title: std::filesystem::path::format
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/format
---


```cpp
dcl | since=c++17 | 1=
enum format {
native_format,
generic_format,
auto_format
};
```

Determines how string representations of pathnames are interpreted by the constructors of `cpp/filesystem/path|std::filesystem::path` that accept strings.

## Constants


| Item | Description |
|------|-------------|
| **Name** | Explanation |


## Notes

On POSIX systems, there is no difference between native and generic format.

## See also

