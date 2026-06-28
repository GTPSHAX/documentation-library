---
title: std::filesystem::exists
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/exists
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool exists( std::filesystem::file_status s ) noexcept;
dcl|num=2|since=c++17|1=
bool exists( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
bool exists( const std::filesystem::path& p, std::error_code& ec ) noexcept;
```

Checks if the given file status or path corresponds to an existing file or directory.
1. Equivalent to `1=status_known(s) && s.type() != file_type::not_found`.
@2,3@ Let `s` be a `std::filesystem::file_status` determined as if by `status(p)` or `status(p, ec)` (symlinks are followed), respectively. Returns `exists(s)`. The non-throwing overload calls `ec.clear()` if `status_known(s)`.

## Parameters


### Parameters

- `s` - file status to check
- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the given path or file status corresponds to an existing file or directory, `false` otherwise.

## Exceptions

No filesystem exception is thrown if object does not exist (use return value).

## Notes

The information provided by this function is usually also provided as a byproduct of directory iteration. During directory iteration, calling `exists(*iterator)` is less efficient than `exists(iterator->status())`.

## Example


### Example

```cpp
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

void demo_exists(const fs::path& p, fs::file_status s = fs::file_status{})
{
    std::cout << p;
    if (fs::status_known(s) ? fs::exists(s) : fs::exists(p))
        std::cout << " exists\n";
    else
        std::cout << " does not exist\n";
}

int main()
{
    const fs::path sandbox{"sandbox"};
    fs::create_directory(sandbox);
    std::ofstream{sandbox/"file"}; // create regular file
    fs::create_symlink("non-existing", sandbox/"symlink");

    demo_exists(sandbox);

    for (const auto& entry : fs::directory_iterator(sandbox))
        demo_exists(entry, entry.status()); // use cached status from directory entry

    fs::remove_all(sandbox);
}
```


**Output:**
```
"sandbox" exists
"sandbox/symlink" does not exist
"sandbox/file" exists
```


## See also


| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc exists | (see dedicated page) |

