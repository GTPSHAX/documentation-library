---
title: std::filesystem::rename
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/rename
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void rename( const std::filesystem::path& old_p,
const std::filesystem::path& new_p );
dcl|num=2|since=c++17|1=
void rename( const std::filesystem::path& old_p,
const std::filesystem::path& new_p,
std::error_code& ec ) noexcept;
```

Moves or renames the filesystem object identified by `old_p` to `new_p` as if by the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html `rename`]:
* If `old_p` is a non-directory file, then `new_p` must be one of:
:* the same file as `old_p` or a hardlink to it: nothing is done in this case.
:* existing non-directory file: `new_p` is first deleted, then, without allowing other processes to observe `new_p` as deleted, the pathname `new_p` is linked to the file and `old_p` is unlinked from the file. Write permissions are required to both the directory that contains `old_p` and the directory that contains `new_p`.
:* non-existing file in an existing directory: The pathname `new_p` is linked to the file and `old_p` is unlinked from the file. Write permissions are required to both the directory that contains `old_p` and the directory that contains `new_p`.
* If `old_p` is a directory, then `new_p` must be one of:
:* the same directory as `old_p` or a hardlink to it: nothing is done in this case.
:* existing directory: `new_p` is deleted if empty on POSIX systems, but this may be an error on other systems. If not an error, then `new_p` is first deleted, then, without allowing other processes to observe `new_p` as deleted, the pathname `new_p` is linked to the directory and `old_p` is unlinked from the directory. Write permissions are required to both the directory that contains `old_p` and the directory that contains `new_p`.
:* non-existing directory, not ending with a directory separator, and whose parent directory exists: The pathname `new_p` is linked to the directory and `old_p` is unlinked from the directory. Write permissions are required to both the directory that contains `old_p` and the directory that contains `new_p`.
* Symlinks are not followed: if `old_p` is a symlink, it is itself renamed, not its target. If `new_p` is an existing symlink, it is itself erased, not its target.
Rename fails if
* `new_p` ends with *dot* or with *dot-dot*.
* `new_p` names a non-existing directory ending with a directory separator.
* `old_p` is a directory which is an ancestor of `new_p`.

## Parameters


### Parameters

- `old_p` - path to move or rename
- `new_p` - target path for the move/rename operation
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
namespace fs = std::filesystem;

int main()
{
    std::filesystem::path p = std::filesystem::current_path() / "sandbox";
    std::filesystem::create_directories(p / "from");
    std::ofstream{ p / "from/file1.txt" }.put('a');
    std::filesystem::create_directory(p / "to");

//  fs::rename(p / "from/file1.txt", p / "to/"); // error: "to" is a directory
    fs::rename(p / "from/file1.txt", p / "to/file2.txt"); // OK
//  fs::rename(p / "from", p / "to"); // error: "to" is not empty
    fs::rename(p / "from", p / "to/subdir"); // OK

    std::filesystem::remove_all(p);
}
```


## See also


| cpp/io/c/dsc rename | (see dedicated page) |
| cpp/filesystem/dsc remove | (see dedicated page) |

