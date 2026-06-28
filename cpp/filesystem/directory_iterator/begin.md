---
title: std::filesystem::end
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_iterator/begin
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|
directory_iterator begin( directory_iterator iter ) noexcept;
dcl|num=2|since=c++17|
directory_iterator end( directory_iterator ) noexcept;
```

1. Returns `iter` unchanged.
2. Returns a default-constructed `cpp/filesystem/directory_iterator|directory_iterator`, which serves as the end iterator. The argument is ignored.
These non-member functions enable the use of `directory_iterator`s with range-based for loops<sup>(since C++20)</sup>  and make `directory_iterator` a .

## Parameters


### Parameters

- `iter` - a `directory_iterator`

## Return value

1. `iter` unchanged.
2. End iterator (default-constructed `directory_iterator`).

## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::create_directories("sandbox/a/b");
    std::ofstream("sandbox/file1.txt");
    std::ofstream("sandbox/file2.txt");
    for (auto& p : fs::directory_iterator("sandbox"))
        std::cout << p << '\n';
    fs::remove_all("sandbox");
}
```


**Output:**
```
"sandbox/a"
"sandbox/file1.txt"
"sandbox/file2.txt"
```


## Defect reports


## See also


| cpp/filesystem/recursive_directory_iterator/dsc begin | (see dedicated page) |

