---
title: std::thread::~thread
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/~thread
---

ddcl|since=c++11|
~thread();
Destroys the thread object.
If `*this` has an associated thread (`1=joinable() == true`), `std::terminate()` is called.

## Notes

A thread object does not have an associated thread (and is safe to destroy) after
* it was default-constructed.
* it was moved from.
* `join()` has been called.
* `detach()` has been called.

## Example


### Example

```cpp
#include <thread>
using namespace std::chrono_literals;

int main()
{
    auto bleah = std::thread{[]{ std::this_thread::sleep_for(13ms); }<!---->};

}   // ~thread calls std::terminate()
```


**Output:**
```
terminate called without an active exception
```


## See also


| cpp/thread/jthread/dsc destructor | (see dedicated page) |

