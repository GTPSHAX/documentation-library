---
title: std::filesystem::recursive_directory_iterator
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
class recursive_directory_iterator;
```

`recursive_directory_iterator` is a *InputIterator* that iterates over the `cpp/filesystem/directory_entry|directory_entry` elements of a directory, and, recursively, over the entries of all subdirectories. The iteration order is unspecified, except that each directory entry is visited only once.
By default, symlinks are not followed, but this can be enabled by specifying the directory option `cpp/filesystem/directory_options|follow_directory_symlink` at construction time.
The special pathnames *dot* and *dot-dot* are skipped.
If the `recursive_directory_iterator` reports an error or is advanced past the last directory entry of the top-level directory, it becomes equal to the default-constructed iterator, also known as the end iterator. Two end iterators are always equal, dereferencing or incrementing the end iterator is undefined behavior.
If a file or a directory is deleted or added to the directory tree after the recursive directory iterator has been created, it is unspecified whether the change would be observed through the iterator.
If the directory structure contains cycles, the end iterator may be unreachable.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/filesystem/recursive_directory_iterator/dsc constructor | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc destructor | (see dedicated page) |

#### Observers

| cpp/filesystem/recursive_directory_iterator/dsc operator* | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc options | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc depth | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc recursion_pending | (see dedicated page) |

#### Modifiers

| cpp/filesystem/recursive_directory_iterator/dsc operator{{= | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc increment | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc pop | (see dedicated page) |
| cpp/filesystem/recursive_directory_iterator/dsc disable_recursion_pending | (see dedicated page) |


## Non-member functions


| cpp/filesystem/recursive_directory_iterator/dsc begin | (see dedicated page) |

Additionally, <sup>(until C++20)</sup> `1=operator==` and `1=operator!=` are<sup>(since C++20)</sup> `1=operator==` is provided as required by *InputIterator*.
It is unspecified <sup>(since C++20)</sup> whether `1=operator!=` is provided because it can be synthesized from `1=operator==`, and whether an equality operator is a member or non-member.

## Helper specializations


```cpp
dcl|since=c++20|1=
template<>
constexpr bool
ranges::enable_borrowed_range<std::filesystem::recursive_directory_iterator> = true;
dcl|since=c++20|1=
template<>
constexpr bool
ranges::enable_view<std::filesystem::recursive_directory_iterator> = true;
```

These specializations for `recursive_directory_iterator` make it a  and a .

## Notes

A `recursive_directory_iterator` typically holds a reference-counted ''pointer'' (to satisfy shallow-copy semantics of *InputIterator*) to an implementation object, which holds:
* a container (such as `std::vector`) of non-recursive `cpp/filesystem/directory_iterator|directory_iterator`s that forms the recursion stack,
* the recursion depth counter (accessible with `cpp/filesystem/recursive_directory_iterator/depth|depth()`),
* the directory options used at construction (accessible with `cpp/filesystem/recursive_directory_iterator/options|options()`),
* the pending recursion flag (accessible with `cpp/filesystem/recursive_directory_iterator/recursion_pending|recursion_pending()`, may be combined with the directory options to save space).

## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
namespace fs = std::filesystem;

int main()
{
    std::filesystem::current_path(std::filesystem::temp_directory_path());
    std::filesystem::create_directories("sandbox/a/b");
    std::ofstream("sandbox/file1.txt");
    std::filesystem::create_symlink("a", "sandbox/syma");

    // Iterate over the std::filesystem::directory_entry elements explicitly
    auto entry_length{3UZ};
    for (const fs::directory_entry& dir_entry :
            fs::recursive_directory_iterator("sandbox"))
    {
        std::cout << dir_entry << '\n';
        if (auto l{dir_entry.path().string().length()}; entry_length < l)
            entry_length = l;
    }
    std::cout << std::string(entry_length + 2, '-') << '\n';

    // Iterate over the std::filesystem::directory_entry elements using `auto`
    for (auto const& dir_entry : fs::recursive_directory_iterator("sandbox"))
        std::cout << dir_entry << '\n';

    std::filesystem::remove_all("sandbox");
}
```


**Output:**
```
"sandbox/syma"
"sandbox/file1.txt"
"sandbox/a"
"sandbox/a/b"
-------------------
"sandbox/syma"
"sandbox/file1.txt"
"sandbox/a"
"sandbox/a/b"
```


## Defect reports


## See also


| cpp/filesystem/dsc directory_iterator | (see dedicated page) |
| cpp/filesystem/dsc directory_entry | (see dedicated page) |
| cpp/filesystem/dsc directory_options | (see dedicated page) |

