---
title: std::unique_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock
---

ddcl|header=mutex|since=c++11|1=
template< class Mutex >
class unique_lock;
The class `unique_lock` is a general-purpose mutex ownership wrapper allowing deferred locking, time-constrained attempts at locking, recursive locking, transfer of lock ownership, and use with condition variables.
The class `unique_lock` is movable, but not copyable -- it meets the requirements of *MoveConstructible* and *MoveAssignable* but not of *CopyConstructible* or *CopyAssignable*.
The class `unique_lock` meets the *BasicLockable* requirements. If `Mutex` meets the *Lockable* requirements, `unique_lock` also meets the *Lockable* requirements (ex.: can be used in `std::lock`); if `Mutex` meets the *TimedLockable* requirements, `unique_lock` also meets the *TimedLockable* requirements.

## Template parameters


### Parameters

- `Mutex` - the type of the mutex to lock. The type must meet the *BasicLockable* requirements

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/thread/unique_lock/dsc constructor | (see dedicated page) |
| cpp/thread/unique_lock/dsc destructor | (see dedicated page) |
| cpp/thread/unique_lock/dsc operator{{= | (see dedicated page) |

#### Locking

| cpp/thread/unique_lock/dsc lock | (see dedicated page) |
| cpp/thread/unique_lock/dsc try_lock | (see dedicated page) |
| cpp/thread/unique_lock/dsc try_lock_for | (see dedicated page) |
| cpp/thread/unique_lock/dsc try_lock_until | (see dedicated page) |
| cpp/thread/unique_lock/dsc unlock | (see dedicated page) |

#### Modifiers

| cpp/thread/unique_lock/dsc swap | (see dedicated page) |
| cpp/thread/unique_lock/dsc release | (see dedicated page) |

#### Observers

| cpp/thread/unique_lock/dsc mutex | (see dedicated page) |
| cpp/thread/unique_lock/dsc owns_lock | (see dedicated page) |
| cpp/thread/unique_lock/dsc operator bool | (see dedicated page) |


## Non-member functions


| cpp/thread/unique_lock/dsc swap2 | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <mutex>
#include <thread>

struct Box
{
    explicit Box(int num) : num_things{num} {}

    int num_things;
    std::mutex m;
};

void transfer(Box& from, Box& to, int num)
{
    // don't actually take the locks yet
    std::unique_lock lock1{from.m, std::defer_lock};
    std::unique_lock lock2{to.m, std::defer_lock};

    // lock both unique_locks without deadlock
    std::lock(lock1, lock2);

    from.num_things -= num;
    to.num_things += num;

    // “from.m” and “to.m” mutexes unlocked in unique_lock dtors
}

int main()
{
    Box acc1{100};
    Box acc2{50};

    std::thread t1{transfer, std::ref(acc1), std::ref(acc2), 10};
    std::thread t2{transfer, std::ref(acc2), std::ref(acc1), 5};

    t1.join();
    t2.join();

    std::cout << "acc1: " << acc1.num_things << "\n"
                 "acc2: " << acc2.num_things << '\n';
}
```


**Output:**
```
acc1: 95
acc2: 55
```


## Defect reports


## See also


| cpp/thread/dsc lock | (see dedicated page) |
| cpp/thread/dsc lock_guard | (see dedicated page) |
| cpp/thread/dsc scoped_lock | (see dedicated page) |
| cpp/thread/dsc mutex | (see dedicated page) |

