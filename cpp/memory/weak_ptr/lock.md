---
title: std::weak_ptr::lock
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/lock
---

ddcla|since=c++11|constexpr=c++26|
std::shared_ptr<T> lock() const noexcept;
Creates a new `std::shared_ptr` that shares ownership of the managed object. If there is no managed object, i.e. `*this` is empty, then the returned `shared_ptr` also is empty.

## Return value

`expired() ? shared_ptr<T>() : shared_ptr<T>(*this)` (executed atomically)

## Notes

Both this function and the constructor of `std::shared_ptr` may be used to acquire temporary ownership of the managed object referred to by a `std::weak_ptr`. The difference is that the constructor of `std::shared_ptr` throws an exception when its `std::weak_ptr` argument is empty, while `std::weak_ptr<T>::lock()` constructs an empty `std::shared_ptr<T>`.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

void observe(std::weak_ptr<int> weak)
{
    if (auto p = weak.lock())
        std::cout << "\tobserve() is able to lock weak_ptr<>, value=" << *p << '\n';
    else
        std::cout << "\tobserve() is unable to lock weak_ptr<>\n";
}

int main()
{
    std::weak_ptr<int> weak;
    std::cout << "weak_ptr<> is not yet initialized\n";
    observe(weak);

    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
        std::cout << "weak_ptr<> is initialized with shared_ptr\n";
        observe(weak);
    }

    std::cout << "shared_ptr<> has been destructed due to scope exit\n";
    observe(weak);
}
```


**Output:**
```
weak_ptr<> is not yet initialized
        observe() is unable to lock weak_ptr<>
weak_ptr<> is initialized with shared_ptr
        observe() is able to lock weak_ptr<>, value=42
shared_ptr<> has been destructed due to scope exit
        observe() is unable to lock weak_ptr<>
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2316 | C++11 | lock() was not required to be atomic, but required to be noexcept, which led to a contradiction | specified to be atomic |


## See also


| cpp/memory/weak_ptr/dsc expired | (see dedicated page) |

