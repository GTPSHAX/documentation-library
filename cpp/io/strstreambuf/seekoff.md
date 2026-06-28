---
title: std::strstreambuf::seekoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/seekoff
---

ddcl|deprecated=c++98|removed=c++26|1=
protected:
virtual pos_type seekoff( off_type off,
ios_base::seekdir way,
ios_base::openmode which = ios_base::in | ios_base::out );
Repositions `std::basic_streambuf::gptr` and/or `std::basic_streambuf::pptr`, if possible, to the position that corresponds to exactly `off` characters from beginning, end, or current position of the get and/or put area of the buffer.
* If `which` includes `ios_base::in` and this buffer is open for reading, then repositions the read pointer `std::basic_streambuf::gptr` inside the get area as described below.
* If `which` includes `ios_base::out` and this buffer is open for writing, then repositions the write pointer `std::basic_streambuf::pptr` inside the put area as described below.
* If `which` includes both `ios_base::in` and `ios_base::out` and the buffer is open for both reading and writing, and `way` is either `ios_base::beg` or `ios_base::end`, then repositions both read and write pointers as described below.
* Otherwise, this function fails.
If the pointer (either `gptr` or `pptr` or both) is repositioned, it is done as follows:
1. If the pointer to be repositioned is a null pointer and the new offset `newoff` would be non-zero, this function fails.
2. The new pointer offset `newoff` of type `off_type` is determined
:@a@ if `1=way == ios_base::beg`, then `newoff` is zero
:@b@ if `1=way == ios_base::cur`, then `newoff` is the current position of the pointer (`gptr() - eback()` or `pptr() - pbase()`)
:@c@ if `1=way == ios_base::end`, then `newoff` is the length of the entire initialized part of the buffer (if overallocation is used, the high watermark pointer minus the beginning pointer)
3. If `newoff + off` is negative or out of bounds of the initialized part of the buffer, the function fails
4. Otherwise, the pointer is assigned as if by `1=gptr() = eback() + newoff + off` or `1=pptr() = pbase() + newoff + off`

## Parameters


### Parameters

- `off` - relative position to set the next pointer(s) to
- `way` - defines base position to apply the relative offset to. It can be one of the following constants:
- `which` - defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants:

## Return value

`pos_type(newoff)` on success, `pos_type(off_type(-1))` on failure and if pos_type cannot represent the resulting stream position.

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    char a[] = "123";
    std::strstream ss(a, sizeof a); // in/out
    std::cout << "put pos = " << ss.tellp()
              << " get pos = " << ss.tellg() << '\n';

    // absolute positioning both pointers
    ss.rdbuf()->pubseekoff(1, std::ios_base::beg); // move both forward
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
    std::cout << "Wrote 'a' at put position, the buffer is now: '";
    std::cout.write(a, sizeof a);
    std::cout << "'\n";

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
Wrote 'a' at put position, the buffer is now: '12a'
reading at get position gives '2'
```


## Defect reports


## See also


| cpp/io/strstreambuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_streambuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |

