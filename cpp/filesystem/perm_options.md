---
title: std::filesystem::perm_options
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/perm_options
---

ddcl|header=filesystem|since=c++17|1=
enum class perm_options {
replace = /* unspecified */,
add = /* unspecified */,
remove = /* unspecified */,
nofollow = /* unspecified */
};
This type represents available options that control the behavior of the function `std::filesystem::permissions()`.

## Member constants

At most one of `add`, `remove`, `replace` may be present, otherwise the behavior of the permissions function is undefined.


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |
| dsc | |
| |`replace` | |
| |permissions will be completely replaced by the argument to  (default behavior) | |
| dsc | |
| |`add` | |
| |permissions will be replaced by the bitwise OR of the argument and the current permissions | |
| dsc | |
| |`remove` | |
| |permissions will be replaced by the bitwise AND of the negated argument and current permissions | |
| dsc | |
| |`nofollow` | |
| |permissions will be changed on the symlink itself, rather than on the file it resolves to | |


## Example


## See also


| cpp/filesystem/dsc permissions | (see dedicated page) |
| cpp/filesystem/dsc perms | (see dedicated page) |

