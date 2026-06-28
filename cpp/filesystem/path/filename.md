---
title: std::filesystem::path::filename
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/filename
---


```cpp
dcl|since=c++17|1=
path filename() const;
```

Returns the generic-format filename component of the path.
Equivalent to `relative_path().empty() ? path() : *--end()`.

## Parameters

(none)

## Return value

The filename identified by the path.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << fs::path("/foo/bar.txt").filename() << '\n'
              << fs::path("/foo/.bar").filename() << '\n'
              << fs::path("/foo/bar/").filename() << '\n'
              << fs::path("/foo/.").filename() << '\n'
              << fs::path("/foo/..").filename() << '\n'
              << fs::path(".").filename() << '\n'
              << fs::path("..").filename() << '\n'
              << fs::path("/").filename() << '\n'
              << fs::path("//host").filename() << '\n';
}
<!-- |p=true -->
```


**Output:**
```
"bar.txt"
".bar"
""
"."
".."
"."
".."
""
"host"
```


## See also


| cpp/filesystem/path/dsc extension | (see dedicated page) |
| cpp/filesystem/path/dsc stem | (see dedicated page) |
| cpp/filesystem/path/dsc replace_filename | (see dedicated page) |

