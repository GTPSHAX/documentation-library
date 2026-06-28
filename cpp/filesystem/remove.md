---
title: std::filesystem::remove_all
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/remove
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|num=1|1=
bool remove( const std::filesystem::path& p );
dcl|since=c++17|num=2|1=
bool remove( const std::filesystem::path& p, std::error_code& ec ) noexcept;
dcl|since=c++17|num=3|
std::uintmax_t remove_all( const std::filesystem::path& p );
dcl|since=c++17|num=4|1=
std::uintmax_t remove_all( const std::filesystem::path& p, std::error_code& ec );
```

@1,2@ The file or empty directory identified by the path `p` is deleted as if by the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/remove.html `remove`]. Symlinks are not followed (symlink is removed, not its target).
@3,4@ Deletes the contents of `p` (if it is a directory) and the contents of all its subdirectories, recursively, then deletes `p` itself as if by repeatedly applying the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/remove.html `remove`]. Symlinks are not followed (symlink is removed, not its target).

## Parameters


### Parameters

- `p` - path to delete
- `ec` - out-parameter for error reporting in the non-throwing overload.

## Return value

@1,2@ `true` if the file was deleted, `false` if it did not exist. The overload that takes `error_code&` argument returns `false` on errors.
@3,4@ Returns the number of files and directories that were deleted (which may be zero if `p` did not exist to begin with). The overload that takes `error_code&` argument returns `static_cast<std::uintmax_t>(-1)` on error.

## Exceptions


## Notes

On POSIX systems, this function typically calls [https://pubs.opengroup.org/onlinepubs/9699919799/functions/unlink.html `unlink`] and [https://pubs.opengroup.org/onlinepubs/9699919799/functions/rmdir.html `rmdir`] as needed, on Windows [https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-deletefilew `DeleteFileW`] and [https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-removedirectoryw `RemoveDirectoryW`].
If `p` did not exist, this function returns `false` and does not report an error.

## Example


### Example

```cpp
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>

int main()
{
    namespace fs = std::filesystem;
    std::cout << std::boolalpha;

    fs::path tmp{std::filesystem::temp_directory_path()};

    const auto O_O{"O_O"};
    std::ofstream{tmp / O_O} << O_O; // creates file containing O_O
    std::cout << "remove(): " << fs::remove(tmp / O_O) << '\n'; // success
    std::cout << "remove(): " << fs::remove(tmp / O_O) << '\n'; // fail

    std::filesystem::create_directories(tmp / "abcdef/example");
    const std::uintmax_t n{fs::remove_all(tmp / "abcdef")};
    std::cout << "remove_all(): " << n << " files or directories\n";
}
```


**Output:**
```
remove(): true
remove(): false
remove_all(): 2 files or directories
```


## Defect reports


## See also


| cpp/io/c/dsc remove | (see dedicated page) |

