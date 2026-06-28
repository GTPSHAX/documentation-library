---
title: std::unique_lock::swap
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/swap
---

ddcl|since=c++11|
void swap( unique_lock& other ) noexcept;
Exchanges the internal states of the lock objects.

## Parameters


### Parameters

- `other` - the lock to swap the state with

## Return value

(none)

## Example


### Example

```cpp
#include <iostream>
#include <mutex>

int main()
{
    std::mutex mtx1;
    std::unique_lock<std::mutex> guard1(mtx1);
    std::unique_lock<std::mutex> guard2;
    guard2.swap(guard1);

    if (!guard1 && guard2)
        std::cout << "swapped success\n";

    return 0;
}
```


**Output:**
```
swapped success
```


## See also


| cpp/thread/unique_lock/dsc swap2 | (see dedicated page) |

