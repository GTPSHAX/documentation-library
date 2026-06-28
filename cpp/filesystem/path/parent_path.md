---
title: std::filesystem::path::parent_path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/parent_path
---


```cpp
dcl|since=c++17|1=
path parent_path() const;
```

Returns the path to the parent directory.
If `has_relative_path()` returns false, the result is a copy of `*this`.
Otherwise, the result is a path whose generic format pathname is the longest prefix of the generic format pathname of `*this` that produces one fewer element in its iteration.

## Parameters

(none)

## Return value

The path to the parent directory, or a copy of `*this` if not `has_relative_path()`.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    for (fs::path p : {"/var/tmp/example.txt", "/", "/var/tmp/."})
        std::cout << "The parent path of " << p
                  << " is " << p.parent_path() << '\n';
}
```


**Output:**
```
The parent path of "/var/tmp/example.txt" is "/var/tmp"
The parent path of "/" is "/"
The parent path of "/var/tmp/." is "/var/tmp"
```


## See also


| cpp/filesystem/path/dsc root_name | (see dedicated page) |
| cpp/filesystem/path/dsc root_directory | (see dedicated page) |
| cpp/filesystem/path/dsc root_path | (see dedicated page) |

