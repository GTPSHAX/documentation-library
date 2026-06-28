---
title: std::filesystem::directory_entry::last_write_time
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/last_write_time
---


```cpp
dcl|num=1|since=c++17|1=
std::filesystem::file_time_type last_write_time() const;
dcl|num=2|since=c++17|1=
std::filesystem::file_time_type last_write_time( std::error_code& ec ) const noexcept;
```

If the last modification time is cached in this `directory_entry`, returns the cached value. Otherwise, returns:
1. `std::filesystem::last_write_time(path())`.
2. `std::filesystem::last_write_time(path(), ec)`.

## Parameters


### Parameters

- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

The last modification time for the referred-to filesystem object.

## Exceptions


## Example


### Example

```cpp
#include <chrono>
#include <ctime>
#include <filesystem>
#include <format>
#include <iostream>
#include <string>

std::string to_string(const std::filesystem::file_time_type& ftime)
{
#if __cpp_lib_format
    return std::format("{:%c}", ftime);
#else
    std::time_t cftime = std::chrono::system_clock::to_time_t(
        std::chrono::file_clock::to_sys(ftime));
    std::string str = std::asctime(std::localtime(&cftime));
    str.pop_back(); // rm the trailing '\n' put by `asctime`
    return str;
#endif
}

int main()
{
    auto dir = std::filesystem::current_path();
    using Entry = std::filesystem::directory_entry;
    for (Entry const& entry : std::filesystem::directory_iterator(dir))
        std::cout << to_string(entry.last_write_time()) << " : "
                  << entry.path().filename() << '\n';
}
```


**Output:**
```
Wed Sep  6 13:37:13.960314156 2023 : "main.cpp"
Wed Sep  6 13:37:42.690271828 2023 : "a.out"
```


## See also


| cpp/filesystem/dsc last_write_time | (see dedicated page) |

