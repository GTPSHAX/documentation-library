---
title: std::filesystem::copy_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/copy_file
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool copy_file( const std::filesystem::path& from,
const std::filesystem::path& to );
dcl|num=2|since=c++17|1=
bool copy_file( const std::filesystem::path& from,
const std::filesystem::path& to,
std::error_code& ec );
dcl|num=3|since=c++17|1=
bool copy_file( const std::filesystem::path& from,
const std::filesystem::path& to,
std::filesystem::copy_options options );
dcl|num=4|since=c++17|1=
bool copy_file( const std::filesystem::path& from,
const std::filesystem::path& to,
std::filesystem::copy_options options,
std::error_code& ec );
```

@1,2@ The default, equivalent to  with `copy_options::none` used as `options`.
@3,4@ Copies a single file from `from` to `to`, using the copy options indicated by `options`. The behavior is undefined if there is more than one option in any of the `copy_options` option group present in `options` (even in the groups not relevant to `std::filesystem::copy_file|filesystem::copy_file`).
* If `std::filesystem::is_regular_file|!filesystem::is_regular_file(from)` (either because the source file doesn't exist or because it is not a regular file), report an error.
* Otherwise, if the destination file does not exist,
:* copies the contents and the attributes of the file to which `from` resolves to the file to which `to` resolves (symlinks are followed).
* Otherwise, if the destination file already exists,
:* report an error if any of the following is true:
::* `to` and `from` are the same as determined by `std::filesystem::equivalent|filesystem::equivalent(from, to)`;
::* `to` is not a regular file as determined by `std::filesystem::is_regular_file|!filesystem::is_regular_file(to)`;
::* none of the `std::filesystem::copy_file|filesystem::copy_file` control options are set in `options`.
:* Otherwise, if `copy_options::skip_existing` is set in `options`, do nothing.
:* Otherwise, if `copy_options::overwrite_existing` is set in `options`, copy the contents and the attributes of the file to which `from` resolves to the file to which `to` resolves.
:* Otherwise, if `copy_options::update_existing` is set in `options`, only copy the file if `from` is newer than `to`, as defined by `std::filesystem::last_write_time|filesystem::last_write_time()`.
The non-throwing overloads return `false` if an error occurs.

## Parameters


### Parameters

- `from` - path to the source file
- `to` - path to the target file
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the file was copied, `false` otherwise.

## Exceptions


## Notes

The functions involve at most one direct or indirect call to `std::filesystem::status|filesystem::status(to)` (used both to determine if the file exists, and, for `filesystem::copy_options::update_existing` option, its last write time).
Error is reported when `std::filesystem::copy_file|filesystem::copy_file` is used to copy a directory: use `std::filesystem::copy|filesystem::copy` for that.
`std::filesystem::copy_file|filesystem::copy_file` follows symlinks: use `std::filesystem::copy_symlink|filesystem::copy_symlink` or `std::filesystem::copy|filesystem::copy` with `filesystem::copy_options::copy_symlinks` for that.

## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::create_directory("sandbox");
    std::ofstream("sandbox/file1.txt").put('a');

    fs::copy_file("sandbox/file1.txt", "sandbox/file2.txt");

    // now there are two files in sandbox:
    std::cout << "file1.txt holds: "
              << std::ifstream("sandbox/file1.txt").rdbuf() << '\n';
    std::cout << "file2.txt holds: "
              << std::ifstream("sandbox/file2.txt").rdbuf() << '\n';

    // fail to copy directory
    fs::create_directory("sandbox/abc");
    try
    {
        fs::copy_file("sandbox/abc", "sandbox/def");
    }
    catch (fs::filesystem_error& e)
    {
        std::cout << "Could not copy sandbox/abc: " << e.what() << '\n';
    }
    fs::remove_all("sandbox");
}
```


**Output:**
```
file1.txt holds: a
file2.txt holds: a
Could not copy sandbox/abc: copy_file: Is a directory: "sandbox/abc", "sandbox/def"
```


## Defect reports


## See also


| cpp/filesystem/dsc copy_options | (see dedicated page) |
| cpp/filesystem/dsc copy_symlink | (see dedicated page) |
| cpp/filesystem/dsc copy | (see dedicated page) |

