---
title: std::filesystem::create_hard_link
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/create_hard_link
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void create_hard_link( const std::filesystem::path& target,
const std::filesystem::path& link );
dcl|num=2|since=c++17|1=
void create_hard_link( const std::filesystem::path& target,
const std::filesystem::path& link,
std::error_code& ec ) noexcept;
```

Creates a hard link `link` with its target set to `target` as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/link.html `link()`]: the pathname `target` must exist.
Once created, `link` and `target` are two logical names that refer to the same file (they are `cpp/filesystem/equivalent|equivalent`). Even if the original name `target` is deleted, the file continues to exist and is accessible as `link`.

## Parameters


### Parameters

- `target` - path of the file or directory to link to
- `link` - path of the new hard link
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Notes

Some operating systems do not support hard links at all or support them only for regular files.
Some file systems do not support hard links regardless of the operating system: the FAT file system used on memory cards and flash drives, for example.
Some file systems limit the number of links per file.
Hardlinking to directories is typically restricted to the superuser.
Hard links typically cannot cross filesystem boundaries.
The special pathname dot (`"."`) is a hard link to its parent directory. The special pathname dot-dot `".."` is a hard link to the directory that is the parent of its parent.

## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::create_directories("sandbox/subdir");
    std::ofstream("sandbox/a").put('a'); // create regular file
    fs::create_hard_link("sandbox/a", "sandbox/b");
    fs::remove("sandbox/a");
    // read from the original file via surviving hard link
    char c = std::ifstream("sandbox/b").get();
    std::cout << c << '\n';
    fs::remove_all("sandbox");
}
```


**Output:**
```
a
```


## See also


| cpp/filesystem/dsc create_symlink | (see dedicated page) |
| cpp/filesystem/dsc hard_link_count | (see dedicated page) |

