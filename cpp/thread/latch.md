---
title: std::latch
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/latch
---

ddcl|header=latch|since=c++20|
class latch;
The `latch` class is a downward counter of type `std::ptrdiff_t` which can be used to synchronize threads. The value of the counter is initialized on creation. Threads may block on the latch until the counter is decremented to zero. There is no possibility to increase or reset the counter, which makes the latch a single-use barrier.
Concurrent invocations of the member functions of `std::latch`, except for the destructor, do not introduce data races.

## Data Members


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Member functions


| cpp/thread/latch/dsc constructor | (see dedicated page) |
| cpp/thread/latch/dsc destructor | (see dedicated page) |
| cpp/thread/latch/dsc count_down | (see dedicated page) |
| cpp/thread/latch/dsc try_wait | (see dedicated page) |
| cpp/thread/latch/dsc wait | (see dedicated page) |
| cpp/thread/latch/dsc arrive_and_wait | (see dedicated page) |

#### Constants

| cpp/thread/latch/dsc max | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <latch>
#include <string>
#include <thread>

struct Job
{
    const std::string name;
    std::string product{"not worked"};
    std::thread action{};
};

int main()
{
    Job jobs[]{<!---->{"Annika"}, {"Buru"}, {"Chuck"}<!---->};

    std::latch work_done{std::size(jobs)};
    std::latch start_clean_up{1};

    auto work = [&](Job& my_job)
    {
        my_job.product = my_job.name + " worked";
        work_done.count_down();
        start_clean_up.wait();
        my_job.product = my_job.name + " cleaned";
    };

    std::cout << "Work is starting... ";
    for (auto& job : jobs)
        job.action = std::thread{work, std::ref(job)};

    work_done.wait();
    std::cout << "done:\n";
    for (auto const& job : jobs)
        std::cout << "  " << job.product << '\n';

    std::cout << "Workers are cleaning up... ";
    start_clean_up.count_down();
    for (auto& job : jobs)
        job.action.join();

    std::cout << "done:\n";
    for (auto const& job : jobs)
        std::cout << "  " << job.product << '\n';
}
```


**Output:**
```
Work is starting... done:
  Annika worked
  Buru worked
  Chuck worked
Workers are cleaning up... done:
  Annika cleaned
  Buru cleaned
  Chuck cleaned
```


## See also


| cpp/thread/dsc barrier | (see dedicated page) |

