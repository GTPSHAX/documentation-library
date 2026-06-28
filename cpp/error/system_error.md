---
title: std::system_error
type: Utilities
source: https://en.cppreference.com/w/cpp/error/system_error
---

ddcl|header=system_error|since=c++11|
class system_error;
`std::system_error` is the type of the exception thrown by various library functions (typically the functions that interface with the OS facilities, e.g. the constructor of `std::thread`) when the exception has an associated `std::error_code`, which may be reported.

## Member functions


| cpp/error/system_error/dsc constructor | (see dedicated page) |
| cpp/error/system_error/dsc operator{{= | (see dedicated page) |
| cpp/error/system_error/dsc code | (see dedicated page) |
| cpp/error/system_error/dsc what | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <system_error>
#include <thread>

int main()
{
    try
    {
        std::thread().detach(); // attempt to detach a non-thread
    }
    catch(const std::system_error& e)
    {
        std::cout << "Caught system_error with code "
                     "[" << e.code() << "] meaning "
                     "[" << e.what() << "]\n";
    }
}
```


**Output:**
```
Caught system_error with code [generic:22] meaning [Invalid argument]
```

