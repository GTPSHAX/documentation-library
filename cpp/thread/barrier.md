---
title: std::barrier
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/barrier
---

ddcl|header=barrier|since=c++20|1=
template< class CompletionFunction = /* see below */ >
class barrier;
The class template `std::barrier` provides a thread-coordination mechanism that blocks a group of threads of known size until all threads in that group have reached the barrier. Unlike `std::latch`, barriers are reusable: once a group of arriving threads are unblocked, the barrier can be reused. Unlike `std::latch`, barriers execute a possibly empty callable before unblocking threads.
A barrier object's lifetime consists of one or more phases. Each phase defines a ''phase synchronization point'' where waiting threads block. Threads can arrive at the barrier, but defer waiting on the ''phase synchronization point'' by calling . Such threads can later block on the ''phase synchronization point'' by calling .
A barrier ''phase'' consists of the following steps:
# The ''expected count'' is decremented by each call to  or .
# When the expected count reaches zero, the ''phase completion step'' is run, meaning that the  is invoked, and all threads blocked on the phase synchronization point are unblocked. The end of the completion step  all calls that were unblocked by the completion step return.<br><!--
-->Exactly once after the expected count reaches zero, a thread executes the completion step during its call to , , or , except that it is implementation-defined whether the step executes if no thread calls .
# When the completion step finishes, the expected count is reset to the value specified at construction less the number of calls to  since, and the next ''barrier phase'' begins.
Concurrent invocations of the member functions of `barrier`, except for the destructor, do not introduce data races.

## Template parameters


### Parameters

- `CompletionFunction` - a function object type
- `CompletionFunction`
The default template argument of `CompletionFunction` is an unspecified function object type that additionally meets the requirements of *DefaultConstructible*. Calling an lvalue of it with no arguments has no effects.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions


| cpp/thread/barrier/dsc constructor | (see dedicated page) |
| cpp/thread/barrier/dsc destructor | (see dedicated page) |
| cpp/thread/barrier/dsc arrive | (see dedicated page) |
| cpp/thread/barrier/dsc wait | (see dedicated page) |
| cpp/thread/barrier/dsc arrive_and_wait | (see dedicated page) |
| cpp/thread/barrier/dsc arrive_and_drop | (see dedicated page) |

#### Constants

| cpp/thread/barrier/dsc max | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <barrier>
#include <iostream>
#include <string>
#include <syncstream>
#include <thread>
#include <vector>

int main()
{
    const auto workers = {"Anil", "Busara", "Carl"};

    auto on_completion = []() noexcept
    {
        // locking not needed here
        static auto phase =
            "... done\n"
            "Cleaning up...\n";
        std::cout << phase;
        phase = "... done\n";
    };

    std::barrier sync_point(std::ssize(workers), on_completion);

    auto work = [&](std::string name)
    {
        std::string product = "  " + name + " worked\n";
        std::osyncstream(std::cout) << product;  // ok, op<< call is atomic
        sync_point.arrive_and_wait();

        product = "  " + name + " cleaned\n";
        std::osyncstream(std::cout) << product;
        sync_point.arrive_and_wait();
    };

    std::cout << "Starting...\n";
    std::vector<std::jthread> threads;
    threads.reserve(std::size(workers));
    for (auto const& worker : workers)
        threads.emplace_back(work, worker);
}
```


**Output:**
```
Starting...
  Anil worked
  Carl worked
  Busara worked
... done
Cleaning up...
  Busara cleaned
  Carl cleaned
  Anil cleaned
... done
```


## Defect reports


## See also


| cpp/thread/dsc latch | (see dedicated page) |

