---
title: std::strstreambuf::seekpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/seekpos
---

ddcl|deprecated=c++98|removed=c++26|1=
protected:
virtual pos_type seekpos( pos_type sp,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out );
Repositions `std::basic_streambuf::gptr` and/or `std::basic_streambuf::pptr`, if possible, to the position indicated by `sp`.
If `std::ios_base::in` is set in `which`, attempts to reposition `gptr()` (the next pointer in the get area). If `std::ios_base::out` is set in `which`, attempts to reposition `pptr()` (the next pointer in the put area). If neither bit is set in `which`, the operation fails.
Each next pointer is repositioned as follows:
* If the next pointer is null, the operation fails.
* Otherwise, the new offset `newoff` (of type `off_type`) is determined by calling `sp.offset()`. If `newoff` is negative, out of bounds of the buffer, or invalid, the operation fails.
* Otherwise, the next pointer is assigned as if by `1=gptr() = eback() + newoff` or `1=pptr() = pbase() + newoff`.

## Parameters


### Parameters

- `sp` - stream position, such as one obtained by `seekoff()` or `seekpos()`
- `which` - defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants:

## Return value

The resultant offset converted to `pos_type` on success or `pos_type(off_type(-1))` on failure.

## Notes

`seekpos()` is called by `std::basic_streambuf::pubseekpos()`, which is called by the single-argument versions of `std::basic_istream::seekg()` and `std::basic_ostream::seekp()`.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <strstream>

struct mybuf : std::strstreambuf
{
    mybuf(const char* str) : std::strstreambuf(str, std::strlen(str)) {}

    pos_type seekpos(pos_type sp, std::ios_base::openmode which)
    {
        std::cout << "Before seekpos(" << sp << "), size of the get area is "
                  << egptr() - eback() << " with "
                  << egptr() - gptr() << " read positions available.\n";

        pos_type rc = std::strstreambuf::seekpos(sp, which);

        std::cout << "seekpos() returns " << rc << ".\nAfter the call, "
                  << "size of the get area is "
                  << egptr() - eback() << " with "
                  << egptr() - gptr() << " read positions available.\n";

        return rc;
    }
};

int main()
{
    mybuf buf("12345");
    std::iostream stream(&buf);
    stream.seekg(2);
}
```


**Output:**
```
Before seekpos(2), size of the get area is 5 with 5 read positions available.
seekpos() returns 2.
After the call, size of the get area is 5 with 3 read positions available.
```


## Defect reports


## See also


| cpp/io/strstreambuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_streambuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |

