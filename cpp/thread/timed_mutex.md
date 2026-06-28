---
title: std::timed_mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/timed_mutex
---

ddcl|header=mutex|since=c++11|1=
class timed_mutex;
The `timed_mutex` class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads.
In a manner similar to `cpp/thread/mutex`, `timed_mutex` offers exclusive, non-recursive ownership semantics. In addition, `timed_mutex` provides the ability to attempt to claim ownership of a `timed_mutex` with a timeout via the member functions  and .
The `timed_mutex` class satisfies all requirements of *TimedMutex* and *StandardLayoutType*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/thread/dsc native_handle_type|timed_mutex | (see dedicated page) |


## Member functions


| cpp/thread/mutex/dsc constructor|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc destructor|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc operator{{= | (see dedicated page) |

#### Locking

| cpp/thread/mutex/dsc lock|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_for|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc try_lock_until|timed_mutex | (see dedicated page) |
| cpp/thread/mutex/dsc unlock|timed_mutex | (see dedicated page) |

#### Native handle

| cpp/thread/mutex/dsc native_handle|timed_mutex | (see dedicated page) |

