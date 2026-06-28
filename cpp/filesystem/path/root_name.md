---
title: std::filesystem::path::root_name
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/root_name
---


```cpp
dcl|since=c++17|1=
path root_name() const;
```

Returns the root name of the generic-format path. If the path (in generic format) does not include root name, returns `path()`.

## Parameters

(none)

## Return value

The root name of the path.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << "Current root name is: " << fs::current_path().root_name() << '\n';
}
```


**Output:**
```
Current root name is: "C:"
```


## See also


| cpp/filesystem/path/dsc root_directory | (see dedicated page) |
| cpp/filesystem/path/dsc root_path | (see dedicated page) |

