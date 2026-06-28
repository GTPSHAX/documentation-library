---
title: std::filesystem::directory_entry::assign
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/assign
---


```cpp
dcl|num=1|since=c++17|1=
void assign( const std::filesystem::path& p );
dcl|num=2|since=c++17|1=
void assign( const std::filesystem::path& p, std::error_code& ec );
```

Assigns new content to the directory entry object. Sets the path to `p` and calls `refresh` to update the cached attributes. If an error occurs, the values of the cached attributes are unspecified.
This function does not commit any changes to the filesystem.

## Parameters


### Parameters

- `p` - path to the filesystem object to which the directory entry will refer
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Example


### Example


**Output:**
```
The entry "/tmp" is a directory
entry.assign();
The entry "/tmp/cppreference.html" is a regular file
remove(entry);
The entry "/tmp/cppreference.html" is a regular file
entry.assign();
The entry "/tmp/cppreference.html" does not exists on the file system
```


## See also


| cpp/filesystem/directory_entry/dsc operator{{= | (see dedicated page) |

