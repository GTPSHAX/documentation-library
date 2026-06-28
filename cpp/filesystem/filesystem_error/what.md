---
title: std::filesystem::filesystem_error::what
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/filesystem_error/what
---


```cpp
dcl | since=c++17 | 1=
const char* what() const noexcept override;
```

Returns an explanatory byte string. This explanatory string contains the explanatory string passed at the time of construction. Implementations are encouraged to include the pathnames of `path1()` and `path2()` in native format and the `std::system_error::what()` string inside the returned string as well.

## Parameters

(none)

## Return value

A C-stye explanatory byte string that contains the explanatory string passed at the time of construction.

## Example

