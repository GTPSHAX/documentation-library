---
title: std::basic_osyncstream::get_wrapped
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream/get_wrapped
---


```cpp
dcl|1=
streambuf_type* get_wrapped() const noexcept;
```

Returns a pointer to the wrapped `std::basic_streambuf`, obtained by calling `cpp/io/basic_syncbuf/get_wrapped|get_wrapped()` on the underlying `std::basic_syncbuf`.

## Parameters

(none)

## Example


### Example

```cpp
#include <iostream>
#include <syncstream>

int main()
{
    std::osyncstream bout1(std::cout);
    bout1 << "Hello, ";
    {
        std::osyncstream(bout1.get_wrapped()) << "Goodbye, " << "Planet!" << '\n';
    } // emits the contents of the temporary buffer
    bout1 << "World!" << '\n';
} // emits the contents of bout1
```


**Output:**
```
Goodbye, Planet!
Hello, World!
```


## See also


| cpp/io/basic_osyncstream/dsc destructor | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc get_wrapped | (see dedicated page) |

