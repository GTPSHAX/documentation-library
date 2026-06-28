---
title: std::unique_ptr::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/operator_bool
---

ddcl|since=c++11|notes=|1=
explicit operator bool() const noexcept;
Checks whether `*this` owns an object, i.e. whether `get()` `1= !=` `nullptr`.

## Parameters

(none)

## Return value

`true` if `*this` owns an object, `false` otherwise.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main()
{
    std::unique_ptr<int> ptr(new int(42));

    if (ptr)
        std::cout << "before reset, ptr is: " << *ptr << '\n';
    ptr.reset();
    (ptr ? (std::cout << "after reset, ptr is: " << *ptr)
        : (std::cout << "after reset ptr is empty")) << '\n';
}
```


**Output:**
```
before reset, ptr is: 42
after reset ptr is empty
```


## See also


| cpp/memory/unique_ptr/dsc get | (see dedicated page) |

