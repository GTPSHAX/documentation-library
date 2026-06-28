---
title: std::filesystem::operator/(std::filesystem::path)
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/operator_slash
---

ddcl|since=c++17|
friend path operator/( const path& lhs, const path& rhs );
Concatenates two path components using the preferred directory separator if appropriate (see `cpp/filesystem/path/append|operator/ for details).
Effectively returns `1=path(lhs) /= rhs`.
This prevents undesirable conversions in the presence of a `using namespace std::filesystem;` ''using-directive''.

## Parameters


### Parameters

- `lhs, rhs` - paths to concatenate

## Return value

The result of path concatenation.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>

int main()
{
#   if defined(_WIN32) // see e.g. stackoverflow.com/questions/142508

    std::filesystem::path p = "C:";

    std::cout << "\"C:\" / \"Users\" / \"batman\" == " << p / "Users" / "batman" << '\n';

#   else // __linux__ etc

    std::filesystem::path p = "/home";

    std::cout << "\"/home\" / \"tux\" / \".fonts\" == " << p / "tux" / ".fonts" << '\n';

#   endif
}
```


**Output:**
```
Windows specific output:
"C:" / "Users" / "batman" == "C:Users\\batman"

Linux etc specific output:
"/home" / "tux" / ".fonts" == "/home/tux/.fonts"
```


## Defect reports


## See also


| cpp/filesystem/path/dsc append | (see dedicated page) |

