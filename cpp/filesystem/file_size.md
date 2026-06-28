---
title: std::filesystem::file_size
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_size
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
std::uintmax_t file_size( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
std::uintmax_t file_size( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
```

If `p` does not exist, reports an error.
For a regular file `p`, returns the size determined as if by reading the `st_size` member of the structure obtained by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/stat.html `stat`] (symlinks are followed).
The result of attempting to determine the size of a directory (as well as any other file that is not a regular file or a symlink) is implementation-defined.
The non-throwing overload returns `static_cast<std::uintmax_t>(-1)` on errors.

## Parameters


### Parameters

- `p` - path to examine
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The size of the file, in bytes.

## Exceptions


## Example


### Example

```cpp
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

struct HumanReadable
{
    std::uintmax_t size{};

private:
    friend std::ostream& operator<<(std::ostream& os, HumanReadable hr)
    {
        int o{};
        double mantissa = hr.size;
        for (; mantissa >= 1024.; mantissa /= 1024., ++o);
        os << std::ceil(mantissa * 10.) / 10. << "BKMGTPE"[o];
        return o ? os << "B (" << hr.size << ')' : os;
    }
};

int main(int, char const* argv[])
{
    fs::path example = "example.bin";
    fs::path p = fs::current_path() / example;
    std::ofstream(p).put('a'); // create file of size 1
    std::cout << example << " size = " << fs::file_size(p) << '\n';
    fs::remove(p);

    p = argv[0];
    std::cout << p << " size = " << HumanReadable{fs::file_size(p)} << '\n';

    try
    {
        std::cout << "Attempt to get size of a directory:\n";
        [[maybe_unused]] auto x_x = fs::file_size("/dev");
    }
    catch (fs::filesystem_error& e)
    {
        std::cout << e.what() << '\n';
    }

    for (std::error_code ec; fs::path bin : {"cat", "mouse"})
    {
        bin = "/bin"/bin;
        if (const std::uintmax_t size = fs::file_size(bin, ec); ec)
            std::cout << bin << " : " << ec.message() << '\n';
        else
            std::cout << bin << " size = " << HumanReadable{size} << '\n';
    }
}
```


**Output:**
```
"example.bin" size = 1
"./a.out" size = 22KB (22512)
Attempt to get size of a directory:
filesystem error: cannot get file size: Is a directory [/dev]
"/bin/cat" size = 50.9KB (52080)
"/bin/mouse" : No such file or directory
```


## See also


| cpp/filesystem/dsc resize_file | (see dedicated page) |
| cpp/filesystem/dsc space | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc file_size | (see dedicated page) |

