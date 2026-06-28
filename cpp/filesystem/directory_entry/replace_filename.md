---
title: std::filesystem::directory_entry::replace_filename
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/replace_filename
---


```cpp
dcl|num=1|since=c++17|1=
void replace_filename( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
void replace_filename( const std::filesystem::path& p, std::error_code& ec );
```

Changes the filename of the directory entry.
Effectively modifies the path member by `path.replace_filename(p)` and calls `cpp/filesystem/directory_entry/refresh|refresh` to update the cached attributes. If an error occurs, the values of the cached attributes are unspecified.
This function does not commit any changes to the filesystem.

## Parameters


### Parameters

- `p` - the path to append to the parent path of the currently stored path
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    {
        fs::directory_entry entry{"alpha"};
        std::cout << entry << '\n';
        entry.replace_filename("omega");
        std::cout << entry << '\n';
    }
    {
        fs::directory_entry entry{"/alpha/"};
        std::cout << entry << '\n';
        entry.replace_filename("omega");
        std::cout << entry << '\n';
    }
}
```


**Output:**
```
"alpha"
"omega"
"/alpha/"
"/alpha/omega"
```


## See also


| cpp/filesystem/directory_entry/dsc assign | (see dedicated page) |
| cpp/filesystem/path/dsc replace_filename | (see dedicated page) |

