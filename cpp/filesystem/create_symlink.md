---
title: std::filesystem::create_symlink
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/create_symlink
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void create_symlink( const std::filesystem::path& target,
const std::filesystem::path& link );
dcl|num=2|since=c++17|1=
void create_symlink( const std::filesystem::path& target,
const std::filesystem::path& link,
std::error_code& ec ) noexcept;
dcl|num=3|since=c++17|1=
void create_directory_symlink( const std::filesystem::path& target,
const std::filesystem::path& link );
dcl|num=4|since=c++17|1=
void create_directory_symlink( const std::filesystem::path& target,
const std::filesystem::path& link,
std::error_code& ec ) noexcept;
```

Creates a symbolic link `link` with its target set to `target` as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/symlink.html `symlink()`]: the pathname `target` may be invalid or non-existing.
Some operating systems require symlink creation to identify that the link is to a directory. Portable code should use  to create directory symlinks rather than , even though there is no distinction on POSIX systems.

## Parameters


### Parameters

- `target` - path to point the symlink to, does not have to exist
- `link` - path of the new symbolic link
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Notes

Some operating systems do not support symbolic links at all or support them only for regular files.
Some file systems do not support symbolic links regardless of the operating system, for example the FAT system used on some memory cards and flash drives.
Like a hard link, a symbolic link allows a file to have multiple logical names. The presence of a hard link guarantees the existence of a file, even after the original name has been removed. A symbolic link provides no such assurance; in fact, the file named by the `target` argument need not exist when the link is created. A symbolic link can cross file system boundaries.

## Example


### Example

```cpp
#include <cassert>
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::create_directories("sandbox/subdir");
    fs::create_symlink("target", "sandbox/sym1");
    fs::create_directory_symlink("subdir", "sandbox/sym2");

    for (auto it = fs::directory_iterator("sandbox"); it != fs::directory_iterator(); ++it)
        if (is_symlink(it->symlink_status()))
            std::cout << *it << "->" << read_symlink(*it) << '\n';

    assert(std::filesystem::equivalent("sandbox/sym2", "sandbox/subdir"));
    fs::remove_all("sandbox");
}
```


**Output:**
```
"sandbox/sym1"->"target"
"sandbox/sym2"->"subdir"
```


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc read_symlink | (see dedicated page) |
| cpp/filesystem/dsc create_hard_link | (see dedicated page) |

