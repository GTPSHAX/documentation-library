---
title: std::filesystem::absolute
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/absolute
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
path absolute( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
path absolute( const std::filesystem::path& p, std::error_code& ec );
```

Returns a path referencing the same file system location as `p`, for which `cpp/filesystem/path/is_absrel|filesystem::path::is_absolute()` is `true`.
2. This non-throwing overload returns default-constructed path if an error occurs.

## Parameters


### Parameters

- `p` - path to convert to absolute form
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

Returns an absolute (although not necessarily canonical) pathname referencing the same file as `p`.

## Exceptions


## Notes

Implementations are encouraged to not consider `p` not existing to be an error.
For POSIX-based operating systems, `std::filesystem::absolute(p)` is equivalent to `std::filesystem::current_path() / p` except for when `p` is the empty path.
For Windows, `std::filesystem::absolute` may be implemented as a call to [https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfullpathnamew `GetFullPathNameW`].

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::filesystem::path p = "foo.c";
    std::cout << "Current path is " << std::filesystem::current_path() << '\n';
    std::cout << "Absolute path for " << p << " is " << fs::absolute(p) << '\n';
}
```


**Output:**
```
Current path is "/tmp/1666297965.0051296"
Absolute path for "foo.c" is "/tmp/1666297965.0051296/foo.c"
```


## See also


| cpp/filesystem/dsc canonical | (see dedicated page) |
| cpp/filesystem/dsc relative | (see dedicated page) |

