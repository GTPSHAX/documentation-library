---
title: std::basic_istream::read
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/read
---

ddcl|
basic_istream& read( char_type* s, std::streamsize count );
Extracts characters from stream.
Behaves as *UnformattedInputFunction*. After constructing and checking the sentry object, extracts characters and stores them into successive locations of the character array whose first element is pointed to by `s`. Characters are extracted and stored until any of the following conditions occurs:
* `count` characters were extracted and stored.
* end of file condition occurs on the input sequence (in which case, `setstate(failbit is called). The number of successfully extracted characters can be queried using .

## Parameters


### Parameters

- `s` - pointer to the character array to store the characters to
- `count` - number of characters to read

## Return value

`*this`

## Exceptions


## Notes

When using a non-converting locale (the default locale is non-converting), the overrider of this function in `std::basic_ifstream` may be optimized for zero-copy bulk I/O (by means of overriding `std::streambuf::xsgetn`).

## Example


### Example

```cpp
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    // read() is often used for binary I/O
    std::string bin = {'\x12', '\x12', '\x12', '\x12'};
    std::istringstream raw(bin);
    std::uint32_t n;
    if (raw.read(reinterpret_cast<char*>(&n), sizeof n))
        std::cout << std::hex << std::showbase << n << '\n';

    // prepare file for next snippet
    std::ofstream("test.txt", std::ios::binary) << "abcd1\nabcd2\nabcd3";

    // read entire file into string
    if (std::ifstream is{"test.txt", std::ios::binary {{!
```

{
auto size = is.tellg();
std::string str(size, '\0'); // construct string to stream size
is.seekg(0);
if (is.read(&str[0], size))
std::cout << str << '\n';
}
}
|output=
0x12121212
abcd1
abcd2
abcd3

## See also


| cpp/io/basic_ostream/dsc write | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |
| cpp/io/basic_istream/dsc readsome | (see dedicated page) |
| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc getline | (see dedicated page) |
| cpp/io/c/dsc fread | (see dedicated page) |

