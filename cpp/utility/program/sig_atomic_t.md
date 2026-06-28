---
title: std::sig_atomic_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/sig_atomic_t
---

ddcl | header=csignal |
typedef /* unspecified */ sig_atomic_t;
An integer type which can be accessed as an atomic entity even in the presence of asynchronous interrupts made by signals.

## Notes

Until C++11, which introduced `std::atomic` and `std::atomic_signal_fence`, about the only thing a strictly conforming program could do in a signal handler was to assign a value to a `volatile static std::sig_atomic_t` variable and promptly return.

## See also

