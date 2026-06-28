---
title: std::streamsize
type: Input/output
source: https://en.cppreference.com/w/cpp/io/streamsize
---

ddcl|header=ios|
typedef /*implementation-defined*/ streamsize;
The type `std::streamsize` is a signed integral type used to represent the number of characters transferred in an I/O operation or the size of an I/O buffer. It is used as a signed counterpart of `std::size_t`, similar to the POSIX type `ssize_t`.

## Notes

Except in the constructors of `std::strstreambuf`, negative values of `std::streamsize` are never used.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

static_assert(std::is_signed_v<std::streamsize>);

int main()
{
    std::cout << sizeof(std::streamsize) << '\n';
}
```


**Output:**
```
8
```


## See also


| cpp/io/basic_istream/dsc gcount | (see dedicated page) |
| cpp/io/basic_istream/dsc ignore | (see dedicated page) |
| cpp/io/basic_istream/dsc read | (see dedicated page) |
| cpp/io/basic_ostream/dsc write | (see dedicated page) |

