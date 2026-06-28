---
title: std::get_pointer_safety
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/gc/get_pointer_safety
---

ddcl|header=memory|since=c++11|removed=c++23|
std::pointer_safety get_pointer_safety() noexcept;
Obtains the implementation-defined pointer safety model, which is a value of type `std::pointer_safety`.

## Parameters

(none)

## Return value

The pointer safety used by this implementation.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main()
{
    std::cout << "Pointer safety: ";
    switch (std::get_pointer_safety())
    {
        case std::pointer_safety::strict:
            std::cout << "strict\n";
            break;
        case std::pointer_safety::preferred:
            std::cout << "preferred\n";
            break;
        case std::pointer_safety::relaxed:
            std::cout << "relaxed\n";
            break;
    }
}
```


**Output:**
```
Pointer safety: relaxed
```


## See also


| cpp/memory/gc/dsc pointer_safety | (see dedicated page) |

