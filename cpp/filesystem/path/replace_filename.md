---
title: std::filesystem::path::replace_filename
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/replace_filename
---


```cpp
dcl|since=c++17|1=
path& replace_filename( const path& replacement );
```

Replaces a single filename component with `replacement`.
Equivalent to: `1=remove_filename(); return operator/=(replacement);`.

## Parameters


### Parameters

- `replacement` - `path` used for replacing the filename component

## Return value

`*this`

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << fs::path("/foo").replace_filename("bar") << '\n'
              << fs::path("/").replace_filename("bar") << '\n'
              << fs::path("").replace_filename("pub") << '\n';
}
```


**Output:**
```
"/bar"
"/bar"
"pub"
```


## See also


| cpp/filesystem/path/dsc replace_extension | (see dedicated page) |
| cpp/filesystem/path/dsc filename | (see dedicated page) |
| cpp/filesystem/path/dsc remove_filename | (see dedicated page) |

