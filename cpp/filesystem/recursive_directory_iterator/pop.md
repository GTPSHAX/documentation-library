---
title: std::filesystem::recursive_directory_iterator::pop
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator/pop
---


```cpp
dcl|since=c++17|num=1|1=
void pop();
dcl|since=c++17|num=2|1=
void pop( std::error_code& ec );
```

Moves the iterator one level up in the directory hierarchy. Invalidates all copies of the previous value of `*this`.
If the parent directory is outside directory hierarchy that is iterated on (i.e. `1=depth() == 0`), sets `*this` to an end directory iterator.

## Parameters


### Parameters

- `ec` - error code to store the error status to

## Return value

(none)

## Exceptions


## Example

