---
title: std::filesystem::directory_iterator
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_iterator
---


```cpp
**Header:** `<`filesystem`>`
dcl|since=c++17|1=
class directory_iterator;
```

`directory_iterator` is a *InputIterator* that iterates over the `cpp/filesystem/directory_entry|directory_entry` elements of a directory (but does not visit the subdirectories). The iteration order is unspecified, except that each directory entry is visited only once. The special pathnames *dot* and *dot-dot* are skipped.
If the `directory_iterator` reports an error or is advanced past the last directory entry, it becomes equal to the default-constructed iterator, also known as the end iterator. Two end iterators are always equal, dereferencing or incrementing the end iterator is undefined behavior.
If a file or a directory is deleted or added to the directory tree after the directory iterator has been created, it is unspecified whether the change would be observed through the iterator.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/filesystem/directory_iterator/dsc constructor | (see dedicated page) |
| cpp/filesystem/directory_iterator/dsc destructor | (see dedicated page) |
| cpp/filesystem/directory_iterator/dsc operator{{= | (see dedicated page) |
| cpp/filesystem/directory_iterator/dsc operator* | (see dedicated page) |
| cpp/filesystem/directory_iterator/dsc increment | (see dedicated page) |


## Non-member functions


| cpp/filesystem/directory_iterator/dsc begin | (see dedicated page) |

Additionally, <sup>(until C++20)</sup> `1=operator==` and `1=operator!=` are<sup>(since C++20)</sup> `1=operator==` is provided as required by *InputIterator*.
It is unspecified <sup>(since C++20)</sup> whether `1=operator!=` is provided because it can be synthesized from `1=operator==`, and whether an equality operator is a member or non-member.

## Helper specializations


```cpp
dcl|since=c++20|1=
template<>
constexpr bool
ranges::enable_borrowed_range<std::filesystem::directory_iterator> = true;
dcl|since=c++20|1=
template<>
constexpr bool
ranges::enable_view<std::filesystem::directory_iterator> = true;
```

These specializations for `directory_iterator` make it a  and a .

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>

int main()
{
    const std::filesystem::path sandbox{"sandbox"};
    std::filesystem::create_directories(sandbox/"dir1"/"dir2");
    std::ofstream{sandbox/"file1.txt"};
    std::ofstream{sandbox/"file2.txt"};

    std::cout << "directory_iterator:\n";
    // directory_iterator can be iterated using a range-for loop
    for (auto const& dir_entry : std::filesystem::directory_iterator{sandbox}) 
        std::cout << dir_entry.path() << '\n';

    std::cout << "\ndirectory_iterator as a range:\n";
    // directory_iterator behaves as a range in other ways, too
    std::ranges::for_each(
        std::filesystem::directory_iterator{sandbox},
        [](const auto& dir_entry) { std::cout << dir_entry << '\n'; });

    std::cout << "\nrecursive_directory_iterator:\n";
    for (auto const& dir_entry : std::filesystem::recursive_directory_iterator{sandbox}) 
        std::cout << dir_entry << '\n';

    // delete the sandbox dir and all contents within it, including subdirs
    std::filesystem::remove_all(sandbox);
}
```


**Output:**
```
directory_iterator:
"sandbox/file2.txt"
"sandbox/file1.txt"
"sandbox/dir1"

directory_iterator as a range:
"sandbox/file2.txt"
"sandbox/file1.txt"
"sandbox/dir1"

recursive_directory_iterator:
"sandbox/file2.txt"
"sandbox/file1.txt"
"sandbox/dir1"
"sandbox/dir1/dir2"
```


## Defect reports


## See also


| cpp/filesystem/dsc recursive_directory_iterator | (see dedicated page) |
| cpp/filesystem/dsc directory_options | (see dedicated page) |
| cpp/filesystem/dsc directory_entry | (see dedicated page) |

