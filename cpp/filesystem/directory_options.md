---
title: std::filesystem::directory_options
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_options
---

ddcl|header=filesystem|since=c++17|1=
enum class directory_options {
none = /* unspecified */,
follow_directory_symlink = /* unspecified */,
skip_permission_denied = /* unspecified */
};
This type represents available options that control the behavior of the `cpp/filesystem/directory_iterator` and `cpp/filesystem/recursive_directory_iterator`.

## Constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |
| dsc | |
| |`none` | |
| |(default) skip directory symlinks, “permission denied” is error | |
| dsc | |
| |`follow_directory_symlink` | |
| |follow rather than skip directory symlinks | |
| dsc | |
| |`skip_permission_denied` | |
| |skip directories that would otherwise result in “permission denied” errors | |


## Example

