---
title: std::filesystem::create_directory
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/create_directory
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
bool create_directory( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
bool create_directory( const std::filesystem::path& p, std::error_code& ec ) noexcept;
dcl|num=3|since=c++17|1=
bool create_directory( const std::filesystem::path& p,
const std::filesystem::path& existing_p );
dcl|num=4|since=c++17|1=
bool create_directory( const std::filesystem::path& p,
const std::filesystem::path& existing_p,
std::error_code& ec ) noexcept;
dcl|num=5|since=c++17|1=
bool create_directories( const std::filesystem::path& p );
dcl|num=6|since=c++17|1=
bool create_directories( const std::filesystem::path& p, std::error_code& ec );
```

@1,2@ Creates the directory `p` as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/mkdir.html `mkdir()`] with a second argument of `static_cast<int>(std::filesystem::perms::all)` (the parent directory must already exist). If the function fails because `p` resolves to an existing directory, no error is reported. Otherwise on failure an error is reported.
@3,4@ Same as , except that the attributes of the new directory are copied from `existing_p` (which must be a directory that exists). It is OS-dependent which attributes are copied: on POSIX systems, the attributes are copied as if by

```cpp
stat(existing_p.c_str(), &attributes_stat)
mkdir(p.c_str(), attributes_stat.st_mode)
```

On Windows OS, no attributes of `existing_p` are copied.
@5,6@ Executes  for every element of `p` that does not already exist. If `p` already exists, the function does nothing (this condition is not treated as an error).

## Parameters


### Parameters

- `p` - the path to the new directory to create
- `existing_p` - the path to a directory to copy the attributes from
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

`true` if a directory was newly created for the directory `p` resolves to, `false` otherwise.

## Exceptions


## Notes

The attribute-preserving overload  is implicitly invoked by  when recursively copying directories. Its equivalent in boost.filesystem is [https://www.boost.org/doc/libs/1_57_0/libs/filesystem/doc/reference.html#copy_directory `copy_directory`] (with argument order reversed).

## Example


### Example

```cpp
#include <cassert>
#include <cstdlib>
#include <filesystem>

int main()
{
    std::filesystem::current_path(std::filesystem::temp_directory_path());

    // Basic usage
    std::filesystem::create_directories("sandbox/1/2/a");
    std::filesystem::create_directory("sandbox/1/2/b");

    // Directory already exists (false returned, no error)
    assert(!std::filesystem::create_directory("sandbox/1/2/b"));

    // Permissions copying usage
    std::filesystem::permissions(
        "sandbox/1/2/b",
        std::filesystem::perms::others_all,
        std::filesystem::perm_options::remove
    );
    std::filesystem::create_directory("sandbox/1/2/c", "sandbox/1/2/b");

    std::system("ls -l sandbox/1/2");
    std::system("tree sandbox");
    std::filesystem::remove_all("sandbox");
}
```


**Output:**
```
drwxr-xr-x 2 user group 4096 Apr 15 09:33 a
drwxr-x--- 2 user group 4096 Apr 15 09:33 b
drwxr-x--- 2 user group 4096 Apr 15 09:33 c
sandbox
└── 1
    └── 2
        ├── a
        ├── b
        └── c
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2935 | C++17 | error if target already exists but is not a directory | not error |


## See also


| cpp/filesystem/dsc create_symlink | (see dedicated page) |
| cpp/filesystem/dsc copy | (see dedicated page) |
| cpp/filesystem/dsc perms | (see dedicated page) |

