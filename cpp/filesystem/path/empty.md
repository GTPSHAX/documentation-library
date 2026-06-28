---
title: std::filesystem::path::empty
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/empty
---


```cpp
dcl| since=c++17 |
bool empty() const noexcept;
```

Checks if the path in generic format is empty.

## Parameters

(none)

## Return value

`true` if the path is empty, `false` otherwise.

## Notes

An empty path can be obtained by calling `cpp/filesystem/path/clear|clear` and by default-constructing a `path`. It can also be returned by a path decomposition function (such as `cpp/filesystem/path/extension|extension`) if the corresponding component is not present in the path.
An empty path is classified as a relative path.

## See also

