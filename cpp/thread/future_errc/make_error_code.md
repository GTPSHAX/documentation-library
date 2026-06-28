---
title: std::make_error_code(std::future_errc)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_errc/make_error_code
---


# make_error_codedsc small|(std::future_errc)


```cpp
dcl | since=c++11 |
std::error_code make_error_code( std::future_errc e );
```

Constructs an `std::error_code` object from a value of type `std::future_errc` as if by:
.
This function is called by the constructor of `std::error_code` when given an `std::future_errc` argument.

## Parameters


### Parameters


## Return value

A value of type `std::error_code` that holds the error code number from `e` associated with the error category `"future"`.

## Example


## See also

