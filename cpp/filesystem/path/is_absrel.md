---
title: std::filesystem::path::is_absolute
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/is_absrel
---


```cpp
dcl | num=1 | since=c++17  | 1=
bool is_absolute() const;
dcl | num=2 | since=c++17  | 1=
bool is_relative() const;
```

Checks whether the path is absolute or relative. An absolute path is a path that unambiguously identifies the location of a file without reference to an additional starting location. The first version returns `true` if the path, in native format, is absolute, `false` otherwise; the second version the other way round.

## Parameters

(none)

## Return value

1. `true` if the path is absolute, `false` otherwise.
2. `false` if the path is absolute, `true` otherwise.

## Notes

The path `"/"` is absolute on a POSIX OS, but is relative on Windows.

## See also

