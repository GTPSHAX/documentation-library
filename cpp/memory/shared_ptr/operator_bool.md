---
title: std::shared_ptr::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/operator_bool
---

ddcla|constexpr=c++26|
explicit operator bool() const noexcept;
Checks if `*this` stores a non-null pointer.

## Return value

`1=get() != nullptr`

## Notes

An empty shared_ptr (where `1=use_count() == 0`) may store a non-null pointer accessible by `get()`, e.g. if it were created using the aliasing constructor.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

void report(std::shared_ptr<int> ptr) 
{
    if (ptr)
        std::cout << "*ptr = " << *ptr << "\n";
    else
        std::cout << "ptr is not a valid pointer.\n";
}

int main()
{
    std::shared_ptr<int> ptr;
    report(ptr);

    ptr = std::make_shared<int>(7);
    report(ptr);
}
```


**Output:**
```
ptr is not a valid pointer.
*ptr=7
```


## See also


| cpp/memory/shared_ptr/dsc get | (see dedicated page) |

