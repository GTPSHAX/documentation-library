---
title: std::basic_streambuf::xsputn
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/sputn
---


```cpp
dcl|num=1|1=
std::streamsize sputn( const char_type* s, std::streamsize count );
dcl|num=2|1=
protected:
virtual std::streamsize xsputn( const char_type* s, std::streamsize count );
```

1. Calls `xsputn(s, count)` of the most derived class.
2. Writes `count` characters to the output sequence from the character array whose first element is pointed to by `s`. The characters are written as if by repeated calls to `sputc()`. Writing stops when either `count` characters are written or a call to `sputc()` would have returned `Traits::eof()`.
If the put area becomes full (`1=pptr() == epptr()`), it is unspecified whether `overflow()` is actually called or its effect is achieved by other means.

## Parameters

(none)

## Return value

The number of characters successfully written.

## Notes

"achieved by other means" permits bulk I/O without intermediate buffering: that is how `std::ofstream::write()` simply passes the pointer to the suitable system call in some implementations.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream s1;
    std::streamsize sz = s1.rdbuf()->sputn("This is a test", 14);
    s1 << '\n';
    std::cout << "The call to sputn() returned " << sz << '\n'
              << "The output sequence contains " << s1.str();

    std::istringstream s2;
    sz = s2.rdbuf()->sputn("This is a test", 14);
    std::cout << "The call to sputn() on an input stream returned " << sz << '\n';
}
```


**Output:**
```
The call to sputn() returned 14
The output sequence contains This is a test
The call to sputn() on an input stream returned 0
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc sgetn | (see dedicated page) |

