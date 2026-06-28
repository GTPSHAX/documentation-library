---
title: std::cv_status
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/cv_status
---

ddcl|header=condition_variable|since=c++11|
enum class cv_status {
no_timeout,
timeout
};
The scoped enumeration `std::cv_status` describes whether a timed wait returned because of timeout or not.
`std::cv_status` is used by the `wait_for` and `wait_until` member functions of `std::condition_variable` and `std::condition_variable_any`.

## Member constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |


## See also


| cpp/thread/condition_variable/dsc wait_for|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_for|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable_any | (see dedicated page) |

