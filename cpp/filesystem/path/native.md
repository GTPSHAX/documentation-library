---
title: std::filesystem::path::operator string_type()
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/native
---


```cpp
dcl|num=1|since=c++17|1=
const value_type* c_str() const noexcept;
dcl|num=2|since=c++17|1=
const string_type& native() const noexcept;
dcl|num=3|since=c++17|1=
operator string_type() const;
```

Accesses the native path name as a character string.
1. Equivalent to `native().c_str()`.
2. Returns the native-format representation of the pathname by reference.
3. Returns the native-format representation of the pathname by value.

## Parameters

(none)

## Return value

The native string representation of the pathname, using native syntax, native character type, and native character encoding. This string is suitable for use with OS APIs.

## Notes

The conversion function  is provided so that APIs that accept `std::basic_string` file names can use pathnames with no changes to code.

## Example


## See also


| cpp/filesystem/path/dsc string | (see dedicated page) |
| cpp/filesystem/path/dsc generic_string | (see dedicated page) |

