---
title: std::future::get
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future/get
---


```cpp
dcl|num=1|since=c++11|
T get();
dcl|num=2|since=c++11|
T& get();
dcl|num=3|since=c++11|
void get();
```

The `get` member function waits (by calling `wait()`) until the shared state is ready, then retrieves the value stored in the shared state (if any). Right after calling this function, `valid()` is `false`.
If `valid()` is `false` before the call to this function, the behavior is undefined.

## Return value

1. The value `v` stored in the shared state, as `std::move(v)`.
2. The reference stored as value in the shared state.
3. (none)

## Exceptions

If an exception was stored in the shared state referenced by the future (e.g. via a call to ) then that exception will be thrown.

## Notes

The C++ standard recommends the implementations to detect the case when `valid()` is `false` before the call and throw a `std::future_error` with an error condition of `std::future_errc::no_state`.

## Example


### Example


**Output:**
```
[0.000004s] launching thread
[0.000461s] waiting for the future, f.valid() = 1
[1.001156s] f.get() returned with 7, f.valid() = 0
[1.001192s] launching thread
[1.001275s] waiting for the future, f.valid() = 1
[2.002356s] caught exception 7, f.valid() = 0
```


## Defect reports


## See also


| cpp/thread/future/dsc valid|future | (see dedicated page) |

