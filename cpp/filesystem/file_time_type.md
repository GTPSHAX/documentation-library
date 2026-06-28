---
title: std::filesystem::file_time_type
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_time_type
---


```cpp
dcl rev multi | since1=c++17  | dcl1=
using file_time_type = std::chrono::time_point</*trivial-clock*/>;
|since2=c++20|dcl2=
using file_time_type = std::chrono::time_point<std::chrono::file_clock>;
```

Represents file time.
and is sufficient to represent the resolution and range of the file time values offered by the filesystem.

## Example


## See also

