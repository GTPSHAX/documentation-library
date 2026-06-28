---
title: std::filesystem::path::end
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/begin
---


```cpp
dcl|num=1|since=c++17|1=
iterator begin() const;
dcl|num=2|since=c++17|1=
iterator end() const;
```

1. Returns an iterator to the first element of the path. If the path is empty, the returned iterator is equal to `end()`.
2. Returns an iterator one past the last element of the path. Dereferencing this iterator is undefined behavior.
The sequence denoted by this pair of iterators consists of the following:
# *root-name* (if any).
# *root-directory* (if any).
# Sequence of *file-name*s, omitting any directory separators.
# If there is a directory separator after the last *file-name* in the path, the last element before the end iterator is an empty element.

## Parameters

(none)

## Return value

1. Iterator to the first element of the path.
2. Iterator one past the end of the path

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    const fs::path p = 
#   ifdef _WIN32
        "C:\\users\\abcdef\\AppData\\Local\\Temp\\";
#   else
        "/home/user/.config/Cppcheck/Cppcheck-GUI.conf";
#   endif
    std::cout << "Examining the path " << p << " through iterators gives\n";
    for (auto it = p.begin(); it != p.end(); ++it)
        std::cout << *it << " │ ";
    std::cout << '\n';
}
```


**Output:**
```
--- Windows ---
Examining the path "C:\users\abcdef\AppData\Local\Temp\" through iterators gives
"C:" │ "/" │ "users" │ "abcdef" │ "AppData" │ "Local" │ "Temp" │ "" │

--- UNIX ---
Examining the path "/home/user/.config/Cppcheck/Cppcheck-GUI.conf" through iterators gives
"/" │ "home" │ "user" │ ".config" │ "Cppcheck" │ "Cppcheck-GUI.conf" │
```

