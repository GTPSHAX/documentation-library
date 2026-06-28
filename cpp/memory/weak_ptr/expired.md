---
title: std::weak_ptr::expired
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/expired
---

ddcla|since=c++11|constexpr=c++26|
bool expired() const noexcept;
Checks if the managed object has already been deleted. The destructor for the managed object may not yet have been called, but this object's destruction is imminent (or may have already happened).

## Return value

`1=use_count() == 0`

## Notes

If the managed object is shared among threads, it is only meaningful when `expired()` returns true.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

std::weak_ptr<int> gw;

void f()
{
    if (!gw.expired())
	    std::cout << "gw is valid\n";
    else
        std::cout << "gw is expired\n";
}

int main()
{
    {
        auto sp = std::make_shared<int>(42);
	    gw = sp;
        f();
    }

    f();
}
```


**Output:**
```
gw is valid
gw is expired
```


## See also


| cpp/memory/weak_ptr/dsc lock | (see dedicated page) |
| cpp/memory/weak_ptr/dsc use_count | (see dedicated page) |

