---
title: std::shared_ptr::use_count
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/use_count
---

ddcla|constexpr=c++26|
long use_count() const noexcept;
Returns the number of different `shared_ptr` objects (including `*this`) managing the current object. If there is no managed object, `0` is returned.
In multithreaded environment, `use_count` retrieves the number of objects atomically (typical implementations use a memory_order_relaxed load).

## Return value

The number of `std::shared_ptr` objects managing the current object or `0` if there is no managed object.

## Notes

Common use cases include:
* Comparison with `0`. If `use_count` returns `0`, the shared pointer is ''empty'' and manages no objects (whether or not its stored pointer is `cpp/language/nullptr|nullptr`).
* Comparison with `1`. If `use_count` returns `1`, there are no other owners. <sup>(until C++20)</sup> The <sup>(since C++17)</sup> deprecated member function `unique()` is provided for this use case.
In multithreaded environment, the value returned by `use_count` should be considered approximate, as the number of shared owners might change in other threads between the atomic retrieval and meaningful use of the value. When `use_count` returns `1`, it does not imply that the object is safe to modify because accesses to the managed object by former shared owners may not have completed, and because new shared owners may be introduced concurrently, such as by `std::weak_ptr::lock`. Only when `use_count` returns `0` is the count accurate.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

void fun(std::shared_ptr<int> sp)
{
    std::cout << "in fun(): sp.use_count() == " << sp.use_count()
              << " (object @ " << sp << ")\n";
}

int main()
{
    auto sp1 = std::make_shared<int>(5);
    std::cout << "in main(): sp1.use_count() == " << sp1.use_count()
              << " (object @ " << sp1 << ")\n";

    fun(sp1);
}
```


**Output:**
```
in main(): sp1.use_count() == 1 (object @ 0x20eec30)
in fun(): sp.use_count() == 2 (object @ 0x20eec30)
```


## See also


| cpp/memory/shared_ptr/dsc unique | (see dedicated page) |

