---
title: std::skipws
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/skipws
---


```cpp
**Header:** `<`ios`>`
dcl|num=1|
std::ios_base& skipws( std::ios_base& str );
dcl|num=2|
std::ios_base& noskipws( std::ios_base& str );
```

Enables or disables skipping of leading whitespace by the formatted input functions (enabled by default). Has no effect on output.
1. Enables the `skipws` flag in the stream `str` as if by calling `str.setf(std::ios_base::skipws)`.
2. Disables the `skipws` flag in the stream `str` as if by calling `str.unsetf(std::ios_base::skipws)`.
The whitespace skipping is performed by the constructor of `std::basic_istream::sentry`, which reads and discards the characters classified as whitespace by the `std::ctype` facet of the stream's imbued locale.
This is an I/O manipulator, it may be called with an expression such as `out << std::noskipws` for any `out` of type `std::basic_ostream` or with an expression such as `in >> std::noskipws` for any `in` of type `std::basic_istream`.

## Parameters


### Parameters

- `str` - reference to I/O stream

## Return value

`str` (reference to the stream after manipulation).

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    char c1, c2, c3;
    std::istringstream("a b c") >> c1 >> c2 >> c3;
    std::cout << "Default  behavior:"
                 " c1 = " << c1 << 
                 " c2 = " << c2 << 
                 " c3 = " << c3 << '\n';
    std::istringstream("a b c") >> std::noskipws >> c1 >> c2 >> c3;
    std::cout << "noskipws behavior:" 
                 " c1 = " << c1 <<
                 " c2 = " << c2 <<
                 " c3 = " << c3 << '\n';
}
```


**Output:**
```
Default  behavior: c1 = a c2 = b c3 = c
noskipws behavior: c1 = a c2 =   c3 = b
```


## See also


| cpp/io/manip/dsc resetiosflags | (see dedicated page) |
| cpp/io/manip/dsc setiosflags | (see dedicated page) |
| cpp/io/manip/dsc ws | (see dedicated page) |

