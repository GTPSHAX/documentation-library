---
title: std::filesystem::path::root_path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/root_path
---


```cpp
dcl|since=c++17|
path root_path() const;
```

Returns the root path of the path. If the path does not include root path, returns `path()`.
Effectively returns `root_name() / root_directory()`.

## Parameters

(none)

## Return value

The root path of the path.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << "Current root path is: " << fs::current_path().root_path() << '\n';
}
```


**Output:**
```
Current root path is: "C:\"
```


## See also


| cpp/filesystem/path/dsc root_name | (see dedicated page) |
| cpp/filesystem/path/dsc root_directory | (see dedicated page) |

