---
title: std::filesystem::file_type
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/file_type
---

ddcl|header=filesystem|since=c++17|1=
enum class file_type {
none = /* unspecified */,
not_found = /* unspecified */,
regular = /* unspecified */,
directory = /* unspecified */,
symlink = /* unspecified */,
block = /* unspecified */,
character = /* unspecified */,
fifo = /* unspecified */,
socket = /* unspecified */,
unknown = /* unspecified */,
/* implementation-defined */
};
`file_type` defines constants that indicate a type of a file or directory a path refers to. The value of the enumerators are distinct.

## Constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |


## Example


## See also


| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/directory_entry/dsc is_regular_file | (see dedicated page) |

