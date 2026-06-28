---
title: std::filesystem::directory_entry::is_regular_file
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_regular_file
---


```cpp
dcl|num=1|since=c++17|
bool is_regular_file() const;
dcl|num=2|since=c++17|
bool is_regular_file( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a regular file. Effectively returns:
1. `std::filesystem::is_regular_file(status())`.
2. `std::filesystem::is_regular_file(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a regular file, `false` otherwise.

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
#include <string>

namespace fs = std::filesystem;

int main(int argc, const char* argv[])
{
    // Print out all regular files in a directory 'dir'.
    try
    {
        const auto dir{argc == 2 ? fs::path{argv[1]} : fs::current_path()};

        std::cout << "Current dir: " << dir << '\n'
                  << std::string(40, '-') << '\n';

        for (fs::directory_entry const& entry : fs::directory_iterator(dir))
            if (entry.is_regular_file())
                std::cout << entry.path().filename() << '\n';
    }
    catch(const fs::filesystem_error& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
Current dir: "/tmp/1588616534.9884143"
----------------------------------------
"main.cpp"
"a.out"
```


## See also


| cpp/filesystem/dsc is_regular_file | (see dedicated page) |

