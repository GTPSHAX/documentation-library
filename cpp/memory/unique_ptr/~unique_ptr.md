---
title: std::unique_ptr::~unique_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/~unique_ptr
---

ddcl|since=c++11|notes=|
~unique_ptr();
If `get()` `1= == ` `nullptr` there are no effects. Otherwise, the owned object is destroyed via `get_deleter()``(``get()``)`.
Requires that `get_deleter()(get())` does not throw exceptions.

## Notes

Although `std::unique_ptr<T>` with the default deleter may be constructed with incomplete type `T`, the type `T` must be complete at the point of code where the destructor is called.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main () 
{
    auto deleter = [](int* ptr)
    {
        std::cout << "[deleter called]\n";
        delete ptr;
    };

    std::unique_ptr<int, decltype(deleter)> uniq(new int, deleter);
    std::cout << (uniq ? "not empty\n" : "empty\n");
    uniq.reset();
    std::cout << (uniq ? "not empty\n" : "empty\n");
}
```


**Output:**
```
not empty
[deleter called]
empty
```

