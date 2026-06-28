---
title: std::filesystem::path::lexically_relative
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/lexically_normal
---


```cpp
dcl|since=c++17|num=1|1=
path lexically_normal() const;
dcl|since=c++17|num=2|1=
path lexically_relative( const path& base ) const;
dcl|since=c++17|num=3|1=
path lexically_proximate( const path& base ) const;
```

1. Returns `*this` converted to normal form in its generic format.
2. Returns `*this` made relative to `base`.
:* First, if `1=root_name() != base.root_name()` is `true` or `1=is_absolute() != base.is_absolute()` is `true` or `(!has_root_directory() && base.has_root_directory())` is `true` or any filename in `relative_path()` or `base.relative_path()` can be interpreted as a *root-name*, returns a default-constructed path.
:* Otherwise, first determines the first mismatched element of `*this` and `base` as if by `auto [a, b] , then
::* if `a  and `b , returns `path(".")`,
::* otherwise, define $N$ as the number of nonempty filename elements that are neither *dot* nor *dot-dot* in `[b, base.end())`, minus the number of *dot-dot* filename elements, If $N < 0$, returns a default-constructed path,
::* otherwise, if $N  and `a , returns `path(".")`,
::* otherwise returns an object composed from
:::* a default-constructed `path()` followed by
:::* $N$ applications of `operator/, followed by
:::* one application of `1=operator/=` for each element in the half-open range [a, end()).
3. If the value of `lexically_relative(base)` is not an empty path, return it. Otherwise return `*this`.

## Parameters

(none)

## Return value

1. The normal form of the path.
2. The relative form of the path.
3. The proximate form of the path.

## Notes

These conversions are purely lexical. They do not check that the paths exist, do not follow symlinks, and do not access the filesystem at all. For symlink-following counterparts of `lexically_relative` and `lexically_proximate`, see `cpp/filesystem/relative|relative` and `cpp/filesystem/relative|proximate`.
On Windows, the returned `path` has backslashes (the preferred separators).
On POSIX, no filename in a relative path is acceptable as a *root-name*.

## Example


### Example

```cpp
#include <cassert>
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    assert(fs::path("a/./b/..").lexically_normal() == "a/");
    assert(fs::path("a/.///b/../").lexically_normal() == "a/");
    assert(fs::path("/a/d").lexically_relative("/a/b/c") == "../../d");
    assert(fs::path("/a/b/c").lexically_relative("/a/d") == "../b/c");
    assert(fs::path("a/b/c").lexically_relative("a") == "b/c");
    assert(fs::path("a/b/c").lexically_relative("a/b/c/x/y") == "../..");
    assert(fs::path("a/b/c").lexically_relative("a/b/c") == ".");
    assert(fs::path("a/b").lexically_relative("c/d") == "../../a/b");
    assert(fs::path("a/b").lexically_relative("/a/b") == "");
    assert(fs::path("a/b").lexically_proximate("/a/b") == "a/b");
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3070 | c++17 | a filename that can also be a root-name may cause surprising result | treated as error case |
| lwg-3096 | c++17 | trailing "/" and "/." are handled incorrectly | corrected |


## See also


| cpp/filesystem/dsc relative | (see dedicated page) |

