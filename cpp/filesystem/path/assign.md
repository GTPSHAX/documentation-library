---
title: std::filesystem::path::assign
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/assign
---


```cpp
dcl | num=1 | since=c++17 | 1=
path& assign( string_type&& source );
dcl | num=2 | since=c++17 | 1=
template< class Source >
path& assign( const Source& source );
dcl | num=3 | since=c++17 | 1=
template< class InputIt >
path& assign( InputIt first, InputIt last );
```

Replaces the contents to the `path` object by a new pathname constructed from the given character sequence.
1. Assigns the pathname identified by the detected-format string `source`, which is left in valid, but unspecified state.
2. Assigns the pathname identified by the detected-format character range `source`.
3. Assigns the pathname identified by detected-format character range `[first, last)`.

## Parameters


### Parameters


**Type requirements:**


## Return value

`*this`

## Defect reports


## See also

