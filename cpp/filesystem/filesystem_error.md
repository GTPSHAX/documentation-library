---
title: std::filesystem::filesystem_error
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/filesystem_error
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
class filesystem_error;
```

The class `std::filesystem::filesystem_error` defines an exception object that is thrown on failure by the throwing overloads of the functions in the filesystem library.

## Member functions


| cpp/filesystem/filesystem_error/dsc constructor | (see dedicated page) |
| cpp/filesystem/filesystem_error/dsc operator{{= | (see dedicated page) |
| cpp/filesystem/filesystem_error/dsc path | (see dedicated page) |
| cpp/filesystem/filesystem_error/dsc what | (see dedicated page) |


## Notes

In order to ensure that copy functions of `filesystem_error` are noexcept, typical implementations store an object holding the return value of `what()` and two `std::filesystem::path` objects referenced by `path1()` and `path2()` respectively in a separately-allocated reference-counted storage.
Currently the [https://github.com/microsoft/STL/blob/master/stl/inc/filesystem#L1749 MS STL implementation] is non-conforming: objects mentioned above are stored directly in the `filesystem` object, which makes the copy functions not noexcept.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
#include <system_error>

int main()
{
    const std::filesystem::path from{"/none1/a"}, to{"/none2/b"};

    try
    {
        std::filesystem::copy_file(from, to); // throws: files do not exist
    }
    catch (std::filesystem::filesystem_error const& ex)
    {
        std::cout << "what():  " << ex.what() << '\n'
                  << "path1(): " << ex.path1() << '\n'
                  << "path2(): " << ex.path2() << '\n'
                  << "code().value():    " << ex.code().value() << '\n'
                  << "code().message():  " << ex.code().message() << '\n'
                  << "code().category(): " << ex.code().category().name() << '\n';
    }

    // All functions have non-throwing equivalents
    std::error_code ec;
    std::filesystem::copy_file(from, to, ec); // does not throw
    std::cout << "\nNon-throwing form sets error_code: " << ec.message() << '\n';
}
```


**Output:**
```
what():  filesystem error: cannot copy file: No such file or directory [/none1/a] [/none2/b]
path1(): "/none1/a"
path2(): "/none2/b"
code().value():    2
code().message():  No such file or directory
code().category(): generic

Non-throwing form sets error_code: No such file or directory
```

