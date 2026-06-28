---
title: Concurrency support library
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread
---


# Concurrency support library mark since c++11

C++ includes built-in support for threads, atomic operations, mutual exclusion, condition variables, and futures.

## Threads

Threads enable programs to execute across several processor cores.


| thread | |
| cpp/thread/dsc thread | (see dedicated page) |
| cpp/thread/dsc jthread | (see dedicated page) |

#### Functions managing the current thread

| this_thread | |
| cpp/thread/dsc yield | (see dedicated page) |
| cpp/thread/dsc get_id | (see dedicated page) |
| cpp/thread/dsc sleep_for | (see dedicated page) |
| cpp/thread/dsc sleep_until | (see dedicated page) |


## Cooperative cancellation <sup>(C++20)</sup>

The components ''stop source'', ''stop token'', and ''stop callback'' can be used to asynchronously request that an operation stops execution in a timely manner, typically because the result is no longer required. Such a request is called a ''stop request''.
These components specify the semantics of shared access to a ''stop state''. Any object modeling any of these components that refer to the same stop state is an associated stop source, stop token, or stop callback, respectively.
rrev|since=c++26|
The concepts , , and  specify the required syntax and model semantics of stop source, stop token, and stop callback, respectively.
They are designed:
* to cooperatively cancel the execution such as for `std::jthread`,
* to interrupt `std::condition_variable_any` waiting functions,
<sup>(since C++26)</sup> * to perform stopped completion of an asynchronous operation created by `execution::connect`,
* or for a custom execution management implementation.
In fact, they do not even need to be used to "stop" anything, but can instead be used for a thread-safe one-time function(s) invocation trigger, for example.


| stop_token | |

#### Stop token types

| cpp/thread/dsc stop_token | (see dedicated page) |
| cpp/thread/dsc never_stop_token | (see dedicated page) |
| cpp/thread/dsc inplace_stop_token | (see dedicated page) |

#### Stop source types

| cpp/thread/dsc stop_source | (see dedicated page) |
| cpp/thread/dsc inplace_stop_source | (see dedicated page) |

#### Stop callback types

| cpp/thread/dsc stop_callback | (see dedicated page) |
| cpp/thread/dsc inplace_stop_callback | (see dedicated page) |
| cpp/thread/dsc stop_callback_for_t | (see dedicated page) |

#### Concepts {{mark since c++20

| cpp/thread/dsc stoppable_token | (see dedicated page) |
| cpp/thread/dsc unstoppable_token | (see dedicated page) |
| cpp/thread/dsc stoppable_source | (see dedicated page) |
| cpp/thread/dsc stoppable_callback_for | (see dedicated page) |


## Cache size access <sup>(C++17)</sup>


| new | |
| cpp/thread/dsc hardware_destructive_interference_size | (see dedicated page) |


## Atomic operations

These components are provided for fine-grained atomic operations allowing for lockless concurrent programming. Each atomic operation is indivisible with regards to any other atomic operation that involves the same object. Atomic objects are free of data races.


| atomic | |

#### Atomic types

| cpp/atomic/dsc atomic | (see dedicated page) |
| cpp/atomic/dsc atomic_ref | (see dedicated page) |

#### Operations on atomic types

| cpp/atomic/dsc atomic_is_lock_free | (see dedicated page) |
| cpp/atomic/dsc atomic_store | (see dedicated page) |
| cpp/atomic/dsc atomic_load | (see dedicated page) |
| cpp/atomic/dsc atomic_exchange | (see dedicated page) |
| cpp/atomic/dsc atomic_compare_exchange | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_add | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_sub | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_and | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_or | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_xor | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_max | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_min | (see dedicated page) |
| cpp/atomic/dsc atomic_wait | (see dedicated page) |
| cpp/atomic/dsc atomic_notify_one | (see dedicated page) |
| cpp/atomic/dsc atomic_notify_all | (see dedicated page) |

#### Flag type and operations

| cpp/atomic/dsc atomic_flag | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_test_and_set | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_clear | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_test | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_wait | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_notify_one | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_notify_all | (see dedicated page) |

#### Initialization

| cpp/atomic/dsc atomic_init | (see dedicated page) |
| cpp/atomic/dsc ATOMIC_VAR_INIT | (see dedicated page) |
| cpp/atomic/dsc ATOMIC_FLAG_INIT | (see dedicated page) |

#### Memory synchronization ordering

| cpp/atomic/dsc memory_order | (see dedicated page) |
| cpp/atomic/dsc kill_dependency | (see dedicated page) |
| cpp/atomic/dsc atomic_thread_fence | (see dedicated page) |
| cpp/atomic/dsc atomic_signal_fence | (see dedicated page) |
| stdatomic.h | |

#### C compatibility macros {{mark since c++23

| cpp/atomic/dsc _Atomic | (see dedicated page) |

Neither the `_Atomic` macro, nor any of the non-macro global namespace declarations are provided by any C++ standard library header other than `<stdatomic.h>`.

## Mutual exclusion

Mutual exclusion algorithms prevent multiple threads from simultaneously accessing shared resources. This prevents data races and provides support for synchronization between threads.


| mutex | |
| cpp/thread/dsc mutex | (see dedicated page) |
| cpp/thread/dsc timed_mutex | (see dedicated page) |
| cpp/thread/dsc recursive_mutex | (see dedicated page) |
| cpp/thread/dsc recursive_timed_mutex | (see dedicated page) |
| shared_mutex | |
| cpp/thread/dsc shared_mutex | (see dedicated page) |
| cpp/thread/dsc shared_timed_mutex | (see dedicated page) |

#### Generic mutex management

| mutex | |
| cpp/thread/dsc lock_guard | (see dedicated page) |
| cpp/thread/dsc scoped_lock | (see dedicated page) |
| cpp/thread/dsc unique_lock | (see dedicated page) |
| cpp/thread/dsc shared_lock | (see dedicated page) |
| cpp/thread/dsc lock_tag | (see dedicated page) |

#### Generic locking algorithms

| cpp/thread/dsc try_lock | (see dedicated page) |
| cpp/thread/dsc lock | (see dedicated page) |

#### Call once

| cpp/thread/dsc once_flag | (see dedicated page) |
| cpp/thread/dsc call_once | (see dedicated page) |


## Condition variables

A condition variable is a synchronization primitive that allows multiple threads to communicate with each other.  It allows some number of threads to wait (possibly with a timeout) for notification from another thread that they may proceed. A condition variable is always associated with a mutex.


| condition_variable | |
| cpp/thread/dsc condition_variable | (see dedicated page) |
| cpp/thread/dsc condition_variable_any | (see dedicated page) |
| cpp/thread/dsc notify_all_at_thread_exit | (see dedicated page) |
| cpp/thread/dsc cv_status | (see dedicated page) |


## Semaphores <sup>(C++20)</sup>

A semaphore is a lightweight synchronization primitive used to constrain concurrent access to a shared resource. When either would suffice, a semaphore can be more efficient than a condition variable.


| semaphore | |
| cpp/thread/dsc counting_semaphore | (see dedicated page) |
| cpp/thread/dsc binary_semaphore | (see dedicated page) |


## Latches and Barriers <sup>(C++20)</sup>

Latches and barriers are thread coordination mechanisms that allow any number of threads to block until an expected number of threads arrive. A latch cannot be reused, while a barrier can be used repeatedly.


| latch | |
| cpp/thread/dsc latch | (see dedicated page) |
| barrier | |
| cpp/thread/dsc barrier | (see dedicated page) |


## Futures

The standard library provides facilities to obtain values that are returned and to catch exceptions that are thrown by asynchronous tasks (i.e. functions launched in separate threads). These values are communicated in a ''shared state'', in which the asynchronous task may write its return value or store an exception, and which may be examined, waited for, and otherwise manipulated by other threads that hold instances of `std::future` or `std::shared_future` that reference that shared state.


| future | |
| cpp/thread/dsc promise | (see dedicated page) |
| cpp/thread/dsc packaged_task | (see dedicated page) |
| cpp/thread/dsc future | (see dedicated page) |
| cpp/thread/dsc shared_future | (see dedicated page) |
| cpp/thread/dsc async | (see dedicated page) |
| cpp/thread/dsc launch | (see dedicated page) |
| cpp/thread/dsc future_status | (see dedicated page) |

#### Future errors

| cpp/thread/dsc future_error | (see dedicated page) |
| cpp/thread/dsc future_category | (see dedicated page) |
| cpp/thread/dsc future_errc | (see dedicated page) |


## Safe Reclamation <sup>(C++26)</sup>

Safe-reclamation techniques are most frequently used to straightforwardly resolve access-deletion races.


#### Read-Copy-Update Mechanism

| rcu | |
| cpp/thread/dsc rcu_obj_base | (see dedicated page) |
| cpp/thread/dsc rcu_domain | (see dedicated page) |
| cpp/thread/dsc rcu_default_domain | (see dedicated page) |
| cpp/thread/dsc rcu_synchronize | (see dedicated page) |
| cpp/thread/dsc rcu_barrier | (see dedicated page) |
| cpp/thread/dsc rcu_retire | (see dedicated page) |

#### Hazard Pointers

| hazard_pointer | |
| cpp/thread/dsc hazard_pointer_obj_base | (see dedicated page) |
| cpp/thread/dsc hazard_pointer | (see dedicated page) |
| cpp/thread/dsc make_hazard_pointer | (see dedicated page) |


## See also

