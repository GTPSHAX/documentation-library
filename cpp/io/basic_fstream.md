---
title: std::basic_fstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_fstream
---

ddcl|header=fstream|1=
template<
class CharT,
class Traits = std::char_traits<CharT>
> class basic_fstream : public std::basic_iostream<CharT, Traits>
The class template `basic_fstream` implements high-level input/output operations on file based streams. It interfaces a file-based streambuffer (`std::basic_filebuf`) with the high-level interface of (`std::basic_iostream`).
A typical implementation of `std::basic_fstream` holds only one non-derived data member: an instance of `std::basic_filebuf<CharT, Traits>`.

## Member functions


| cpp/io/basic_fstream/dsc constructor|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc destructor|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc rdbuf|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc native_handle | (see dedicated page) |

#### File operations

| cpp/io/basic_fstream/dsc is_open|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc open|basic_fstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc close|basic_fstream | (see dedicated page) |


## Non-member functions


| cpp/io/basic_fstream/dsc swap2|basic_fstream | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::string filename{"test.bin"};
    std::fstream s{filename, s.binary {{!
```

if (!s.is_open())
std::cout << "failed to open " << filename << '\n';
else
{
// write
double d{3.14};
s.write(reinterpret_cast<char*>(&d), sizeof d); // binary output
s << 123 << "abc";                              // text output
// for fstream, this moves the file position pointer (both put and get)
s.seekp(0);
// read
d = 2.71828;
s.read(reinterpret_cast<char*>(&d), sizeof d); // binary input
int n;
std::string str;
if (s >> n >> str)                             // text input
std::cout << "read back from file: " << d << ' ' << n << ' ' << str << '\n';
}
}
|output=
read back from file: 3.14 123 abc

## See also


| cpp/string/basic_string/dsc getline | (see dedicated page) |

