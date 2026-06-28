---
title: std::filesystem::copy_options
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/copy_options
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
enum class copy_options {
none = /* unspecified */,
skip_existing = /* unspecified */,
overwrite_existing = /* unspecified */,
update_existing = /* unspecified */,
recursive = /* unspecified */,
copy_symlinks = /* unspecified */,
skip_symlinks = /* unspecified */,
directories_only = /* unspecified */,
create_symlinks = /* unspecified */,
create_hard_links = /* unspecified */
};
```

This type represents available options that control the behavior of the `cpp/filesystem/copy|copy()` and `cpp/filesystem/copy_file|copy_file()` function.

## Member constants

At most one copy option in each of the following options groups may be present, otherwise the behavior of the copy functions is undefined.


| - |
| Member constant |
| Meaning |
| - |
| colspan=2 | options controlling ltt | cpp/filesystem/copy_file | copy_file() when the file already exists |
| - |
| tt | none |
| Report an error (default behavior). |
| - |
| tt | skip_existing |
| Keep the existing file, without reporting an error. |
| - |
| tt | overwrite_existing |
| Replace the existing file. |
| - |
| tt | update_existing |
| Replace the existing file only if it is older than the file being copied. |
| - |
| colspan=2 | options controlling the effects of ltt | cpp/filesystem/copy | copy() on subdirectories |
| - |
| tt | none |
| Skip subdirectories (default behavior). |
| - |
| tt | recursive |
| Recursively copy subdirectories and their content. |
| - |
| colspan=2 | options controlling the effects of ltt | cpp/filesystem/copy | copy() on symbolic links |
| - |
| tt | none |
| Follow symlinks (default behavior). |
| - |
| tt | copy_symlinks |
| Copy symlinks as symlinks, not as the files they point to. |
| - |
| tt | skip_symlinks |
| Ignore symlinks. |
| - |
| colspan=2 | options controlling the kind of copying ltt | cpp/filesystem/copy | copy() does |
| - |
| tt | none |
| Copy file content (default behavior). |
| - |
| tt | directories_only |
| Copy the directory structure, but do not copy any non-directory files. |
| - |
| tt | create_symlinks |
| Instead of creating copies of files, create symlinks pointing to the originals. Note: the source path must be an absolute path unless the destination path is in the current directory. |
| - |
| tt | create_hard_links |
| Instead of creating copies of files, create hardlinks that resolve to the same files as the originals. |


## Example


## See also


| cpp/filesystem/dsc copy | (see dedicated page) |
| cpp/filesystem/dsc copy_file | (see dedicated page) |

