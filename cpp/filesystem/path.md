---
title: std::filesystem::path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|
class path;
```

Objects of type `path` represent paths on a filesystem. Only syntactic aspects of paths are handled: the pathname may represent a non-existing path or even one that is not allowed to exist on the current file system or OS.
The path name has the following syntax:
# *root-name*: identifies the root on a filesystem with multiple roots (such as `"C:"` or `"//myserver"`). In case of ambiguity, the longest sequence of characters that forms a valid *root-name* is treated as the *root-name*. The standard library may define additional root-names besides the ones understood by the OS API.
# *root-directory*: a directory separator that, if present, marks this path as ''absolute''. If it is missing (and the first element other than the root name is a file name), then the path is ''relative'' and requires another path as the starting location to resolve to a file name.
# Zero or more of the following:
:* *file-name*: sequence of characters that aren't directory separators or preferred directory separators (additional limitations may be imposed by the OS or file system). This name may identify a file, a hard link, a symbolic link, or a directory. Two special *file-name*s are recognized:
::* *dot*: the file name consisting of a single dot character `.` is a directory name that refers to the current directory.
::* *dot-dot*: the file name consisting of two dot characters `..` is a directory name that refers to the parent directory.
:* *directory-separator*s: the forward slash character `/` or the alternative character provided as `path::preferred_separator`. If this character is repeated, it is treated as a single directory separator: `/usr///////lib` is the same as `/usr/lib`.
A path can be ''normalized'' by following this algorithm:
# If the path is empty, stop (normal form of an empty path is an empty path).
# Replace each *directory-separator* (which may consist of multiple slashes) with a single `path::preferred_separator`.
# Replace each slash character in the *root-name* with `path::preferred_separator`.
# Remove each *dot* and any immediately following *directory-separator*.
# Remove each non-*dot-dot* filename immediately followed by a *directory-separator* and a *dot-dot*, along with any immediately following *directory-separator*.
# If there is *root-directory*, remove all *dot-dot*s and any *directory-separator*s immediately following them.
# If the last filename is *dot-dot*, remove any trailing *directory-separator*.
# If the path is empty, add a *dot* (normal form of `./` is `.`).
The path can be traversed element-wise via iterators returned by the `begin()` and `end()` functions, which views the path in generic format and iterates over root name, root directory, and the subsequent file name elements (directory separators are skipped except the one that identifies the root directory). If the very last element in the path is a directory separator, the last iterator will dereference to an empty element.
Calling any non-const member function of a `path` invalidates all iterators referring to elements of that object.
If the OS uses a ''native'' syntax that is different from the portable ''generic'' syntax described above, library functions that are defined to accept "detected format" accept path names in both formats: a detected format argument is taken to be in the generic format if and only if it matches the generic format but is not acceptable to the operating system as a native path. On those OS where native format differs between pathnames of directories and pathnames of files, a generic pathname is treated as a directory path if it ends on a directory separator and a regular file otherwise.
In any case, the path class behaves as if it stores a pathname in the native format and automatically converts to generic format as needed (each member function specifies which format it interprets the path as).
On POSIX systems, the generic format is the native format and there is no need to distinguish or convert between them.
Paths are implicitly convertible to and from `std::basic_string`s, which makes it possible to use them with other file APIs.
The  use `std::quoted` so that spaces do not cause truncation when later read by .
Decomposition member functions (e.g. `extension`) return `filesystem::path` objects instead of string objects as other APIs do.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`const_iterator`|a constant *InputIterator* with a `value_type` of `path` that meets all requirements of *BidirectionalIterator* except that for two equal dereferenceable iterators `a` and `b` of type `const_iterator`, there is no requirement that `*a` and `*b` refer to the same object. | |
| It is unspecified whether `const_iterator` is actually a *BidirectionalIterator* | |
| dsc mem enum|cpp/filesystem/path/format|determines how to interpret string representations of pathnames. | |
| The following enumerators are also defined: | |


| Item | Description |
|------|-------------|
| **Name** | Explanation |


## Member constants


| cpp/filesystem/path/dsc preferred_separator | (see dedicated page) |


## Member functions


| cpp/filesystem/path/dsc constructor | (see dedicated page) |
| cpp/filesystem/path/dsc destructor | (see dedicated page) |
| cpp/filesystem/path/dsc operator{{= | (see dedicated page) |
| cpp/filesystem/path/dsc assign | (see dedicated page) |

#### Concatenation

| cpp/filesystem/path/dsc append | (see dedicated page) |
| cpp/filesystem/path/dsc concat | (see dedicated page) |

#### Modifiers

| cpp/filesystem/path/dsc clear | (see dedicated page) |
| cpp/filesystem/path/dsc make_preferred | (see dedicated page) |
| cpp/filesystem/path/dsc remove_filename | (see dedicated page) |
| cpp/filesystem/path/dsc replace_filename | (see dedicated page) |
| cpp/filesystem/path/dsc replace_extension | (see dedicated page) |
| cpp/filesystem/path/dsc swap | (see dedicated page) |

#### Format observers

| cpp/filesystem/path/dsc native | (see dedicated page) |
| cpp/filesystem/path/dsc string | (see dedicated page) |
| cpp/filesystem/path/dsc generic_string | (see dedicated page) |

#### Compare

| cpp/filesystem/path/dsc compare | (see dedicated page) |

#### Generation

| cpp/filesystem/path/dsc lexically_normal | (see dedicated page) |

#### Decomposition

| cpp/filesystem/path/dsc root_name | (see dedicated page) |
| cpp/filesystem/path/dsc root_directory | (see dedicated page) |
| cpp/filesystem/path/dsc root_path | (see dedicated page) |
| cpp/filesystem/path/dsc relative_path | (see dedicated page) |
| cpp/filesystem/path/dsc parent_path | (see dedicated page) |
| cpp/filesystem/path/dsc filename | (see dedicated page) |
| cpp/filesystem/path/dsc stem | (see dedicated page) |
| cpp/filesystem/path/dsc extension | (see dedicated page) |

#### Queries

| cpp/filesystem/path/dsc empty | (see dedicated page) |
| cpp/filesystem/path/dsc has_path | (see dedicated page) |
| cpp/filesystem/path/dsc is_absrel | (see dedicated page) |

#### Iterators

| cpp/filesystem/path/dsc begin | (see dedicated page) |


## Non-member functions


| std::filesystem | |
| cpp/filesystem/path/dsc swap2 | (see dedicated page) |
| cpp/filesystem/path/dsc hash_value | (see dedicated page) |
| cpp/filesystem/path/dsc operator_cmp | (see dedicated page) |
| cpp/filesystem/path/dsc operator/ | (see dedicated page) |
| cpp/filesystem/path/dsc operator_ltltgtgt | (see dedicated page) |
| cpp/filesystem/path/dsc u8path | (see dedicated page) |


## Helper classes


| std | |
| cpp/filesystem/path/dsc hash | (see dedicated page) |
| cpp/filesystem/path/dsc formatter | (see dedicated page) |


## Defect reports

