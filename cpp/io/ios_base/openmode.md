---
title: std::ios_base::openmode
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/openmode
---


```cpp
dcl|
typedef /* implementation defined */ openmode;
dcl|1=
static constexpr openmode app       = /* implementation defined */;
static constexpr openmode binary    = /* implementation defined */;
static constexpr openmode in        = /* implementation defined */;
static constexpr openmode out       = /* implementation defined */;
static constexpr openmode trunc     = /* implementation defined */;
static constexpr openmode ate       = /* implementation defined */;
dcl|since=c++23|1=
static constexpr openmode noreplace = /* implementation defined */;
```

Specifies available file open flags. It is a *BitmaskType*, the following constants are defined:

## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    const char* fname = "unique_name.txt";

    // write to a temporary stream object
    std::fstream(fname, std::ios::out {{!
```

std::string s;
std::fstream(fname, std::ios::in) >> s;
std::cout << s << '\n';
}
|output=
Hi

## See also


| cpp/io/basic_filebuf/dsc open | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc constructor | (see dedicated page) |

