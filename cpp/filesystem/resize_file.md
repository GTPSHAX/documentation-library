---
title: std::filesystem::resize_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/resize_file
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void resize_file( const std::filesystem::path& p,
std::uintmax_t new_size );
dcl|num=2|since=c++17|1=
void resize_file( const std::filesystem::path& p,
std::uintmax_t new_size,
std::error_code& ec ) noexcept;
```

Changes the size of the regular file named by `p` as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/truncate.html `truncate`]: if the file size was previously larger than `new_size`, the remainder of the file is discarded. If the file was previously smaller than `new_size`, the file size is increased and the new area appears as if zero-filled.

## Parameters


### Parameters

- `p` - path to resize
- `new_size` - size that the file will now have
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Notes

On systems that support sparse files, increasing the file size does not increase the space it occupies on the file system: space allocation takes place only when non-zero bytes are written to the file.

## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iostream>
#include <locale>

int main()
{
    auto p = std::filesystem::temp_directory_path() / "example.bin";
    std::ofstream{p}.put('a');
    std::cout.imbue(std::locale{"en_US.UTF8"});
    std::cout << "File size:  " << std::filesystem::file_size(p) << '\n'
              << "Free space: " << std::filesystem::space(p).free << '\n';
    std::filesystem::resize_file(p, 64*1024); // resize to 64 KB
    std::cout << "File size:  " << std::filesystem::file_size(p) << '\n'
              << "Free space: " << std::filesystem::space(p).free << '\n';
    std::filesystem::remove(p);
}
```


**Output:**
```
File size:  1
Free space: 42,954,108,928
File size:  65,536
Free space: 42,954,108,928
```


## See also


| cpp/filesystem/dsc file_size | (see dedicated page) |
| cpp/filesystem/dsc space | (see dedicated page) |

