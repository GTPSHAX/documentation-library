---
title: std::shared_mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_mutex
---

ddcl|header=shared_mutex|since=c++17|1=
class shared_mutex;
The `shared_mutex` class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. In contrast to other mutex types which facilitate exclusive access, a shared_mutex has two levels of access:
* ''shared'' - several threads can share ownership of the same mutex.
* ''exclusive'' - only one thread can own the mutex.
If one thread has acquired the ''exclusive'' lock (through `lock`, `try_lock`), no other threads can acquire the lock (including the ''shared'').
If one thread has acquired the ''shared'' lock (through `lock_shared`, `try_lock_shared`), no other thread can acquire the ''exclusive'' lock, but can acquire the ''shared'' lock.
Only when the ''exclusive'' lock has not been acquired by any thread, the ''shared'' lock can be acquired by multiple threads.
Within one thread, only one lock (''shared'' or ''exclusive'') can be acquired at the same time.
Shared mutexes are especially useful when shared data can be safely read by any number of threads simultaneously, but a thread may only write the same data when no other thread is reading or writing at the same time.
The `shared_mutex` class satisfies all requirements of *SharedMutex* and *StandardLayoutType*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/thread/dsc native_handle_type|shared_mutex | (see dedicated page) |


## Member functions


| cpp/thread/mutex/dsc constructor|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc destructor|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc operator{{= | (see dedicated page) |

#### Exclusive locking

| cpp/thread/mutex/dsc lock|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock|shared_mutex | (see dedicated page) |

#### Shared locking

| cpp/thread/mutex/dsc lock_shared|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_shared|shared_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock_shared|shared_mutex | (see dedicated page) |

#### Native handle

| cpp/thread/mutex/dsc native_handle|shared_mutex | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <mutex>
#include <shared_mutex>
#include <syncstream>
#include <thread>

class ThreadSafeCounter
{
public:
    ThreadSafeCounter() = default;

    // Multiple threads/readers can read the counter's value at the same time.
    unsigned int get() const
    {
        std::shared_lock lock(mutex_);
        return value_;
    }

    // Only one thread/writer can increment/write the counter's value.
    void increment()
    {
        std::unique_lock lock(mutex_);
        ++value_;
    }

    // Only one thread/writer can reset/write the counter's value.
    void reset()
    {
        std::unique_lock lock(mutex_);
        value_ = 0;
    }

private:
    mutable std::shared_mutex mutex_;
    unsigned int value_{};
};

int main()
{
    ThreadSafeCounter counter;

    auto increment_and_print = [&counter]()
    {
        for (int i{}; i != 3; ++i)
        {
            counter.increment();
            std::osyncstream(std::cout)
                << std::this_thread::get_id() << ' ' << counter.get() << '\n';
        }
    };

    std::thread thread1(increment_and_print);
    std::thread thread2(increment_and_print);

    thread1.join();
    thread2.join();
}
```


**Output:**
```
123084176803584 2
123084176803584 3
123084176803584 4
123084185655040 1
123084185655040 5
123084185655040 6
```


## See also


| cpp/thread/dsc shared_timed_mutex | (see dedicated page) |
| cpp/thread/dsc shared_lock | (see dedicated page) |
| cpp/thread/dsc unique_lock | (see dedicated page) |

