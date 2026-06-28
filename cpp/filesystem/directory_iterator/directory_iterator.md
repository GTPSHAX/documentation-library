---
title: std::filesystem::directory_iterator::directory_iterator
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_iterator/directory_iterator
---


```cpp
dcl|num=1|since=c++17|1=
directory_iterator() noexcept;
dcl|num=2|since=c++17|1=
explicit directory_iterator( const std::filesystem::path& p );
dcl|num=3|since=c++17|1=
directory_iterator( const std::filesystem::path& p,
std::filesystem::directory_options options );
dcl|num=4|since=c++17|1=
directory_iterator( const std::filesystem::path& p, std::error_code& ec );
dcl|num=5|since=c++17|1=
directory_iterator( const std::filesystem::path& p,
std::filesystem::directory_options options,
std::error_code& ec );
dcl|num=6|since=c++17|1=
directory_iterator( const directory_iterator& other ) = default;
dcl|num=7|since=c++17|1=
directory_iterator( directory_iterator&& other ) = default;
```

Constructs a new directory iterator.
1. Constructs the end iterator.
2. Constructs a directory iterator that refers to the first directory entry of a directory identified by `p`. If `p` refers to a non-existing file or not a directory, throws `std::filesystem::filesystem_error`.
3. Same as , but if `std::filesystem::directory_options::skip_permission_denied` is set in `options` and construction encounters a permissions denied error, constructs the end iterator and does not report an error.
4. Constructs a directory iterator that refers to the first directory entry of a directory identified by `p`. If `p` refers to a non-existing file or not a directory, returns the end iterator and sets `ec`.
5. Same as , but if `std::filesystem::directory_options::skip_permission_denied` is set in `options` and construction encounters a permissions denied error, constructs the end iterator and does not report an error.
6. Copy constructor.
7. Move constructor.

## Parameters


### Parameters

- `p` - path to the filesystem object to which the directory iterator will refer
- `ec` - out-parameter for error reporting in the non-throwing overloads
- `options` - the set of *BitmaskType* options that control the behavior of the directory iterator
- `other` - another directory iterator to use as source to initialize the directory iterator with

## Exceptions


## Notes

To iterate over the current directory, construct the iterator as `directory_iterator(".")` instead of `directory_iterator("")`.

## Example

