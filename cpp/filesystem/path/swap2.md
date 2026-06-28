---
title: std::filesystem::swap(std::filesystem::path)
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/swap2
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|
void swap( std::filesystem::path& lhs, std::filesystem::path& rhs ) noexcept;
```

Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - paths whose states to swap

## Return value

(none)

## See also


| cpp/filesystem/path/dsc swap | (see dedicated page) |

