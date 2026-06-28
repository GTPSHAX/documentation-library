---
title: std::filesystem::path::operator/=
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/append
---


```cpp
dcl|num=1|since=c++17|1=
path& operator/=( const path& p );
dcl|num=2|since=c++17|1=
template< class Source >
path& operator/=( const Source& source );
dcl|num=3|since=c++17|1=
template< class Source >
path& append( const Source& source );
dcl|num=4|since=c++17|1=
template< class InputIt >
path& append( InputIt first, InputIt last );
```

1. If `p.is_absolute() , then replaces the current path with `p` as if by `operator and finishes.
@@* Otherwise, if `p.has_root_directory()`, then removes any root directory and the entire relative path from the generic format pathname of `*this`.
@@* Otherwise, if `has_filename() , then appends `path::preferred_separator` to the generic format of `*this`.
@@* Either way, then appends the native format pathname of `p`, omitting any *root-name* from its generic format, to the native format of `*this`.

```cpp
// Where "//host" is a root-name
path("//host")  / "foo" // the result is      "//host/foo" (appends with separator)
path("//host/") / "foo" // the result is also "//host/foo" (appends without separator)

// On POSIX,
path("foo") / ""      // the result is "foo/" (appends)
path("foo") / "/bar"; // the result is "/bar" (replaces)

// On Windows,
path("foo") / "C:/bar";  // the result is "C:/bar" (replaces)
path("foo") / "C:";      // the result is "C:"     (replaces)
path("C:") / "";         // the result is "C:"     (appends, without separator)
path("C:foo") / "/bar";  // yields "C:/bar"        (removes relative path, then appends)
path("C:foo") / "C:bar"; // yields "C:foo/bar"     (appends, omitting p's root-name)
```

@2,3@ Same as , but accepts any `std::basic_string`, `std::basic_string_view`, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence. Equivalent to `1=return operator/=(path(source));`.
4. Same as , but accepts any iterator pair that designates a multicharacter string. Equivalent to `1=return operator/=(path(first, last));`.

## Parameters


### Parameters

- `p` - pathname to append
- `source` - `std::basic_string`, `std::basic_string_view`, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence, which represents a path name (either in portable or in native format)
- `first, last` - pair of *InputIterator*s that specify a multicharacter sequence that represents a path name

**Type requirements:**

- `InputIt`

## Return value

`*this`

## Exceptions

May throw `std::bad_alloc` if memory allocation fails.

## Notes

These functions effectively yield an approximation of the meaning of the argument path `p` in an environment where `*this` is the starting directory.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::path p1 = "C:";
    p1 /= "Users"; // does not insert a separator
    std::cout << "\"C:\" / \"Users\" == " << p1 << '\n';
    p1 /= "batman"; // inserts fs::path::preferred_separator, '\' on Windows
    std::cout << "\"C:\" / \"Users\" / \"batman\" == " << p1 << '\n';
}
```


**Output:**
```
"C:" / "Users" == "C:Users"
"C:" / "Users" / "batman" == "C:Users\\batman"
```


## Defect reports


## See also


| cpp/filesystem/path/dsc concat | (see dedicated page) |
| cpp/filesystem/path/dsc operator/ | (see dedicated page) |

