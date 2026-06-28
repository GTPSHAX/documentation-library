---
title: std::filesystem::current_path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/current_path
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
path current_path();
dcl|num=2|since=c++17|1=
path current_path( std::error_code& ec );
dcl|num=3|since=c++17|1=
void current_path( const std::filesystem::path& p );
dcl|num=4|since=c++17|1=
void current_path( const std::filesystem::path& p,
std::error_code& ec ) noexcept;
```

Returns or changes the current path.
@1,2@ Returns the absolute path of the current working directory, obtained as if (in native format) by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/getcwd.html `getcwd`].  returns `path()` if error occurs.
@3,4@ Changes the current working directory to `p`, as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/chdir.html `chdir`].

## Parameters


### Parameters

- `p` - path to change the current working directory to
- `ec` - out-parameter for error reporting in the non-throwing overloads

## Return value

@1,2@ Returns the current working directory.
@3,4@ (none)

## Exceptions


## Notes

The current working directory is the directory, associated with the process, that is used as the starting location in pathname resolution for relative paths.
The current path as returned by many operating systems is a dangerous global variable. It may be changed unexpectedly by third-party or system library functions, or by another thread.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << "Current path is " << fs::current_path() << '\n'; // (1)
    fs::current_path(fs::temp_directory_path()); // (3)
    std::cout << "Current path is " << fs::current_path() << '\n';
}
```


**Output:**
```
Current path is "D:/local/ConsoleApplication1"
Current path is "E:/Temp"
```


## See also


| cpp/filesystem/dsc temp_directory_path | (see dedicated page) |

