---
title: std::filesystem::path::replace_extension
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/replace_extension
---


```cpp
dcl|since=c++17|1=
path& replace_extension( const path& replacement = path() );
```

Replaces the extension with `replacement` or removes it when the default value of `replacement` is used.
Firstly, if this path has an , it is removed from the generic-format view of the pathname.
Then, a dot character is appended to the generic-format view of the pathname, if `replacement` is not empty and does not begin with a dot character.
Then `replacement` is appended as if by `operator+.

## Parameters


### Parameters

- `replacement` - the extension to replace with

## Return value

`*this`

## Notes

The type of `replacement` is `std::filesystem::path` even though it is not intended to represent an object on the file system in order to correctly account for the filesystem character encoding.

## Example


### Example

```cpp
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <utility>

int main()
{
    const int width1{18}, width2{11}; // columns' width

    std::cout << std::left << std::setw(width1) << "Path:"
              << std::setw(width2) << "Ext:" << "Result:\n";
    for (const auto& [p, e] : {
            std::make_pair("/foo/bar.jpg", ".png"),
            {"/foo/bar.jpg", "png"},
            {"/foo/bar.jpg", "."},
            {"/foo/bar.jpg", ""},
            {"/foo/bar.", "png"},
            {"/foo/bar", ".png"},
            {"/foo/bar", "png"},
            {"/foo/bar", "."},
            {"/foo/bar", ""},
            {"/foo/.", ".png"},
            {"/foo/.", "png"},
            {"/foo/.", "."},
            {"/foo/.", ""},
            {"/foo/", ".png"},
            {"/foo/", "png"}<!---->})
    {
        std::filesystem::path path{p}, ext{e};
        std::cout << std::setw(width1) << path << std::setw(width2) << ext;
        path.replace_extension(ext);
        std::cout << path << '\n';
    }
}
```


**Output:**
```
Path:             Ext:       Result:
"/foo/bar.jpg"    ".png"     "/foo/bar.png"
"/foo/bar.jpg"    "png"      "/foo/bar.png"
"/foo/bar.jpg"    "."        "/foo/bar."
"/foo/bar.jpg"    ""         "/foo/bar"
"/foo/bar."       "png"      "/foo/bar.png"
"/foo/bar"        ".png"     "/foo/bar.png"
"/foo/bar"        "png"      "/foo/bar.png"
"/foo/bar"        "."        "/foo/bar."
"/foo/bar"        ""         "/foo/bar"
"/foo/."          ".png"     "/foo/..png"
"/foo/."          "png"      "/foo/..png"
"/foo/."          "."        "/foo/.."
"/foo/."          ""         "/foo/."
"/foo/"           ".png"     "/foo/.png"
"/foo/"           "png"      "/foo/.png"
```


## See also


| cpp/filesystem/path/dsc extension | (see dedicated page) |
| cpp/filesystem/path/dsc filename | (see dedicated page) |
| cpp/filesystem/path/dsc stem | (see dedicated page) |

