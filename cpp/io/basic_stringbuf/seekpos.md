---
title: std::basic_stringbuf::seekpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/seekpos
---

ddcl|1=
protected:
virtual pos_type seekpos( pos_type sp,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
Repositions `std::basic_streambuf::gptr` and/or `std::basic_streambuf::pptr`, if possible, to the position indicated by `sp`.
Effectively executes `seekoff(off_type(sp), std::ios_base::beg, which)`.

## Parameters


### Parameters

- `sp` - stream position, such as one obtained by `seekoff()` or `seekpos()`
- `which` - defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants:

## Return value

`sp` on success or `pos_type(off_type(-1))` on failure.

## Notes

`seekpos()` is called by `std::basic_streambuf::pubseekpos()`, which is called by the single-argument versions of `std::basic_istream::seekg()` and `std::basic_ostream::seekp()`.

## Example


### Example

```cpp
#include <sstream>
#include <iostream>

struct mybuf : std::stringbuf
{
    mybuf(const std::string& str) : std::stringbuf(str) {}

    pos_type seekpos(pos_type sp, std::ios_base::openmode which)
    {
        std::cout << "Before seekpos(" << sp << "), size of the get area is "
                  << egptr() - eback() << " with "
                  << egptr() - gptr() << " read positions available.\n";

        pos_type rc = std::stringbuf::seekpos(sp, which);

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


| cpp/io/basic_streambuf/dsc pubseekpos | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekpos | (see dedicated page) |

