---
title: Filesystem library
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem
---


# Filesystem library mark since c++17

The Filesystem library provides facilities for performing operations on file systems and their components, such as paths, regular files, and directories.
The filesystem library was originally developed as [https://www.boost.org/doc/libs/release/libs/filesystem/doc/index.htm boost.filesystem], was published as the technical specification ISO/IEC TS 18822:2015, and finally merged to ISO C++ as of C++17. The boost implementation is currently available on more compilers and platforms than the C++17 library.
The filesystem library facilities may be unavailable if a hierarchical file system is not accessible to the implementation, or if it does not provide the necessary capabilities. Some features may not be available if they are not supported by the underlying file system (e.g. the FAT filesystem lacks symbolic links and forbids multiple hardlinks). In those cases, errors must be reported.
The behavior is undefined if the calls to functions in this library introduce a ''file system race'', that is, when multiple threads, processes, or computers interleave access and modification to the same object in a file system.

### Library-wide definitions

* ''file'': a file system object that holds data, can be written to, read from, or both. Files have names, attributes, one of which is file type:
:* ''directory'': a file that acts as a container of directory entries, which identify other files (some of which may be other, nested directories). When discussing a particular file, the directory in which it appears as an entry is its ''parent directory''. The parent directory can be represented by the relative pathname `".."`.
:* ''regular file'': a directory entry that associates a name with an existing file (i.e. a ''hard link''). If multiple hard links are supported, the file is removed after the last hard link to it is removed.
:* ''symbolic link'': a directory entry that associates a name with a path, which may or may not exist.
:* other special file types: ''block'', ''character'', ''fifo'', ''socket''.
* ''file name'': a string of characters that names a file. Permissible characters, case sensitivity, maximum length, and the disallowed names are implementation-defined. Names `"."` (dot) and `".."` (dot-dot) have special meaning at library level.
* ''path'': sequence of elements that identifies a file. It begins with an optional *root-name* (e.g. `"C:"` or `"//server"` on Windows), followed by an optional *root-directory* (e.g. `"/"` on Unix), followed by a sequence of zero or more file names (all but last of which have to be directories or links to directories). The native format (e.g. which characters are used as separators) and character encoding of the string representation of a path (the ''pathname'') is implementation-defined, this library provides portable representation of paths.
:* ''absolute path'': a path that unambiguously identifies the location of a file.
:* ''canonical path'': an absolute path that includes no symlinks, `"."` or `".."` elements.
:* ''relative path'': a path that identifies the location of a file relative to some location on the file system. The special path names `"."` (dot, "current directory") and `".."` (dot-dot, "parent directory") are relative paths.


| filesystem | |
| std::filesystem | |
| cpp/filesystem/dsc path | (see dedicated page) |
| cpp/filesystem/dsc filesystem_error | (see dedicated page) |
| cpp/filesystem/dsc directory_entry | (see dedicated page) |
| cpp/filesystem/dsc directory_iterator | (see dedicated page) |
| cpp/filesystem/dsc recursive_directory_iterator | (see dedicated page) |
| cpp/filesystem/dsc file_status | (see dedicated page) |
| cpp/filesystem/dsc space_info | (see dedicated page) |
| cpp/filesystem/dsc file_type | (see dedicated page) |
| cpp/filesystem/dsc perms | (see dedicated page) |
| cpp/filesystem/dsc perm_options | (see dedicated page) |
| cpp/filesystem/dsc copy_options | (see dedicated page) |
| cpp/filesystem/dsc directory_options | (see dedicated page) |
| cpp/filesystem/dsc file_time_type | (see dedicated page) |
| filesystem | |
| std::filesystem | |
| cpp/filesystem/dsc absolute | (see dedicated page) |
| cpp/filesystem/dsc canonical | (see dedicated page) |
| cpp/filesystem/dsc relative | (see dedicated page) |
| cpp/filesystem/dsc copy | (see dedicated page) |
| cpp/filesystem/dsc copy_file | (see dedicated page) |
| cpp/filesystem/dsc copy_symlink | (see dedicated page) |
| cpp/filesystem/dsc create_directory | (see dedicated page) |
| cpp/filesystem/dsc create_hard_link | (see dedicated page) |
| cpp/filesystem/dsc create_symlink | (see dedicated page) |
| cpp/filesystem/dsc current_path | (see dedicated page) |
| cpp/filesystem/dsc exists | (see dedicated page) |
| cpp/filesystem/dsc equivalent | (see dedicated page) |
| cpp/filesystem/dsc file_size | (see dedicated page) |
| cpp/filesystem/dsc hard_link_count | (see dedicated page) |
| cpp/filesystem/dsc last_write_time | (see dedicated page) |
| cpp/filesystem/dsc permissions | (see dedicated page) |
| cpp/filesystem/dsc read_symlink | (see dedicated page) |
| cpp/filesystem/dsc remove | (see dedicated page) |
| cpp/filesystem/dsc rename | (see dedicated page) |
| cpp/filesystem/dsc resize_file | (see dedicated page) |
| cpp/filesystem/dsc space | (see dedicated page) |
| cpp/filesystem/dsc status | (see dedicated page) |
| cpp/filesystem/dsc temp_directory_path | (see dedicated page) |

#### File types

| cpp/filesystem/dsc is_block_file | (see dedicated page) |
| cpp/filesystem/dsc is_character_file | (see dedicated page) |
| cpp/filesystem/dsc is_directory | (see dedicated page) |
| cpp/filesystem/dsc is_empty | (see dedicated page) |
| cpp/filesystem/dsc is_fifo | (see dedicated page) |
| cpp/filesystem/dsc is_other | (see dedicated page) |
| cpp/filesystem/dsc is_regular_file | (see dedicated page) |
| cpp/filesystem/dsc is_socket | (see dedicated page) |
| cpp/filesystem/dsc is_symlink | (see dedicated page) |
| cpp/filesystem/dsc status_known | (see dedicated page) |


## Notes

Using this library may require additional compiler/linker options. GNU implementation prior to 9.1 requires linking with  and LLVM implementation prior to LLVM 9.0 requires linking with .

## See also

