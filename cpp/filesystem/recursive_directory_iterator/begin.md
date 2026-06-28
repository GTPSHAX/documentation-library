---
title: std::filesystem::end
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/recursive_directory_iterator/begin
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|
recursive_directory_iterator begin( recursive_directory_iterator iter ) noexcept;
dcl|num=2|since=c++17|
recursive_directory_iterator end( recursive_directory_iterator ) noexcept;
```

1. Returns `iter` unchanged.
2. Returns a default-constructed `cpp/filesystem/recursive_directory_iterator|recursive_directory_iterator`, which serves as the end iterator. The argument is ignored.
These non-member functions enable the use of `recursive_directory_iterator`s with range-based for loops<sup>(since C++20)</sup>  and make `recursive_directory_iterator` a .

## Parameters


### Parameters

- `iter` - a `recursive_directory_iterator`

## Return value

1. `iter` unchanged.
2. End iterator (default-constructed `recursive_directory_iterator`).

## Example


### Example

```cpp
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::current_path(fs::temp_directory_path());
    fs::create_directories("sandbox/a/b");
    std::ofstream("sandbox/file1.txt");
    fs::create_symlink("a", "sandbox/syma");

    std::cout << "Print dir structure using OS specific command 'tree':\n";
    std::system("tree --noreport sandbox");

    std::cout << "\nPrint dir structure using directory iterator:\n";
    for (auto& p : fs::recursive_directory_iterator("sandbox"))
        std::cout << p << '\n';

    fs::remove_all("sandbox");
}
```


**Output:**
```
Print dir structure using OS specific command 'tree':
sandbox
├── a
│   └── b
├── file1.txt
└── syma -> a

Print dir structure using directory iterator:
"sandbox/syma"
"sandbox/file1.txt"
"sandbox/a"
"sandbox/a/b"
```


## Defect reports


## See also


| cpp/filesystem/directory_iterator/dsc begin | (see dedicated page) |

