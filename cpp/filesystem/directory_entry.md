---
title: std::filesystem::directory_entry
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
class directory_entry;
```

Represents a directory entry. The object stores a `path` as a member and may also store additional file attributes (hard link count, status, symlink status, file size, and last write time) during directory iteration.

## Member functions


| cpp/filesystem/directory_entry/dsc constructor | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc destructor | (see dedicated page) |

#### Modifiers

| cpp/filesystem/directory_entry/dsc operator{{= | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc assign | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc replace_filename | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc refresh | (see dedicated page) |

#### Observers

| cpp/filesystem/directory_entry/dsc path | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc exists | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_directory | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_other | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_socket | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc file_size | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc hard_link_count | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc last_write_time | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc status | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc operator_cmp | (see dedicated page) |


## Non-member functions


| cpp/filesystem/directory_entry/dsc operator_ltlt | (see dedicated page) |


## Defect reports

