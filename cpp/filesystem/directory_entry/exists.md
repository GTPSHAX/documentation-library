---
title: std::filesystem::directory_entry::exists
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/exists
---


```cpp
dcl|num=1|since=c++17|1=
bool exists() const;
dcl|num=2|since=c++17|1=
bool exists( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object exists. Effectively returns:
1. `std::filesystem::exists(status())`,
2. `std::filesystem::exists(status(ec))`.
Note that  follows symlinks to their targets.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object exists.

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    for (auto const str:
    {
        "/usr/bin/cat",
        "/usr/bin/mouse",
        "/usr/bin/python",
        "/usr/bin/bison",
        "/usr/bin/yacc",
        "/usr/bin/c++",
    })
    {
        std::filesystem::directory_entry entry{str};

        std::cout << "directory entry " << entry
                  << (entry.exists() ? " exists\n" : " does not exist\n");
    }
}
```


**Output:**
```
// Output on a POSIX system:
directory entry "/usr/bin/cat" exist
directory entry "/usr/bin/mouse" does not exist
directory entry "/usr/bin/python" exists
directory entry "/usr/bin/bison" exists
directory entry "/usr/bin/yacc" does not exist
directory entry "/usr/bin/c++" exists
```


## See also


| cpp/filesystem/dsc exists | (see dedicated page) |

