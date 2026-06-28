---
title: std::bad_alloc
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/bad_alloc
---

ddcl|header=new|
class bad_alloc;
`std::bad_alloc` is the type of the object thrown as exceptions by the `allocation functions` to report failure to allocate storage.

## Member functions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <new>

int main()
{
    try
    {
        while (true)
        {
            new int[100000000ul];
        }
    }
    catch (const std::bad_alloc& e)
    {
        std::cout << "Allocation failed: " << e.what() << '\n';
    }
}
```


**Output:**
```
Allocation failed: std::bad_alloc
```


## See also


| cpp/memory/new/dsc operator_new | (see dedicated page) |

