---
title: std::filesystem::path::root_directory
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/root_directory
---


```cpp
dcl|since=c++17|1=
path root_directory() const;
```

Returns the root directory of the generic-format path. If the path (in generic format) does not include root directory, returns `path()`.

## Parameters

(none)

## Return value

The root directory of the path.

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
              << "root name " << p.root_name() << '\n'
              << "root directory " << p.root_directory() << '\n'
              << "relative path " << p.relative_path() << '\n';
}
```


**Output:**
```
The current path "C:\Users\abcdef\Local Settings\temp" decomposes into:
root name "C:"
root directory "\"
relative path "Users\abcdef\Local Settings\temp"
```


## See also


| cpp/filesystem/path/dsc root_name | (see dedicated page) |
| cpp/filesystem/path/dsc root_path | (see dedicated page) |

