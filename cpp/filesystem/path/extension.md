---
title: std::filesystem::path::extension
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/extension
---


```cpp
dcl|since=c++17|1=
path extension() const;
```

Returns the extension of the filename component of the generic-format view of `*this`.
If the `cpp/filesystem/path/filename|filename()` component of the generic-format path contains a period (**`.`**), and is not one of the special filesystem elements *dot* or *dot-dot*, then the ''extension'' is the substring beginning at the rightmost period (including the period) and until the end of the pathname.
If the first character in the filename is a period, that period is ignored (a filename like ".profile" is not treated as an extension).
If the pathname is either **`.`** or **`..`**, or if `cpp/filesystem/path/filename|filename()` does not contain the `'.'` character, then empty path is returned.
Additional behavior may be defined by the implementations for file systems which append additional elements (such as alternate data streams or partitioned dataset names) to extensions.

## Parameters

(none)

## Return value

The extension of the current pathname or an empty path if there's no extension.

## Notes

The extension as returned by this function includes a period to make it possible to distinguish the file that ends with a period (function returns `"."`) from a file with no extension (function returns `""`).
On a non-POSIX system, it is possible that `1=p.stem() + p.extension() != p.filename()` even though generic-format versions are the same.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    std::cout << fs::path("/foo/bar.txt").extension() << '\n'
              << fs::path("/foo/bar.").extension() << '\n'
              << fs::path("/foo/bar").extension() << '\n'
              << fs::path("/foo/bar.txt/bar.cc").extension() << '\n'
              << fs::path("/foo/bar.txt/bar.").extension() << '\n'
              << fs::path("/foo/bar.txt/bar").extension() << '\n'
              << fs::path("/foo/.").extension() << '\n'
              << fs::path("/foo/..").extension() << '\n'
              << fs::path("/foo/.hidden").extension() << '\n'
              << fs::path("/foo/..bar").extension() << '\n';
}
```


**Output:**
```
".txt"
"."
""
".cc"
"."
""
""
""
""
".bar"
```


## See also


| cpp/filesystem/path/dsc filename | (see dedicated page) |
| cpp/filesystem/path/dsc stem | (see dedicated page) |
| cpp/filesystem/path/dsc replace_extension | (see dedicated page) |

