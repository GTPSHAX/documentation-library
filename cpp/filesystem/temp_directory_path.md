---
title: std::filesystem::temp_directory_path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/temp_directory_path
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
path temp_directory_path();
dcl|num=2|since=c++17|1=
path temp_directory_path( std::error_code& ec );
```

Returns the directory location suitable for temporary files.

## Parameters

(none)

## Return value

A directory suitable for temporary files. The path is guaranteed to exist and to be a directory. The overload that takes `error_code&` argument returns an empty path on error.

## Exceptions


## Notes

On POSIX systems, the path may be the one specified in the environment variables `TMPDIR`, `TMP`, `TEMP`, `TEMPDIR`, and, if none of them are specified, the path `"/tmp"` is returned.
On Windows systems, the path is typically the one returned by [https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-gettemppathw `GetTempPath`].

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << "Temp directory is " << fs::temp_directory_path() << '\n';
}
```


**Output:**
```
Temp directory is "C:\Windows\TEMP\"
```


## See also


| cpp/io/c/dsc tmpfile | (see dedicated page) |
| cpp/filesystem/dsc current_path | (see dedicated page) |

