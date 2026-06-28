---
title: std::jthread
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/jthread
---

ddcl|header=thread|since=c++20|
class jthread;
The class `jthread` represents a single thread of execution. It has the same general behavior as `std::thread`, except that `jthread` automatically rejoins on destruction, and can be cancelled/stopped in certain situations.
Threads begin execution immediately upon construction of the associated thread object (pending any OS scheduling delays), starting at the top-level function provided as a `constructor argument`. The return value of the top-level function is ignored and if it terminates by throwing an exception, `std::terminate` is called. The top-level function may communicate its return value or an exception to the caller via `std::promise` or by modifying shared variables (which may require synchronization, see `std::mutex` and `std::atomic`).
Unlike `std::thread`, the `jthread` logically holds an internal private member of type `std::stop_source`, which maintains a shared stop-state. The `jthread` constructor accepts a function that takes a `std::stop_token` as its first argument, which will be passed in by the `jthread` from its internal `std::stop_source`. This allows the function to check if stop has been requested during its execution, and return if it has.
`std::jthread` objects may also be in the state that does not represent any thread (after default construction, move from, `detach`, or `join`), and a thread of execution may be not associated with any `jthread` objects (after `detach`).
No two `std::jthread` objects may represent the same thread of execution; `std::jthread` is not *CopyConstructible* or *CopyAssignable*, although it is *MoveConstructible* and *MoveAssignable*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/thread/dsc native_handle_type|jthread | (see dedicated page) |


## Member functions


| cpp/thread/jthread/dsc constructor | (see dedicated page) |
| cpp/thread/jthread/dsc destructor | (see dedicated page) |
| 1=cpp/thread/jthread/dsc operator= | (see dedicated page) |

#### Observers

| cpp/thread/thread/dsc joinable|jthread | (see dedicated page) |
| cpp/thread/thread/dsc get_id|jthread | (see dedicated page) |
| cpp/thread/thread/dsc native_handle|jthread | (see dedicated page) |
| cpp/thread/thread/dsc hardware_concurrency|jthread | (see dedicated page) |

#### Operations

| cpp/thread/thread/dsc join|jthread | (see dedicated page) |
| cpp/thread/thread/dsc detach|jthread | (see dedicated page) |
| cpp/thread/thread/dsc swap|jthread | (see dedicated page) |

#### Stop token handling

| cpp/thread/jthread/dsc get_stop_source | (see dedicated page) |
| cpp/thread/jthread/dsc get_stop_token | (see dedicated page) |
| cpp/thread/jthread/dsc request_stop | (see dedicated page) |


## Non-member functions


| cpp/thread/thread/dsc swap2|jthread | (see dedicated page) |


## Notes


## See also


| cpp/thread/dsc thread | (see dedicated page) |

