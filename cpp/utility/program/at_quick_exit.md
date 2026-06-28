---
title: std::at_quick_exit
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/at_quick_exit
---


```cpp
**Header:** `<`cstdlib`>`
dcl|num=1|since=c++11|
int at_quick_exit( /*atexit-handler*/* func ) noexcept;
int at_quick_exit( /*c-atexit-handler*/* func ) noexcept;
|1=
extern "C++" using /*atexit-handler*/ = void();
extern "C" using /*c-atexit-handler*/ = void();
```

Registers the function pointed to by `func` to be called on quick program termination (via `std::quick_exit`).
Calling the function from several threads does not induce a data race. The implementation is guaranteed to support the registration of at least 32 functions. The exact limit is implementation-defined.
The registered functions will not be called on `normal program termination`. If a function need to be called in that case, `std::atexit` must be used.

## Parameters


### Parameters

- `func` - pointer to a function to be called on quick program termination

## Return value

`0` if the registration succeeds, nonzero value otherwise.

## Notes

The two overloads are distinct because the types of the parameter `func` are distinct (language linkage is part of its type).

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

void f1()
{
    std::cout << "pushed first" << std::endl; // flush is intentional
}

extern "C" void f2()
{
    std::cout << "pushed second\n";
}

int main()
{
    auto f3 = []
    {
        std::cout << "pushed third\n";
    };

    std::at_quick_exit(f1);
    std::at_quick_exit(f2);
    std::at_quick_exit(f3);
    std::quick_exit(0);
}
```


**Output:**
```
pushed third
pushed second
pushed first
```


## See also


| cpp/utility/program/dsc abort | (see dedicated page) |
| cpp/utility/program/dsc exit | (see dedicated page) |
| cpp/utility/program/dsc atexit | (see dedicated page) |
| cpp/utility/program/dsc quick_exit | (see dedicated page) |

