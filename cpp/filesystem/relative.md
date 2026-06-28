---
title: std::filesystem::relative
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/relative
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
path relative( const std::filesystem::path& p,
std::error_code& ec );
dcl|num=2|since=c++17|1=
path relative( const std::filesystem::path& p,
const std::filesystem::path& base = std::filesystem::current_path() );
dcl|num=3|since=c++17|1=
path relative( const std::filesystem::path& p,
const std::filesystem::path& base,
std::error_code& ec );
dcl|num=4|since=c++17|1=
path proximate( const std::filesystem::path& p,
std::error_code& ec );
dcl|num=5|since=c++17|1=
path proximate( const std::filesystem::path& p,
const std::filesystem::path& base = std::filesystem::current_path() );
dcl|num=6|since=c++17|1=
path proximate( const std::filesystem::path& p,
const std::filesystem::path& base,
std::error_code& ec );
```

1. Returns `relative(p, current_path(), ec)`.
@2,3@ Returns `p` made relative to `base`. Resolves symlinks and normalizes both `p` and `base` before other processing. Effectively returns `std::filesystem::weakly_canonical(p).lexically_relative(std::filesystem::weakly_canonical(base))` or `std::filesystem::weakly_canonical(p, ec).lexically_relative(std::filesystem::weakly_canonical(base, ec))`, except the error code form returns `path()` at the first error occurrence, if any.
4. Returns `proximate(p, current_path(), ec)`.
@5,6@ Effectively returns `std::filesystem::weakly_canonical(p).lexically_proximate(std::filesystem::weakly_canonical(base))` or `std::filesystem::weakly_canonical(p, ec).lexically_proximate(std::filesystem::weakly_canonical(base, ec))`, except the error code form returns `path()` at the first error occurrence, if any.

## Parameters


### Parameters

- `p` - an existing path
- `base` - base path, against which `p` will be made relative/proximate
- `ec` - error code to store error status to

## Return value

1. `p` made relative against `current_path()`.
@2,3@ `p` made relative against `base`.
4. `p` made proximate against `current_path()`.
@5,6@ `p` made proximate against `base`.

## Exceptions


## Example


### Example

```cpp
#include <filesystem>
#include <iostream>

void show(std::filesystem::path x, std::filesystem::path y)
{
    std::cout << "x:\t\t " << x << "\ny:\t\t " << y << '\n'
              << "relative(x, y):  "
              << std::filesystem::relative(x, y) << '\n'
              << "proximate(x, y): "
              << std::filesystem::proximate(x, y) << "\n\n";
}

int main()
{
    show("/a/b/c", "/a/b");
    show("/a/c", "/a/b");
    show("c", "/a/b");
    show("/a/b", "c");
}
```


**Output:**
```
x:               "/a/b/c"
y:               "/a/b"
relative(x, y):  "c"
proximate(x, y): "c"

x:               "/a/c"
y:               "/a/b"
relative(x, y):  "../c"
proximate(x, y): "../c"

x:               "c"
y:               "/a/b"
relative(x, y):  ""
proximate(x, y): "c"

x:               "/a/b"
y:               "c"
relative(x, y):  ""
proximate(x, y): "/a/b"
```


## See also


| cpp/filesystem/dsc path | (see dedicated page) |
| cpp/filesystem/dsc absolute | (see dedicated page) |
| cpp/filesystem/dsc canonical | (see dedicated page) |
| cpp/filesystem/path/dsc lexically_normal | (see dedicated page) |

