---
title: std::condition_variable_any
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable_any
---

ddcl|header=condition_variable|since=c++11|1=
class condition_variable_any;
The `condition_variable_any` class is a generalization of `std::condition_variable`.  Whereas `std::condition_variable` works only on `std::unique_lock<std::mutex>`, `condition_variable_any` can operate on any lock that meets the *BasicLockable* requirements.
See `std::condition_variable` for the description of the semantics of condition variables.
The class `std::condition_variable_any` is a *StandardLayoutType*. It is not *CopyConstructible*, *MoveConstructible*, *CopyAssignable*, or *MoveAssignable*.
If the lock is `std::unique_lock<std::mutex>`, `std::condition_variable` may provide better performance.

## Member functions


| cpp/thread/condition_variable/dsc constructor|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc destructor|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc operator{{= | (see dedicated page) |

#### Notification

| cpp/thread/condition_variable/dsc notify_one|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc notify_all|condition_variable_any | (see dedicated page) |

#### Waiting

| cpp/thread/condition_variable/dsc wait|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_for|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable_any | (see dedicated page) |


## Notes

`std::condition_variable_any` can be used with `std::shared_lock` in order to wait on a `std::shared_mutex` in shared ownership mode.
A possible use for `std::condition_variable_any` with custom *Lockable* types is to provide convenient interruptible waits: the custom lock operation would both lock the associated mutex as expected, and also perform the necessary setup to notify this condition variable when the interrupting signal is received.<ref>Anthony Williams (2012, 1st ed./ 2019, 2nd ed.), “C++ Concurrency in Action”, 9.2.4 “Interrupting a wait on <code>std::condition_variable_any</code>”.</ref>

## See also


| cpp/thread/dsc condition_variable | (see dedicated page) |


## External links

