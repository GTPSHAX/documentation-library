---
title: std::filesystem::copy
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/copy
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void copy( const std::filesystem::path& from,
const std::filesystem::path& to );
dcl|num=2|since=c++17|1=
void copy( const std::filesystem::path& from,
const std::filesystem::path& to,
std::error_code& ec );
dcl|num=3|since=c++17|1=
void copy( const std::filesystem::path& from,
const std::filesystem::path& to,
std::filesystem::copy_options options );
dcl|num=4|since=c++17|1=
void copy( const std::filesystem::path& from,
const std::filesystem::path& to,
std::filesystem::copy_options options,
std::error_code& ec );
```

Copies files and directories, with a variety of options.
@1,2@ The default, equivalent to  with `copy_options::none` used as `options`.
@3,4@ Copies the file or directory `from` to file or directory `to`, using the copy options indicated by `options`. The behavior is undefined if there is more than one option in any of the `copy_options` option group present in `options` (even in the `copy_file` group).
The behavior is as follows:
* First, before doing anything else, obtains type and permissions of `from` by no more than a single call to
:* `std::filesystem::symlink_status`, if `copy_options::skip_symlinks`, `copy_options::copy_symlinks`, or `copy_options::create_symlinks` is present in `options`;
:* `std::filesystem::status` otherwise.
* If necessary, obtains the status of `to`, by no more than a single call to
:* `std::filesystem::symlink_status`, if `copy_options::skip_symlinks` or `copy_options::create_symlinks` is present in `options`;
:* `std::filesystem::status` otherwise (including the case where `copy_options::copy_symlinks` is present in `options`).
* If either `from` or `to` has an implementation-defined file type, the effects of this function are implementation-defined.
* If `from` does not exist, reports an error.
* If `from` and `to` are the same file as determined by `std::filesystem::equivalent`, reports an error.
* If either `from` or `to` is not a regular file, a directory, or a symlink, as determined by `std::filesystem::is_other`, reports an error.
* If `from` is a directory, but `to` is a regular file, reports an error.
* If `from` is a symbolic link, then
:* If `copy_options::skip_symlink` is present in `options`, does nothing.
:* Otherwise, if `to` does not exist and `copy_options::copy_symlinks` is present in `options`, then behaves as if `copy_symlink(from, to)`.
:* Otherwise, reports an error.
* Otherwise, if `from` is a regular file, then
:* If `copy_options::directories_only` is present in `options`, does nothing.
:* Otherwise, if `copy_options::create_symlinks` is present in `options`, creates a symlink to `to`. Note: `from` must be an absolute path unless `to` is in the current directory.
:* Otherwise, if `copy_options::create_hard_links` is present in `options`, creates a hard link to `to`.
:* Otherwise, if `to` is a directory, then behaves as if `copy_file(from, to/from.filename(), options)` (creates a copy of `from` as a file in the directory `to`).
:* Otherwise, behaves as if `copy_file(from, to, options)` (copies the file).
* Otherwise, if `from` is a directory and `copy_options::create_symlinks` is set in `options`, reports an error with an error code equal to `std::make_error_code(std::errc::is_a_directory)`.
* Otherwise, if `from` is a directory and either `options` has `copy_options::recursive` or is `copy_options::none`,
:* If `to` does not exist, first executes `create_directory(to, from)` (creates the new directory with a copy of the old directory's attributes).
:* Then, whether `to` already existed or was just created, iterates over the files contained in `from` as if by `for (const std::filesystem::directory_entry& x : std::filesystem::directory_iterator(from))` and for each directory entry, recursively calls `copy(x.path(), to/x.path().filename(), options , where ''in-recursive-copy'' is a special bit that has no other effect when set in `options`. (The sole purpose of setting this bit is to prevent recursive copying subdirectories if `options` is `copy_options::none`.)
* Otherwise does nothing.

## Parameters


### Parameters

- `from` - path to the source file, directory, or symlink
- `to` - path to the target file, directory, or symlink
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Notes

The default behavior when copying directories is the non-recursive copy: the files are copied, but not the subdirectories:

```cpp
// Given
// /dir1 contains /dir1/file1, /dir1/file2, /dir1/dir2
// and /dir1/dir2 contains /dir1/dir2/file3
// After
std::filesystem::copy("/dir1", "/dir3");
// /dir3 is created (with the attributes of /dir1)
// /dir1/file1 is copied to /dir3/file1
// /dir1/file2 is copied to /dir3/file2
```

While with `copy_options::recursive`, the subdirectories are also copied, with their content, recursively.

```cpp
// ...but after
std::filesystem::copy("/dir1", "/dir3", std::filesystem::copy_options::recursive);
// /dir3 is created (with the attributes of /dir1)
// /dir1/file1 is copied to /dir3/file1
// /dir1/file2 is copied to /dir3/file2
// /dir3/dir2 is created (with the attributes of /dir1/dir2)
// /dir1/dir2/file3 is copied to /dir3/dir2/file3
```


## Example


## Defect reports


## See also


| cpp/filesystem/dsc copy_options | (see dedicated page) |
| cpp/filesystem/dsc copy_symlink | (see dedicated page) |
| cpp/filesystem/dsc copy_file | (see dedicated page) |

