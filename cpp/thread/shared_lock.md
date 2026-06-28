---
title: std::shared_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock
---

ddcl|header=shared_mutex|since=c++14|
template< class Mutex >
class shared_lock;
The class `shared_lock` is a general-purpose shared mutex ownership wrapper allowing deferred locking, timed locking and transfer of lock ownership. Locking a `shared_lock` locks the associated shared mutex in shared mode (to lock it in exclusive mode, `std::unique_lock` can be used).
The `shared_lock` class is movable, but not copyable &ndash; it meets the requirements of *MoveConstructible* and *MoveAssignable* but not of *CopyConstructible* or *CopyAssignable*.
`shared_lock` meets the *Lockable* requirements. If `Mutex` meets the *SharedTimedLockable* requirements, `shared_lock` also meets *TimedLockable* requirements.
In order to wait in a shared mutex in shared ownership mode, `std::condition_variable_any` can be used (`std::condition_variable` requires `std::unique_lock` and so can only wait in unique ownership mode).

## Template parameters


### Parameters

- `Mutex` - the type of the shared mutex to lock. The type must meet the *SharedLockable* requirements

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/thread/shared_lock/dsc constructor | (see dedicated page) |
| cpp/thread/shared_lock/dsc destructor | (see dedicated page) |
| cpp/thread/shared_lock/dsc operator{{= | (see dedicated page) |

#### Shared locking

| cpp/thread/shared_lock/dsc lock | (see dedicated page) |
| cpp/thread/shared_lock/dsc try_lock | (see dedicated page) |
| cpp/thread/shared_lock/dsc try_lock_for | (see dedicated page) |
| cpp/thread/shared_lock/dsc try_lock_until | (see dedicated page) |
| cpp/thread/shared_lock/dsc unlock | (see dedicated page) |

#### Modifiers

| cpp/thread/shared_lock/dsc swap | (see dedicated page) |
| cpp/thread/shared_lock/dsc release | (see dedicated page) |

#### Observers

| cpp/thread/shared_lock/dsc mutex | (see dedicated page) |
| cpp/thread/shared_lock/dsc owns_lock | (see dedicated page) |
| cpp/thread/shared_lock/dsc operator bool | (see dedicated page) |


## Non-member functions


| cpp/thread/shared_lock/dsc swap2 | (see dedicated page) |


## Defect reports

