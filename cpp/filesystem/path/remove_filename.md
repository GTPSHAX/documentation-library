---
title: std::filesystem::path::remove_filename
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/remove_filename
---


```cpp
dcl|since=c++17|
path& remove_filename();
```

Removes a single generic-format filename component (as returned by `cpp/filesystem/path/filename`) from the given generic-format path.
After this function completes, `cpp/filesystem/path/has_path|has_filename` returns `false`.

## Parameters

(none)

## Return value

`*this`

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::path p;
    std::cout << std::boolalpha
              << (p = "foo/bar").remove_filename() << '\t' << p.has_filename() << '\n'
              << (p = "foo/").remove_filename() << '\t' << p.has_filename() << '\n'
              << (p = "/foo").remove_filename() << '\t' << p.has_filename() << '\n'
              << (p = "/").remove_filename() << '\t' << p.has_filename() << '\n'
              << (p = "").remove_filename() << '\t' << p.has_filename() << '\n';
}
```


**Output:**
```
"foo/"  false
"foo/"  false
"/"     false
"/"     false
""      false
```


## See also


| cpp/filesystem/path/dsc filename | (see dedicated page) |
| cpp/filesystem/path/dsc replace_filename | (see dedicated page) |

