---
title: std::filesystem::path::relative_path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/relative_path
---


```cpp
dcl|since=c++17|1=
path relative_path() const;
```

Returns path relative to *root-path*, that is, a pathname composed of every generic-format component of `*this` after *root-path*. If `*this` is an empty path, returns an empty path.

## Parameters

(none)

## Return value

Path relative to the `root path`.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::path p = fs::current_path();

    std::cout << "The current path " << p << " decomposes into:\n"
              << "root-path " << p.root_path() << '\n'
              << "relative path " << p.relative_path() << '\n';
}
```


**Output:**
```
The current path "C:\Users\abcdef\Local Settings\temp" decomposes into:
root-path "C:\"
relative path "Users\abcdef\Local Settings\temp"
```


## See also


| cpp/filesystem/path/dsc root_name | (see dedicated page) |
| cpp/filesystem/path/dsc root_directory | (see dedicated page) |
| cpp/filesystem/path/dsc root_path | (see dedicated page) |

