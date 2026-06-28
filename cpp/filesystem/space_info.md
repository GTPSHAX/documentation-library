---
title: std::filesystem::space_info
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/space_info
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
struct space_info {
std::uintmax_t capacity;
std::uintmax_t free;
std::uintmax_t available;
};
```

Represents the filesystem information as determined by `filesystem::space`.

## Member objects


## Non-member functions


| cpp/filesystem/space_info|title=operator==|inlinemem=true|compares two `space_infos|notes= | |

member|operator<small>(std::filesystem::space_info)</small>|ddcl|since=c++20|1=
friend bool operator==( const space_info&, const space_info& ) = default;
Checks if `capacity`, `free` and `available` of both arguments are equal respectively.

## Example


## See also


| cpp/filesystem/dsc space | (see dedicated page) |

