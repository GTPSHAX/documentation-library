---
title: std::filesystem::weakly_canonical
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/canonical
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
path canonical( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
path canonical( const std::filesystem::path& p,
std::error_code& ec );
dcl|num=3|since=c++17|
path weakly_canonical( const std::filesystem::path& p );
dcl|num=4|since=c++17|
path weakly_canonical( const std::filesystem::path& p,
std::error_code& ec );
```

@1,2@ Converts path `p` to a canonical absolute path, i.e. an absolute path that has no dot, dot-dot elements or symbolic links in its generic format representation. If `p` is not an absolute path, the function behaves as if it is first made absolute by `std::filesystem::absolute(p)`. The path `p` must exist.
@3,4@ Returns a path composed by `1=operator/=` from the result of calling `canonical()` with a path argument composed of the leading elements of `p` that exist (as determined by `status(p)` or `status(p, ec)`), if any, followed by the elements of `p` that do not exist. The resulting path is in `normal form`.

## Parameters


### Parameters

- `p` - a path which may be absolute or relative; for `canonical` it must be an existing path
- `ec` - error code to store error status to

## Return value

@1,2@ An absolute path that resolves to the same file as `std::filesystem::absolute(p)`.
@3,4@ A normal path of the form `canonical(x)/y`, where `x` is a path composed of the longest leading sequence of elements in `p` that exist, and `y` is a path composed of the remaining trailing non-existent elements of `p`.

## Exceptions


## Notes

The function `canonical()` is modeled after the POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/realpath.html `realpath`].
The function `weakly_canonical()` was introduced to simplify operational semantics of `relative()`.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>

int main()
{
    /* set up sandbox directories:
     a
     └── b
         ├── c1
         │   └── d <== current path
         └── c2
             └── e
    */
    auto old = std::filesystem::current_path();
    auto tmp = std::filesystem::temp_directory_path();
    std::filesystem::current_path(tmp);
    auto d1 = tmp / "a/b/c1/d";
    auto d2 = tmp / "a/b/c2/e";
    std::filesystem::create_directories(d1);
    std::filesystem::create_directories(d2);
    std::filesystem::current_path(d1);

    auto p1 = std::filesystem::path("../../c2/./e");
    auto p2 = std::filesystem::path("../no-such-file");
    std::cout << "Current path is "
              << std::filesystem::current_path() << '\n'
              << "Canonical path for " << p1 << " is "
              << std::filesystem::canonical(p1) << '\n'
              << "Weakly canonical path for " << p2 << " is "
              << std::filesystem::weakly_canonical(p2) << '\n';
    try
    {
        [[maybe_unused]] auto x_x = std::filesystem::canonical(p2);
        // NOT REACHED
    }
    catch (const std::exception& ex)
    {
        std::cout << "Canonical path for " << p2 << " threw exception:\n"
                  << ex.what() << '\n';
    }

    // cleanup
    std::filesystem::current_path(old);
    const auto count = std::filesystem::remove_all(tmp / "a");
    std::cout << "Deleted " << count << " files or directories.\n";
}
```


**Output:**
```
Current path is "/tmp/a/b/c1/d"
Canonical path for "../../c2/./e" is "/tmp/a/b/c2/e"
Weakly canonical path for "../no-such-file" is "/tmp/a/b/c1/no-such-file"
Canonical path for "../no-such-file" threw exception:
filesystem error: in canonical: No such file or directory [../no-such-file] [/tmp/a/b/c1/d]
Deleted 6 files or directories.
```


## Defect reports


## See also


| cpp/filesystem/dsc path | (see dedicated page) |
| cpp/filesystem/dsc absolute | (see dedicated page) |
| cpp/filesystem/dsc relative | (see dedicated page) |

