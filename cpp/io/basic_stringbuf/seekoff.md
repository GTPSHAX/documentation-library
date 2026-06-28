---
title: std::basic_stringbuf::seekoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/seekoff
---

ddcl|1=
protected:
virtual pos_type seekoff( off_type off,
std::ios_base::seekdir dir,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
Repositions `std::basic_streambuf::gptr` and/or `std::basic_streambuf::pptr`, if possible, to the position that corresponds to exactly `off` characters from beginning, end, or current position of the get and/or put area of the buffer.
* If `which` includes `std::ios_base::in` and this buffer is open for reading (that is, if `1=(which & std::ios_base::in) == std::ios_base::in`), then repositions the read pointer `std::basic_streambuf::gptr` inside the get area as described below
* If `which` includes `std::ios_base::out` and this buffer is open for writing (that is, `1=(which & std::ios_base::out) == std::ios_base::out`), then repositions the write pointer `std::basic_streambuf::pptr` inside the put area as described below
* If `which` includes both  `std::ios_base::in` and  `std::ios_base::out` and the buffer is open for both reading and writing (that is, `1=(which & (std::ios_base::in ), and `dir` is either `std::ios_base::beg` or `std::ios_base::end`, then repositions both read and write pointers as described below.
* Otherwise, this function fails.
If `cpp/io/basic_streambuf|gptr` and/or `cpp/io/basic_streambuf|pptr` is repositioned, it is done as follows:
1. The new pointer offset `newoff` of type `off_type` is determined
:@a@ if `1=dir == std::ios_base::beg`, then `newoff` is zero
:@b@ if `1=dir == std::ios_base::cur`, then `newoff` is the current position of the pointer (`gptr() - eback()` or `pptr() - pbase()`)
:@c@ if `1=dir == std::ios_base::end`, then `newoff` is the length of the entire initialized part of the buffer (if `over-allocation` is used, the high watermark pointer minus the beginning pointer)
2. If the pointer to be repositioned is a null pointer and `newoff` would be non-zero, this function fails.
3. If `newoff + off < 0` (the repositioning would move the pointer to before the beginning of the buffer) or if `newoff + off` would point past the end of the buffer (or past the last initialized character in the buffer if `over-allocation` is used), the function fails.
4. Otherwise, the pointer is assigned as if by `1=gptr() = eback() + newoff + off` or `1=pptr() = pbase() + newoff + off`.

## Parameters


### Parameters

- `off` - relative position to set the next pointer(s) to
- `dir` - defines base position to apply the relative offset to. It can be one of the following constants:
- `which` - defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants:

## Return value

`pos_type(newoff)` on success, `pos_type(off_type(-1))` on failure or if `pos_type` cannot represent the resulting stream position.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::stringstream ss("123"); // in/out
    std::cout << "put pos = " << ss.tellp()
              << " get pos = " << ss.tellg() << '\n';

    // absolute positioning both pointers
    ss.rdbuf()->pubseekoff(1, std::ios_base::beg); // move both 1 forward
    std::cout << "put pos = " << ss.tellp()
              << " get pos = " << ss.tellg() << '\n';

    // try to move both pointers 1 forward from current position
    if (-1 == ss.rdbuf()->pubseekoff(1, std::ios_base::cur))
        std::cout << "moving both pointers from current position failed\n";
    std::cout << "put pos = " << ss.tellp()
              << " get pos = " << ss.tellg() << '\n';

    // move the write pointer 1 forward, but not the read pointer
    // can also be called as ss.seekp(1, std::ios_base::cur);
    ss.rdbuf()->pubseekoff(1, std::ios_base::cur, std::ios_base::out);
    std::cout << "put pos = " << ss.tellp()
              << " get pos = " << ss.tellg() << '\n';

    ss << 'a'; // write at put position
    std::cout << "Wrote 'a' at put position, the buffer is now " << ss.str() << '\n';

    char ch;
    ss >> ch;
    std::cout << "reading at get position gives '" << ch << "'\n";
}
```


**Output:**
```
put pos = 0 get pos = 0
put pos = 1 get pos = 1
moving both pointers from current position failed
put pos = 1 get pos = 1
put pos = 2 get pos = 1
Wrote 'a' at put position, the buffer is now 12a
reading at get position gives '2'
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekoff | (see dedicated page) |

