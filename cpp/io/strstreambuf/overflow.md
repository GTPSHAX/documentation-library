---
title: std::strstreambuf::overflow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/overflow
---

ddcl|deprecated=c++98|removed=c++26|1=
protected:
virtual int_type overflow( int_type c = EOF );
Appends the character `c` to the put area of the buffer, reallocating if possible.
1. If `1=c == EOF`, does nothing.
2. Otherwise, if the put area has a write position available (`pptr() < epptr()`), stores the character as if by `1=*pptr()++ = c`.
3. Otherwise, if the stream buffer mode is not dynamic or the stream buffer is currently frozen, the function fails and returns `EOF`.
4. Otherwise, the function reallocates (or initially allocates) a dynamic array large enough to hold the contents of the current dynamic array (if any) plus at least one additional write position. If a pointer to the allocating function `palloc` was used in the constructor, that function is called with `(*palloc)(n)` where `n` is the number of bytes to allocate, otherwise `new char[n]` is used. If a pointer to the deallocating function `pfree` was used in the constructor, that function is called with `(*pfree)(p)` to deallocate the previous array, if needed, otherwise `delete[] p` is used. If allocation fails, the function fails and returns `EOF`.

## Parameters


### Parameters

- `c` - the character to store in the put area

## Return value

If `1=c == EOF`, returns some value other than `EOF`. Otherwise, returns `(unsigned char)(c)` on success, `EOF` on failure.

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

struct mybuf : std::strstreambuf
{
    int_type overflow(int_type c) 
    {
        std::cout << "Before overflow(): size of the put area is " << epptr()-pbase()
                  << " with " << epptr()-pptr() << " write positions available\n";
        int_type rc = std::strstreambuf::overflow(c);
        std::cout << "After overflow(): size of the put area is " << epptr()-pbase()
                  << " with " << epptr()-pptr() << " write positions available\n";
        return rc;
    }
};

int main()
{
    mybuf sbuf; // read-write dynamic strstreambuf
    std::iostream stream(&sbuf);

    stream << "Sufficiently long string to overflow the initial allocation, at least "
           << " on some systems.";
}
```


**Output:**
```
Before overflow(): size of the put area is 16 with 0 write positions available
After overflow(): size of the put area is 32 with 15 write positions available
Before overflow(): size of the put area is 32 with 0 write positions available
After overflow(): size of the put area is 64 with 31 write positions available
Before overflow(): size of the put area is 64 with 0 write positions available
After overflow(): size of the put area is 128 with 63 write positions available
```


## See also


| cpp/io/basic_streambuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_filebuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sputc | (see dedicated page) |
| cpp/io/basic_ostream/dsc put | (see dedicated page) |

