---
title: std::filesystem::recursive_directory_iterator::recursion_pending
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator/recursion_pending
---


```cpp
dcl | since=c++17 | 1=
bool recursion_pending() const;
```

Returns `true` if the next increment will cause the directory currently referred to by `*this` to be iterated into.
This function returns `true` immediately after construction or an increment. Recursion can be disabled via `disable_recursion_pending()`.

## Parameters

(none)

## Return value

`true` if the next increment will iterate into the currently referred directory, `false` otherwise.

## Exceptions

Throws nothing.

## Example

