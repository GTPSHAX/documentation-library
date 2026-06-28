---
title: std::future_errc
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_errc
---

ddcl|header=future|since=c++11|1=
enum class future_errc {
broken_promise             = /* implementation-defined */,
future_already_retrieved   = /* implementation-defined */,
promise_already_satisfied  = /* implementation-defined */,
no_state                   = /* implementation-defined */
};
The scoped enumeration `std::future_errc` defines the error codes reported by `std::future` and related classes in `std::future_error` exception objects. Only four error codes are required, although the implementation may define additional error codes. Because the appropriate specialization of `std::is_error_code_enum` is provided, values of type `std::future_errc` are implicitly convertible to `std::error_code`.
All error codes are distinct and non-zero.

## Member constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |


## Non-member functions


| cpp/thread/future_errc/dsc make_error_code | (see dedicated page) |
| cpp/thread/future_errc/dsc make_error_condition | (see dedicated page) |


## Helper classes


| cpp/thread/future_errc/dsc is_error_code_enum | (see dedicated page) |


## Example


## See also


| cpp/error/dsc error_code | (see dedicated page) |
| cpp/error/dsc error_condition | (see dedicated page) |

