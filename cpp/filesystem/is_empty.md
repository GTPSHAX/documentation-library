---
title: std::filesystem::is_empty
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/is_empty
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool is_empty( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
bool is_empty( const std::filesystem::path& p, std::error_code& ec );
```

Checks whether the given path refers to an empty file or directory.

## Parameters


### Parameters

- `p` - path to examine
- `ec` - error code to modify in case of error

## Return value

`true` if the path indicated by `p` refers to an empty file or directory, `false` otherwise. The non-throwing overload returns `false` if an error occurs.

## Exceptions


## Example


### Example

```cpp
#include <cstdio>
#include <filesystem>
#include <fstream>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;

    const fs::path tmp_dir{fs::temp_directory_path()};
    std::cout << std::boolalpha
              << "Temp dir: " << tmp_dir << '\n'
              << "is_empty(): " << fs::is_empty(tmp_dir) << '\n';

    const fs::path tmp_name{tmp_dir / std::tmpnam(nullptr)};
    std::cout << "Temp file: " << tmp_name << '\n';

    std::ofstream file{tmp_name.string()};
    std::cout << "is_empty(): " << fs::is_empty(tmp_name) << '\n';
    file << "cppreference.com";
    file.flush();
    std::cout << "is_empty(): " << fs::is_empty(tmp_name) << '\n'
              << "file_size(): " << fs::file_size(tmp_name) << '\n';
    file.close();
    fs::remove(tmp_name);
}
```


**Output:**
```
Temp dir: "/tmp"
is_empty(): false
Temp file: "/tmp/fileCqd9DM"
is_empty(): true
is_empty(): false
file_size(): 16
```


## Defect reports


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |

