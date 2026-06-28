---
title: std::filesystem::hard_link_count
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/hard_link_count
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
std::uintmax_t hard_link_count( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
std::uintmax_t hard_link_count( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
```

Returns the number of hard links for the filesystem object identified by path `p`.
The non-throwing overload returns `static_cast<uintmax_t>(-1)` on errors.

## Parameters


### Parameters

- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The number of hard links for `p`.

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    // On a POSIX-style filesystem, each directory has at least 2 hard links:
    // itself and the special member pathname "."
    fs::path p = fs::current_path();
    std::cout << "Number of hard links for current path is "
              << fs::hard_link_count(p) << '\n';

    // Each ".." is a hard link to the parent directory, so the total number
    // of hard links for any directory is 2 plus number of direct subdirectories
    p = fs::current_path() / ".."; // Each dot-dot is a hard link to parent
    std::cout << "Number of hard links for .. is "
              << fs::hard_link_count(p) << '\n';
}
```


**Output:**
```
Number of hard links for current path is 2
Number of hard links for .. is 3
```


## See also


| cpp/filesystem/dsc create_hard_link | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc hard_link_count | (see dedicated page) |

