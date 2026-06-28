---
title: std::bad_weak_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/bad_weak_ptr
---

ddcl|header=memory|since=c++11|
class bad_weak_ptr;
`std::bad_weak_ptr` is the type of the object thrown as exceptions by the constructors of `std::shared_ptr` that take `std::weak_ptr` as the argument, when the `std::weak_ptr` refers to an already deleted object.

## Member functions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main()
{
    std::shared_ptr<int> p1(new int(42));
    std::weak_ptr<int> wp(p1);
    p1.reset();
    try
    {
        std::shared_ptr<int> p2(wp);
    }
    catch (const std::bad_weak_ptr& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
std::bad_weak_ptr
```


## Defect reports


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |
| cpp/memory/dsc weak_ptr | (see dedicated page) |

