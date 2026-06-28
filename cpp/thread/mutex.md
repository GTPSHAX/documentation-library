---
title: std::mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/mutex
---

ddcl|header=mutex|since=c++11|
class mutex;
The `mutex` class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads.
`mutex` offers exclusive, non-recursive ownership semantics:
* A calling thread ''owns'' a `mutex` from the time that it successfully calls either  or  until it calls .
* When a thread owns a `mutex`, all other threads will block (for calls to ) or receive a `false` return value (for ) if they attempt to claim ownership of the `mutex`.
* A calling thread must not own the `mutex` prior to calling  or .
The behavior of a program is undefined if a `mutex` is destroyed while still owned by any threads, or a thread terminates while owning a `mutex`. The `mutex` class satisfies all requirements of *Mutex* and *StandardLayoutType*.
`std::mutex` is neither copyable nor movable.

## Nested types


| Item | Description |
|------|-------------|
| **Name** | Definition |
| cpp/thread/dsc native_handle_type|mutex | (see dedicated page) |


## Member functions


| cpp/thread/mutex/dsc constructor|mutex | (see dedicated page) |
| cpp/thread/mutex/dsc destructor|mutex | (see dedicated page) |
| cpp/thread/mutex/dsc operator{{= | (see dedicated page) |

#### Locking

| cpp/thread/mutex/dsc lock|mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock|mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock|mutex | (see dedicated page) |

#### Native handle

| cpp/thread/mutex/dsc native_handle|mutex | (see dedicated page) |


## Notes

`std::mutex` is usually not accessed directly: `std::unique_lock`, `std::lock_guard`, <sup>(since C++17)</sup> or `std::scoped_lock` manage locking in a more exception-safe manner.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <map>
#include <mutex>
#include <string>
#include <thread>

std::map<std::string, std::string> g_pages;
std::mutex g_pages_mutex;

void save_page(const std::string& url)
{
    // simulate a long page fetch
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::string result = "fake content";

    std::lock_guard<std::mutex> guard(g_pages_mutex);
    g_pages[url] = result;
}

int main() 
{
    std::thread t1(save_page, "http://foo");
    std::thread t2(save_page, "http://bar");
    t1.join();
    t2.join();

    // safe to access g_pages without lock now, as the threads are joined
    for (const auto& [url, page] : g_pages)
        std::cout << url << " => " << page << '\n';
}
```


**Output:**
```
http://bar => fake content
http://foo => fake content
```


## See also


| cpp/thread/dsc recursive_mutex | (see dedicated page) |
| cpp/thread/dsc lock_guard | (see dedicated page) |
| cpp/thread/dsc unique_lock | (see dedicated page) |
| cpp/thread/dsc scoped_lock | (see dedicated page) |
| cpp/thread/dsc condition_variable | (see dedicated page) |

