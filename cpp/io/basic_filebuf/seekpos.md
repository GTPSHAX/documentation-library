---
title: std::basic_filebuf::seekpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/seekpos
---

ddcl|1=
protected:
virtual pos_type seekpos( pos_type sp,
std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );
Repositions the file pointer, if possible, to the position indicated by `sp`. If the associated file is not open (`1=is_open() == false`), fails immediately.
Reposition performs as follows:
1. If the file is open for writing, writes the put area and any unshift sequences required by the currently imbued locale, using `overflow()`.
2. Repositions the file pointer, as if by calling `std::fsetpos()`.
3. If the file is open for reading, updates the get area if necessary.
If `sp` was not obtained by calling `seekoff()` or `seekpos()` on the same file, the behavior is undefined.

## Parameters


### Parameters

- `sp` - file position obtained by `seekoff()` or `seekpos()` called earlier on the same file
- `which` - defines which of the input and/or output sequences to affect. It can be one or a combination of the following constants:

## Return value

`sp` on success or `pos_type(off_type(-1))` on failure.

## Notes

`seekpos()` is called by `std::basic_streambuf::pubseekpos()`, which is called by the single-argument versions of `std::basic_istream::seekg()` and `std::basic_ostream::seekp()`.
Many implementations do not update the get area in `seekpos()`, delegating to `underflow()` that is called by the next `sgetc()`.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

struct mybuf : std::filebuf
{
    pos_type seekpos(pos_type sp, std::ios_base::openmode which)
    {
        std::cout << "Before seekpos(" << sp << "), size of the get area is "
                  << egptr() - eback() << " with "
                  << egptr() - gptr() << " read positions available.\n";

        pos_type rc = std::filebuf::seekpos(sp, which);

        std::cout << "seekpos() returns " << rc << ".\nAfter the call, "
                  << "size of the get area is "
                  << egptr() - eback() << " with "
                  << egptr() - gptr() << " read positions available.\n";
// uncomment if get area is emptied by seekpos()
//        std::filebuf::underflow();
//        std::cout << "after forced underflow(), size of the get area is "
//                  << egptr() - eback() << " with "
//                  << egptr() - gptr() << " read positions available.\n";

        return rc;
    }
};

int main()
{
    mybuf buf;
    buf.open("test.txt", std::ios_base::in);
    std::istream stream(&buf);
    stream.get(); // read one char to force underflow()
    stream.seekg(2);
}
```


**Output:**
```
Before seekpos(2), size of the get area is 110 with 109 read positions available.
seekpos() returns 2.
After the call, size of the get area is 110 with 108 read positions available.
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-171 | C++98 | the sequence of the operations of reposition was not clear | made clear |


## See also


| cpp/io/basic_streambuf/dsc pubseekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/c/dsc fseek | (see dedicated page) |

