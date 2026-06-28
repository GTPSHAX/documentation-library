---
title: deduction guides for std::weak_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/deduction_guides
---


# deduction guides for tt|std::weak_ptr


```cpp
**Header:** `<`memory`>`
dcl|since=c++17|
template< class T >
weak_ptr( std::shared_ptr<T> ) -> weak_ptr<T>;
```

One deduction guide is provided for `std::weak_ptr` to account for the edge case missed by the implicit deduction guides.

## Example


### Example

```cpp
#include <memory>

int main()
{
    auto p = std::make_shared<int>(42);
    std::weak_ptr w{p}; // explicit deduction guide is used in this case
}
```

