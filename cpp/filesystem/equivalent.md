---
title: std::filesystem::equivalent
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/equivalent
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool equivalent( const std::filesystem::path& p1,
const std::filesystem::path& p2 );
dcl|num=2|since=c++17|1=
bool equivalent( const std::filesystem::path& p1,
const std::filesystem::path& p2,
std::error_code& ec ) noexcept;
```

Checks whether the paths `p1` and `p2` resolve to the same file system entity.
If either `p1` or `p2` does not exist, an error is reported.
The non-throwing overload returns `false` on errors.

## Parameters


### Parameters

- `p1, p2` - paths to check for equivalence
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the `p1` and `p2` refer to the same file or directory and their file status is the same. `false` otherwise.

## Exceptions


## Notes

Two paths are considered to resolve to the same file system entity if the two candidate entities the paths resolve to are located on the same device at the same location. For POSIX, this means that the `st_dev` and `st_ino` members of their POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html `stat` structure], obtained as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/stat.html `stat()`], are equal.
In particular, all hard links for the same file or directory are equivalent, and a symlink and its target on the same file system are equivalent.

## Example


### Example

```cpp
#include <cstdint>
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    // hard link equivalency
    fs::path p1 = ".";
    fs::path p2 = fs::current_path();
    if (fs::equivalent(p1, p2))
        std::cout << p1 << " is equivalent to " << p2 << '\n';

    // symlink equivalency
    for (const fs::path lib : {"/lib/libc.so.6", "/lib/x86_64-linux-gnu/libc.so.6"})
    {
        try
        {
            p2 = lib.parent_path() / fs::read_symlink(lib);
        }
        catch (std::filesystem::filesystem_error const& ex)
        {
            std::cout << ex.what() << '\n';
            continue;
        }

        if (fs::equivalent(lib, p2))
            std::cout << lib << " is equivalent to " << p2 << '\n';
    }
}
```


**Output:**
```
"." is equivalent to "/var/tmp/test"
filesystem error: read_symlink: No such file or directory [/lib/libc.so.6]
"/lib/x86_64-linux-gnu/libc.so.6" is equivalent to "/lib/x86_64-linux-gnu/libc-2.23.so"
```


## Defect reports


## See also


| cpp/filesystem/path/dsc compare | (see dedicated page) |
| cpp/filesystem/path/dsc operator_cmp | (see dedicated page) |
| cpp/filesystem/dsc status | (see dedicated page) |

