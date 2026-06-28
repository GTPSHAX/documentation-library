---
title: std::filesystem::recursive_directory_iterator::recursive_directory_iterator
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator/recursive_directory_iterator
---


```cpp
dcl|num=1|since=c++17|1=
recursive_directory_iterator() noexcept;
dcl|num=2|since=c++17|1=
recursive_directory_iterator( const recursive_directory_iterator& other );
dcl|num=3|since=c++17|1=
recursive_directory_iterator( recursive_directory_iterator&& other ) noexcept;
dcl|num=4|since=c++17|1=
explicit recursive_directory_iterator( const std::filesystem::path& p );
dcl|num=5|since=c++17|1=
recursive_directory_iterator(
const std::filesystem::path& p,
std::filesystem::directory_options options );
dcl|num=6|since=c++17|1=
recursive_directory_iterator(
const std::filesystem::path& p,
std::filesystem::directory_options options,
std::error_code& ec );
dcl|num=7|since=c++17|1=
recursive_directory_iterator( const std::filesystem::path& p, std::error_code& ec );
```

Constructs new recursive directory iterator.
1. Default constructor. Constructs an end iterator.
2. Copy constructor.
3. Move constructor.
@4-7@ Constructs an iterator that refers to the first entry in the directory that `p` resolves to.

## Parameters


### Parameters

- `p` - path to the filesystem object to which the directory iterator will refer
- `ec` - out-parameter for error reporting in the non-throwing overloads
- `options` - the set of *BitmaskType* options that control the behavior of the directory iterator
- `other` - another directory iterator to use as source to initialize the directory iterator with

## Exceptions


## Notes

Recursive directory iterators do not follow directory symlinks by default. To enable this behavior, specify `std::filesystem::directory_options|directory_options::follow_directory_symlink` among the `options` option set.

## Example


## Defect reports

