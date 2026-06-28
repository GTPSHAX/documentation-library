---
title: std::stop_token
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token
---

ddcl|header=stop_token|since=c++20|
class stop_token;
The `stop_token` class provides the means to check if a stop request has been made or can be made, for its associated `cpp/thread/stop_source|std::stop_source` object. It is essentially a thread-safe "view" of the associated stop-state.
The `stop_token` can also be passed to the constructor of `cpp/thread/stop_callback|std::stop_callback`, such that the callback will be invoked if the `stop_token`'s associated `std::stop_source` is requested to stop. And `stop_token` can be passed to the interruptible waiting functions of `std::condition_variable_any`, to interrupt the condition variable's wait if stop is requested.

## Member alias templates


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/thread/stop_token/dsc constructor | (see dedicated page) |
| cpp/thread/stop_token/dsc destructor | (see dedicated page) |
| cpp/thread/stop_token/dsc operator{{= | (see dedicated page) |

#### Modifiers

| cpp/thread/stop_token/dsc swap | (see dedicated page) |

#### Observers

| cpp/thread/stop_token/dsc stop_requested | (see dedicated page) |
| cpp/thread/stop_token/dsc stop_possible | (see dedicated page) |


## Non-member functions


| cpp/thread/stop_token/dsc operator_cmp | (see dedicated page) |
| cpp/thread/stop_token/dsc swap2 | (see dedicated page) |


## Notes

A `stop_token` object is not generally constructed independently, but rather retrieved from a `std::jthread` or `std::stop_source`. This makes it share the same associated stop-state as the `std::jthread` or `std::stop_source`.

## Example


### Example

```cpp
#include <iostream>
#include <thread>

using namespace std::literals::chrono_literals;

void f(std::stop_token stop_token, int value)
{
    while (!stop_token.stop_requested())
    {
        std::cout << value++ << ' ' << std::flush;
        std::this_thread::sleep_for(200ms);
    }
    std::cout << std::endl;
}

int main()
{
    std::jthread thread(f, 5); // prints 5 6 7 8... for approximately 3 seconds
    std::this_thread::sleep_for(3s);
    // The destructor of jthread calls request_stop() and join().
}
```


**Output:**
```
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

