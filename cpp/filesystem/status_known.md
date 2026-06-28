---
title: std::filesystem::status_known
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/status_known
---


```cpp
dcl | num=1 | since=c++17 | 1=
bool status_known( std::filesystem::file_status s ) noexcept;
```

Checks if the given file status is known, equivalent to `1=s.type() != file_type::none`.

## Parameters


### Parameters


## Return value

`true` if the given file status is a known file status.

## Notes

Despite the name, the function checks for the file status of `std::filesystem::file_type::none|file_type::none` (meaning an error occurred), not `std::filesystem::file_type::unknown|file_type::unknown` (meaning file exists, but its type cannot be determined).

## See also

