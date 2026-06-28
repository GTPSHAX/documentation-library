---
title: std::hash<std::filesystem::path>
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/hash
---


# hashsmall|<std::filesystem::path>

ddcl|header=filesystem|since=c++17|
template<>
struct hash<std::filesystem::path>;
The template specialization of `std::hash` for `std::filesystem::path` allows users to obtain hash values of `std::filesystem::path`.
The `operator()` of this specialization is `noexcept`. For every `std::filesystem::path` value `p`, } is equal to `std::filesystem::hash_value(p)`.
This specialization was absent from the C++17 standard publication, see .

## Example


### Example

```cpp
#include <cassert>
#include <cstddef>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <unordered_set>
namespace fs = std::filesystem;

void show_hash(fs::path const& p)
{
    std::cout << std::hex << std::uppercase << std::setw(16)
              << std::hash<fs::path>{}(p) << " : " << p << '\n';
}

int main()
{
    auto tmp1 = fs::path{"/tmp"};
    auto tmp2 = fs::path{"/tmp/../tmp"};
    assert(!(tmp1 == tmp2));
    assert(fs::equivalent(tmp1, tmp2));
    show_hash(tmp1);
    show_hash(tmp2);

    for (auto s : {"/a///b", "/a//b", "/a/c", "...", "..", ".", ""})
        show_hash(s);

    std::unordered_set<fs::path, std::hash<fs::path>> dirs{
        "/bin", "/bin", "/lib", "/lib", "/opt", "/opt", "/tmp", "/tmp/../tmp"};
    for (fs::path const& p : dirs)
        std::cout << p << ' ';
    std::cout << '\n';
}
```


**Output:**
```
6050C47ADB62DFE5 : "/tmp"
62795A58B69AD90A : "/tmp/../tmp"
FF302110C9991974 : "/a///b"
FF302110C9991974 : "/a//b"
FD6167277915D464 : "/a/c"
C42040F82CD8B542 : "..."
D2D30154E0B78BBC : ".."
D18C722215ED0530 : "."
               0 : ""
"/tmp/../tmp" "/opt" "/lib" "/tmp" "/bin"
```


## See also


| cpp/utility/dsc hash | (see dedicated page) |
| cpp/filesystem/path/dsc hash_value | (see dedicated page) |

