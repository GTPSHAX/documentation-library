---
title: std::shared_timed_mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_timed_mutex
---

ddcl|header=shared_mutex|since=c++14|1=
class shared_timed_mutex;
The `shared_timed_mutex` class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. In contrast to other mutex types which facilitate exclusive access, a `shared_timed_mutex` has two levels of access:
* ''exclusive'' - only one thread can own the mutex.
* ''shared'' - several threads can share ownership of the same mutex.
Shared mutexes are usually used in situations when multiple readers can access the same resource at the same time without causing data races, but only one writer can do so.
In a manner similar to `cpp/thread/timed_mutex`, `shared_timed_mutex` provides the ability to attempt to claim ownership of a `shared_timed_mutex` with a timeout via the , , ,  member functions.
The `shared_timed_mutex` class satisfies all requirements of *SharedTimedMutex* and *StandardLayoutType*.

## Member functions


| cpp/thread/mutex/dsc constructor|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc destructor|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc operator{{= | (see dedicated page) |

#### Exclusive locking

| cpp/thread/mutex/dsc lock|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_for|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_until|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock|shared_timed_mutex | (see dedicated page) |

#### Shared locking

| cpp/thread/mutex/dsc lock_shared|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_shared|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_shared_for|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_shared_until|shared_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock_shared|shared_timed_mutex | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <mutex>
#include <shared_mutex>

class R
{
    mutable std::shared_timed_mutex mut;
    /* data */
public:
    R& operator=(const R& other)
    {
        // requires exclusive ownership to write to *this
        std::unique_lock<std::shared_timed_mutex> lhs(mut, std::defer_lock);
        // requires shared ownership to read from other
        std::shared_lock<std::shared_timed_mutex> rhs(other.mut, std::defer_lock);
        std::lock(lhs, rhs);
        /* assign data */
        return *this;
    }
};

int main()
{
    R r;
}
```

