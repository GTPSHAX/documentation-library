---
title: std::basic_ofstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ofstream
---

ddcl|header=fstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_ofstream : public std::basic_ostream<CharT, Traits>
The class template `basic_ofstream` implements high-level output operations on file based streams. It interfaces a file-based streambuffer (`std::basic_filebuf`) with the high-level interface of (`std::basic_ostream`).
A typical implementation of `std::basic_ofstream` holds only one non-derived data member: an instance of `std::basic_filebuf<CharT, Traits>`.

## Member functions


| cpp/io/basic_fstream/dsc constructor|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc destructor|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc rdbuf|basic_ofstream | (see dedicated page) |
| cpp/io/basic_ofstream/dsc native_handle | (see dedicated page) |

#### File operations

| cpp/io/basic_fstream/dsc is_open|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc open|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc close|basic_ofstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_fstream/dsc swap2|basic_ofstream | (see dedicated page) |


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
    {
        std::ofstream ostrm(filename, std::ios::binary);
        double d = 3.14;
        ostrm.write(reinterpret_cast<char*>(&d), sizeof d); // binary output
        ostrm << 123 << "abc" << '\n';                      // text output
    }

    // read back
    std::ifstream istrm(filename, std::ios::binary);
    double d;
    istrm.read(reinterpret_cast<char*>(&d), sizeof d);
    int n;
    std::string s;
    istrm >> n >> s;
    std::cout << " read back: " << d << ' ' << n << ' ' << s << '\n';
}
```


**Output:**
```
read back: 3.14 123 abc
```

