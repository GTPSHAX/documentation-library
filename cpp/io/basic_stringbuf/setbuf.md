---
title: std::basic_stringbuf::setbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/setbuf
---

ddcl|
protected:
virtual std::basic_streambuf<CharT, Traits>* setbuf( char_type* s, std::streamsize n )
If `s` is a null pointer and `n` is zero, this function has no effect.
Otherwise, the effect is implementation-defined: some implementations do nothing, while some implementations clear the `std::string` member currently used as the buffer and begin using the user-supplied character array of size `n`, whose first element is pointed to by `s`, as the buffer and the input/output character sequence.
This function is protected virtual, it may only be called through `pubsetbuf()` or from member functions of a user-defined class derived from `std::basic_stringbuf`.

## Parameters


### Parameters

- `s` - pointer to the first CharT in the user-provided buffer or null
- `n` - the number of CharT elements in the user-provided buffer or zero

## Return value

`this`

## Notes

The deprecated stream buffer `std::strstreambuf` or the boost.IOStreams device [https://www.boost.org/doc/libs/release/libs/iostreams/doc/classes/array.html#array `boost::basic_array`] may be used to implement I/O buffering over a user-provided char array in portable manner.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream ss;
    char c[1024] = {};
    ss.rdbuf()->pubsetbuf(c, 1024);
    ss << 3.14 << '\n';
    std::cout << c << '\n';
}
```


**Output:**
```
3.14 (on GNU g++/libstdc++ and SunPro C++/roguewave)
<nothing> (on MS Visual Studio 2010, SunPro C++/stlport4, CLang++/libc++)
```


## See also


| cpp/io/basic_streambuf/dsc pubsetbuf | (see dedicated page) |

