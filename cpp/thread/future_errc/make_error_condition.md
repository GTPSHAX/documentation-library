---
title: std::make_error_condition(std::future_errc)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_errc/make_error_condition
---


# make_error_conditiondsc small|(std::future_errc)


```cpp
dcl | since=c++11 |
std::error_condition make_error_condition( std::future_errc e );
```

Constructs an `std::error_condition` object from a value of type `std::future_errc` as if by:
.

## Parameters


### Parameters


## Return value

A value of type `std::error_condition` that holds the error code number from `e` associated with the error category `"future"`.

## Example


## See also

