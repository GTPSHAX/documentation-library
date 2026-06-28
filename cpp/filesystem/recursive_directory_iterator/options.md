---
title: std::filesystem::recursive_directory_iterator::options
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator/options
---


```cpp
dcl | since=c++17 | 1=
std::filesystem::directory_options options() const;
```

Returns the options that affect the directory iteration. The options can only be supplied when constructing the directory iterator.
If the options argument was not supplied, returns `std::filesystem::directory_options::none`.

## Parameters

(none)

## Return value

The effective options that affect the directory iteration.

## Exceptions

Throws nothing.
