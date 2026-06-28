---
title: std::strstreambuf::pcount
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/pcount
---

ddcl|deprecated=c++98|removed=c++26|
int pcount() const;
Returns the number of characters written to the output sequence.
If the next pointer for the put area (`std::streambuf::pptr()`) is a null pointer, returns zero.
Otherwise, returns the next pointer in the put area minus the beginning pointer in the put area, that is `pptr() - pbase()`.

## Parameters

(none)

## Return value

The number of characters written to the put area.

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    std::strstream dyn; // dynamically-allocated output buffer
    dyn << "Test: " << 1.23 << std::ends;
    std::strstreambuf* buf = dyn.rdbuf();
    std::cout << "The size of the output is "
              << buf->pcount() // or just buf.pcount()
              << " and it holds \"" << dyn.str() << "\"\n";
    dyn.freeze(false); // after calling .str() on a dynamic strstream

    char arr[10];
    std::ostrstream user(arr, 10); // user-provided output buffer
    buf = user.rdbuf();
    user << 1.23; // note: no std::ends
    std::cout.write(arr, buf->pcount()); // or just user.pcount()
    std::cout << '\n';

    std::istrstream lit("1 2 3"); // read-only fixed-size buffer
    buf = lit.rdbuf();
    // istrstream has no member pcount(), so lit.pcount() won't work
    std::cout << "Input-only pcount() = " << buf->pcount() << '\n';
}
```


**Output:**
```
The size of the output is 11 and it holds "Test: 1.23"
1.23
Input-only pcount() = 0
```


## See also


| cpp/io/strstream/dsc pcount|strstream | (see dedicated page) |
| cpp/io/strstream/dsc pcount|ostrstream | (see dedicated page) |

