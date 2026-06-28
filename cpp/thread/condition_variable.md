---
title: std::condition_variable
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable
---

ddcl|header=condition_variable|since=c++11|1=
class condition_variable;
`std::condition_variable` is a synchronization primitive used with a `std::mutex` to block one or more threads until another thread both modifies a shared variable (the ''condition'') and notifies the `std::condition_variable`.
The thread that intends to modify the shared variable must:
# Acquire a `std::mutex` (typically via `std::lock_guard`).
# Modify the shared variable while the lock is owned.
# Call `notify_one` or `notify_all` on the `std::condition_variable` (can be done after releasing the lock).
Even if the shared variable is atomic, it must be modified while owning the mutex to [https://stackoverflow.com/questions/38147825/ correctly] publish the modification to the waiting thread.
Any thread that intends to wait on a `std::condition_variable` must:
# Acquire a `std::unique_lock<std::mutex>` on the mutex used to protect the shared variable.
# Do one of the following:
:# Check the condition, in case it was already updated and notified.
:# Call `wait`, `wait_for`, or `wait_until` on the `std::condition_variable` (atomically releases the mutex and suspends thread execution until the condition variable is notified, a timeout expires, or a [Spurious wakeup|spurious wakeup](https://en.wikipedia.org/wiki/Spurious wakeup|spurious wakeup) occurs, then atomically acquires the mutex before returning).
:# Check the condition and resume waiting if not satisfied.
:: or:
:# Use the predicated overload of `wait`, `wait_for`, and `wait_until`, which performs the same three steps.
`std::condition_variable` works only with `std::unique_lock<std::mutex>`, which allows for maximal efficiency on some platforms. `std::condition_variable_any` provides a condition variable that works with any *BasicLockable* object, such as `std::shared_lock`.
Condition variables permit concurrent invocation of the `wait`, `wait_for`, `wait_until`, `notify_one` and `notify_all` member functions.
The class `std::condition_variable` is a *StandardLayoutType*. It is not *CopyConstructible*, *MoveConstructible*, *CopyAssignable*, or *MoveAssignable*.

## Nested types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Member functions


| cpp/thread/condition_variable/dsc constructor|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc destructor|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc operator{{= | (see dedicated page) |

#### Notification

| cpp/thread/condition_variable/dsc notify_one|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc notify_all|condition_variable | (see dedicated page) |

#### Waiting

| cpp/thread/condition_variable/dsc wait|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_for|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable | (see dedicated page) |

#### Native handle

| cpp/thread/condition_variable/dsc native handle|condition_variable | (see dedicated page) |


## Example


### Example

```cpp
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>

std::mutex m;
std::condition_variable cv;
std::string data;
bool ready = false;
bool processed = false;

void worker_thread()
{
    // wait until main() sends data
    std::unique_lock lk(m);
    cv.wait(lk, []{ return ready; });

    // after the wait, we own the lock
    std::cout << "Worker thread is processing data\n";
    data += " after processing";

    // send data back to main()
    processed = true;
    std::cout << "Worker thread signals data processing completed\n";

    // manual unlocking is done before notifying, to avoid waking up
    // the waiting thread only to block again (see notify_one for details)
    lk.unlock();
    cv.notify_one();
}

int main()
{
    std::thread worker(worker_thread);

    data = "Example data";
    // send data to the worker thread
    {
        std::lock_guard lk(m);
        ready = true;
        std::cout << "main() signals data ready for processing\n";
    }
    cv.notify_one();

    // wait for the worker
    {
        std::unique_lock lk(m);
        cv.wait(lk, []{ return processed; });
    }
    std::cout << "Back in main(), data = " << data << '\n';

    worker.join();
}
```


**Output:**
```
main() signals data ready for processing
Worker thread is processing data
Worker thread signals data processing completed
Back in main(), data = Example data after processing
```


## See also


| cpp/thread/dsc condition_variable_any | (see dedicated page) |
| cpp/thread/dsc mutex | (see dedicated page) |
| cpp/thread/dsc lock_guard | (see dedicated page) |
| cpp/thread/dsc unique_lock | (see dedicated page) |

