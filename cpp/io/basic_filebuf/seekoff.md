---
title: std::basic_filebuf::seekoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/seekoff
---

ddcl|1=
protected:
virtual pos_type seekoff( off_type off,
std::ios_base::seekdir dir,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
Repositions the file pointer, if possible, to the position that corresponds to exactly `off` characters from beginning, end, or current position of the file (depending on the value of `dir`).
If the associated file is not open (`1=is_open() == false`), fails immediately.
If the multibyte character encoding is state-dependent (`cpp/locale/codecvt/encoding|codecvt::encoding()` returned `-1`) or variable-length (`codecvt::encoding()` returned `0`) and the offset `off` is not `0`, fails immediately: this function cannot determine the number of bytes that correspond to `off` characters.
If `dir` is not `std::basic_ios::cur` or the offset `off` is not `0`, and the most recent operation done on this filebuf object was output (that is, either the put buffer is not empty, or the most recently called function was `overflow()`), then calls `std::codecvt::unshift` to determine the unshift sequence necessary, and writes that sequence to the file by calling `overflow()`.
Then converts the argument `dir` to a value `whence` of type `int` as follows:


| Item | Description |
|------|-------------|
| **value of {{c** | dir |

Then, if the character encoding is fixed-width (`codecvt::encoding()` returns some positive number `width`), moves the file pointer as if by `std::fseek(file, width*off, whence)`.
Otherwise, moves the file pointer as if by `std::fseek(file, 0, whence)`.
The `openmode` argument, required by the base class function signature, is usually ignored, because `std::basic_filebuf` maintains only one file position.

## Parameters


### Parameters

- `off` - relative position to set the position indicator to
- `dir` - defines base position to apply the relative offset to. It can be one of the following constants:
- `which` - defines which of the input and/or output sequences to affect. It can be one or a combination of the following constants:

## Return value

A newly constructed object of type `pos_type` which stores the resulting file position, or `pos_type(off_type(-1))` on failure.

## Notes

`seekoff()` is called by `std::basic_streambuf::pubseekoff`, which is called by `std::basic_istream::seekg`, `std::basic_ostream::seekp`, `std::basic_istream::tellg`, and `std::basic_ostream::tellp`.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <locale>

template<typename CharT>
int get_encoding(const std::basic_istream<CharT>& stream)
{
    using Facet = std::codecvt<CharT, char, std::mbstate_t>;
    return std::use_facet<Facet>(stream.getloc()).encoding();
}

int main()
{
    // prepare a 10-byte file holding 4 characters ("zß水𝄋") in UTF-8
    std::ofstream("text.txt") << "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b";

    // open using a non-converting encoding
    std::ifstream f1("text.txt");
    std::cout << "f1's locale's encoding() returns "
              << get_encoding(f1) << '\n'
              << "pubseekoff(3, beg) returns "
              << f1.rdbuf()->pubseekoff(3, std::ios_base::beg) << '\n'
              << "pubseekoff(0, end) returns "
              << f1.rdbuf()->pubseekoff(0, std::ios_base::end) << '\n';

    // open using UTF-8
    std::wifstream f2("text.txt");
    f2.imbue(std::locale("en_US.UTF-8"));
    std::cout << "f2's locale's encoding() returns "
              << get_encoding(f2) << '\n'
              << "pubseekoff(3, beg) returns "
              << f2.rdbuf()->pubseekoff(3, std::ios_base::beg) << '\n'
              << "pubseekoff(0, end) returns "
              << f2.rdbuf()->pubseekoff(0, std::ios_base::end) << '\n';
}
```


**Output:**
```
f1's locale's encoding() returns 1
pubseekoff(3, beg) returns 3
pubseekoff(0, end) returns 10
f2's locale's encoding() returns 0
pubseekoff(3, beg) returns -1
pubseekoff(0, end) returns 10
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |
| cpp/io/c/dsc fseek | (see dedicated page) |

