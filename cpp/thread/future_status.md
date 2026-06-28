---
title: std::future_status
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_status
---

ddcl|header=future|since=c++11|1=
enum class future_status {
ready,
timeout,
deferred
};
Specifies state of a future as returned by `wait_for` and `wait_until` functions of `std::future` and `std::shared_future`.

## Constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |


## See also


| cpp/thread/future/dsc wait_for|future | (see dedicated page) |
| cpp/thread/future/dsc wait_for|shared_future | (see dedicated page) |
| cpp/thread/future/dsc wait_until|future | (see dedicated page) |
| cpp/thread/future/dsc wait_until|shared_future | (see dedicated page) |

