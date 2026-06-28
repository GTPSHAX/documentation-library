---
title: std::basic_ifstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ifstream
---

ddcl|header=fstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_ifstream : public std::basic_istream<CharT, Traits>
The class template `basic_ifstream` implements high-level input operations on file-based streams. It interfaces a file-based streambuffer (`std::basic_filebuf`) with the high-level interface of (`std::basic_istream`).
A typical implementation of `std::basic_ifstream` holds only one non-derived data member: an instance of `std::basic_filebuf<CharT, Traits>`.

## Member functions


| cpp/io/basic_fstream/dsc constructor|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc destructor|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc rdbuf|basic_ifstream | (see dedicated page) |
| cpp/io/basic_ifstream/dsc native_handle | (see dedicated page) |

#### File operations

| cpp/io/basic_fstream/dsc is_open|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc open|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc close|basic_ifstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_fstream/dsc swap2|basic_ifstream | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::string filename = "Test.b";

    // prepare a file to read
    double d = 3.14;
    std::ofstream(filename, std::ios::binary)
        .write(reinterpret_cast<char*>(&d), sizeof d) << 123 << "abc";

    // open file for reading
    std::ifstream istrm(filename, std::ios::binary);
    if (!istrm.is_open())
        std::cout << "failed to open " << filename << '\n';
    else
    {
        double d;
        istrm.read(reinterpret_cast<char*>(&d), sizeof d); // binary input
        int n;
        std::string s;
        if (istrm >> n >> s)                               // text input
            std::cout << "read back from file: " << d << ' ' << n << ' ' << s << '\n';
    }
}
```


**Output:**
```
read back from file: 3.14 123 abc
```

