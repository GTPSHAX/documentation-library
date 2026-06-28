---
title: std::strstreambuf::setbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/setbuf
---

ddcl|deprecated=c++98|removed=c++26|1=
protected:
virtual streambuf* setbuf( char* s, std::streamsize n );
If `s` is a null pointer and `n` is zero, this function has no effect.
Otherwise, the effect is implementation-defined: some implementations do nothing, while some implementations deallocate the dynamic member array used as the buffer and begin using the user-supplied character array of size `n`, whose first element is pointed to by `s`.
This function is protected virtual, it may only be called through `pubsetbuf()` or from member functions of a user-defined class derived from `std::strstreambuf`.

## Parameters


### Parameters

- `s` - pointer to the first byte in the user-provided buffer
- `n` - the number of bytes in the user-provided buffer

## Return value

`this`

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    char a[100] = {};
    std::strstream str;
    str.rdbuf()->pubsetbuf(a, sizeof a);
    str << "Test string" << std::ends;
    std::cout << "user-provided buffer holds \"" << a << "\"\n";
}
```


**Output:**
```
user-provided buffer holds "Test string"
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubsetbuf | (see dedicated page) |
| cpp/io/basic_streambuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc setbuf | (see dedicated page) |

