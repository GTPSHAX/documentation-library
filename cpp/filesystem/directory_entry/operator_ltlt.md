---
title: operator<<(std::filesystem::directory_entry)
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/directory_entry/operator_ltlt
---


# operator<<small|(std::filesystem::directory_entry)


```cpp
dcl|since=c++17|1=
template< class CharT, class Traits >
friend std::basic_ostream<CharT,Traits>&
operator<<( std::basic_ostream<CharT,Traits>& os, const directory_entry& d );
```

Performs stream output on the directory entry `d`. Equivalent to `return os << d.path();`.
This prevents undesirable conversions in the presence of a `using namespace std::filesystem;` using-directive.

## Parameters


### Parameters

- `os` - stream to perform output on
- `d` - `directory_entry` to be inserted

## Return value

`os`

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    const auto entries = {fs::directory_entry{fs::current_path()},
                          fs::directory_entry{fs::temp_directory_path()}<!---->};

    for (const fs::directory_entry& de : entries)
        std::cout << de << '\n';
}
```


**Output:**
```
"/home/猫"
"/tmp"
```


## See also


| cpp/filesystem/path/dsc operator_ltltgtgt | (see dedicated page) |

