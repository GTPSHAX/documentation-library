---
title: std::packaged_task::operator()
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/operator()
---

ddcl|since=c++11|
void operator()( Args... args );
Calls the stored task as if by , where `f` is the stored task. The return value of the task or any exceptions thrown are stored in the shared state. The shared state is made ready and any threads waiting for this are unblocked.

## Parameters


### Parameters

- `args` - the parameters to pass on invocation of the stored task

## Return value

(none)

## Exceptions

`std::future_error` on the following error conditions:
* The stored task has already been invoked. The error category is set to `cpp/thread/future_errc|promise_already_satisfied`.
* `*this` has no shared state. The error category is set to `cpp/thread/future_errc|no_state`.

## Example


## Defect reports


## See also


| cpp/thread/packaged_task/dsc make_ready_at_thread_exit | (see dedicated page) |

