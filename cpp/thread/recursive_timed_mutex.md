---
title: std::recursive_timed_mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/recursive_timed_mutex
---

ddcl|header=mutex|since=c++11|1=
class recursive_timed_mutex;
The `recursive_timed_mutex` class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads.
In a manner similar to `std::recursive_mutex`, `recursive_timed_mutex` provides exclusive, recursive ownership semantics. In addition, `recursive_timed_mutex` provides the ability to attempt to claim ownership of a `recursive_timed_mutex` with a timeout via the `try_lock_for` and `try_lock_until` member functions.
The `recursive_timed_mutex` class satisfies all requirements of *TimedMutex* and *StandardLayoutType*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/thread/dsc native_handle_type|recursive_timed_mutex | (see dedicated page) |


## Member functions


| cpp/thread/mutex/dsc constructor|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc destructor|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc operator{{= | (see dedicated page) |

#### Locking

| cpp/thread/mutex/dsc lock|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_for|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_until|recursive_timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock|recursive_timed_mutex | (see dedicated page) |

#### Native handle

| cpp/thread/mutex/dsc native_handle|recursive_timed_mutex | (see dedicated page) |

