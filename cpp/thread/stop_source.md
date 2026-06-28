---
title: std::stop_source
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source
---

ddcl|header=stop_token|since=c++20|
class stop_source;
The `stop_source` class provides the means to issue a stop request, such as for `std::jthread` cancellation. A stop request made for one `stop_source` object is visible to all `stop_source`s and `std::stop_token`s of the same associated stop-state; any `std::stop_callback`(s) registered for associated `std::stop_token`(s) will be invoked, and any `std::condition_variable_any` objects waiting on associated `std::stop_token`(s) will be awoken.
Once a stop is requested, it cannot be withdrawn. Additional stop requests have no effect.

## Member functions


| cpp/thread/stop_source/dsc constructor | (see dedicated page) |
| cpp/thread/stop_source/dsc destructor | (see dedicated page) |
| 1=cpp/thread/stop_source/dsc operator= | (see dedicated page) |

#### Modifiers

| cpp/thread/stop_source/dsc request_stop | (see dedicated page) |
| cpp/thread/stop_source/dsc swap | (see dedicated page) |

#### Observers

| cpp/thread/stop_source/dsc get_token | (see dedicated page) |
| cpp/thread/stop_source/dsc stop_requested | (see dedicated page) |
| cpp/thread/stop_source/dsc stop_possible | (see dedicated page) |


## Non-member functions


| cpp/thread/stop_source/dsc operator_cmp | (see dedicated page) |
| cpp/thread/stop_source/dsc swap2 | (see dedicated page) |


## Helper tags


| cpp/thread/stop_source/dsc nostopstate | (see dedicated page) |


## Notes

For the purposes of `std::jthread` cancellation the `stop_source` object should be retrieved from the `std::jthread` object using ; or stop should be requested directly from the `std::jthread` object using . This will then use the same associated stop-state as that passed into the `std::jthread`'s invoked function argument (i.e., the function being executed on its thread).
For other uses, however, a `stop_source` can be constructed separately using the default constructor, which creates new stop-state.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <stop_token>
#include <thread>

using namespace std::chrono_literals;

void worker_fun(int id, std::stop_token stoken)
{ 
    for (int i = 10; i; --i)
    {
        std::this_thread::sleep_for(300ms);
        if (stoken.stop_requested())
        {
            std::printf("  worker%d is requested to stop\n", id);
            return;
        }
        std::printf("  worker%d goes back to sleep\n", id);
    }
}

int main()
{
    std::jthread threads[4];
    std::cout << std::boolalpha;
    auto print = [](const std::stop_source& source)
    {
        std::printf("stop_source stop_possible = %s, stop_requested = %s\n",
                    source.stop_possible() ? "true" : "false",
                    source.stop_requested() ? "true" : "false");
    };

    // Common source
    std::stop_source stop_source;

    print(stop_source);

    // Create worker threads
    for (int i = 0; i < 4; ++i)
        threads[i] = std::jthread(worker_fun, i + 1, stop_source.get_token());

    std::this_thread::sleep_for(500ms);

    std::puts("Request stop");
    stop_source.request_stop();

    print(stop_source);

    // Note: destructor of jthreads will call join so no need for explicit calls
}
```


**Output:**
```
stop_source stop_possible = true, stop_requested = false
  worker2 goes back to sleep
  worker3 goes back to sleep
  worker1 goes back to sleep
  worker4 goes back to sleep
Request stop
stop_source stop_possible = true, stop_requested = true
  worker3 is requested to stop
  worker1 is requested to stop
  worker2 is requested to stop
  worker4 is requested to stop
```

