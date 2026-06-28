---
title: std::filesystem::directory_entry::is_directory
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/is_directory
---


```cpp
dcl|num=1|since=c++17|1=
bool is_directory() const;
dcl|num=2|since=c++17|1=
bool is_directory( std::error_code& ec ) const noexcept;
```

Checks whether the pointed-to object is a directory. Effectively returns:
1. `std::filesystem::is_directory(status())`,
2. `std::filesystem::is_directory(status(ec))`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if the referred-to filesystem object is a directory, `false` otherwise.

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
#include <string_view>

namespace fs = std::filesystem;

void check_directory(fs::directory_entry const& d, std::string_view rem = "")
{
    std::cout << "is_directory(" << d << "): " << d.is_directory() << rem << '\n';
}

int main()
{
    fs::directory_entry d1(".");
    fs::directory_entry d2("file.txt");
    fs::directory_entry d3("new_dir");

    std::cout << std::boolalpha;

    check_directory(d1);
    check_directory(d2);
    check_directory(d3, " (has not been created yet).");

    std::filesystem::create_directory("new_dir");

    check_directory(d3, " (before refresh).");
    d3.refresh();
    check_directory(d3, " (after refresh).");
}
```


**Output:**
```
is_directory("."): true
is_directory("file.txt"): false
is_directory("new_dir"): false (has not been created yet).
is_directory("new_dir"): false (before refresh).
is_directory("new_dir"): true (after refresh).
```


## See also


| cpp/filesystem/dsc is_directory | (see dedicated page) |

