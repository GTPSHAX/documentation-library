---
title: std::filesystem::permissions
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/permissions
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|1=
void permissions( const std::filesystem::path& p,
std::filesystem::perms prms,
std::filesystem::perm_options opts = perm_options::replace );
dcl|num=2|since=c++17|1=
void permissions( const std::filesystem::path& p,
std::filesystem::perms prms,
std::error_code& ec ) noexcept;
dcl|num=3|since=c++17|1=
void permissions( const std::filesystem::path& p,
std::filesystem::perms prms,
std::filesystem::perm_options opts,
std::error_code& ec );
```

Changes access permissions of the file to which `p` resolves, as if by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/fchmodat.html `fchmodat`]. Symlinks are followed unless `perm_options::nofollow` is set in `opts`.
The second signature behaves as if called with `opts` set to `perm_options::replace`.
The effects depend on `prms` and `opts` as follows:
* If `opts` is `perm_options::replace`, file permissions are set to exactly `prms & std::filesystem::perms::mask` (meaning, every valid bit of `prms` is applied).
* If `opts` is `perm_options::add`, the file permissions are set to exactly `status(p).permissions()  (meaning, any valid bit that is set in `prms`, but not in the file's current permissions is added to the file's permissions).
* If `opts` is `perm_options::remove`, the file permissions are set to exactly `status(p).permissions() & ~(prms & perms::mask)` (meaning, any valid bit that is clear in `prms`, but set in the file's current permissions is cleared in the file's permissions).
`opts` is required to have only one of `replace`, `add`, or `remove` to be set.
The non-throwing overload has no special action on error.

## Parameters


### Parameters

- `p` - path to examine
- `prms` - permissions to set, add, or remove
- `opts` - options controlling the action taken by this function
- `ec` - out-parameter for error reporting in the non-throwing overload

## Return value

(none)

## Exceptions


## Notes

Permissions may not necessarily be implemented as bits, but they are treated that way conceptually.
Some permission bits may be ignored on some systems, and changing some bits may automatically change others (e.g. on platforms without owner/group/all distinction, setting any of the three write bits set all three).

## Example


## See also


| cpp/filesystem/dsc perms | (see dedicated page) |
| cpp/filesystem/dsc status | (see dedicated page) |

